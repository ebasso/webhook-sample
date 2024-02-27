import os
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Get environment variables
WEBHOOK_KEY = os.environ.get("WEBHOOK_KEY")
GIT_BRANCH = os.environ.get("GIT_BRANCH")
GIT_REPO_URL = os.environ.get("GIT_REPO_URL")

# Endpoint to receive webhook from Git
@app.route('/webhook', methods=['POST'])
def webhook():
    # Check if the request contains the webhook key
    if request.headers.get('X-Webhook-Key') != WEBHOOK_KEY:
        return jsonify({'error': 'Unauthorized'}), 401

    git_data = request.json
    git_repo_url = git_data['repository']['clone_url']
    git_branch = git_data['ref'].split('/')[-1]  # Extract branch name

    # Clone Git repository and perform Ant build
    try:
        subprocess.run(['git', 'clone', '--branch', git_branch, git_repo_url])
        subprocess.run(['ant'])  # Assuming 'ant' command runs the build process
        return jsonify({'message': 'Ant build completed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
