


This command generates a random string of 32 bytes and encodes it in base64 format.

```
openssl rand -base64 32
```

For example, to set the generated webhook key as an environment variable in Unix-like systems, you can do:

```bash
export WEBHOOK_KEY=$(openssl rand -base64 32)
```

To build your Docker image, navigate to the directory containing the Dockerfile and run:
```
docker build -t your-image-name .
```


To add the webhook key as an environment variable when running the Container, 
```
docker run -d -p 5000:5000 -e WEBHOOK_KEY="your_webhook_key" --name your-container-name your-image-name
```


