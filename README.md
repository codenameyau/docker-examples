# docker-examples

### Cheatsheet

```bash
# Stop all containers.
sudo docker stop $(sudo docker ps -a -q)

# Remove all containers.
sudo docker rm $(sudo docker ps -a -q)
```

--

### Building a local docker container.
```bash
# Build image locally.
sudo docker build .

# Find your new docker image.
sudo docker images

# Run container (ports -> host:guest)
sudo docker run -dit -p 8080:80 <image-id>

# SSH into container
sudo docker ps
sudo docker attach <container-id>
```

--

### Publishsing a conatainer to Dockerhub.
```bash
# Create a Dockerhub account.
https://hub.docker.com/

# Log into your Dockerhub account in your terminal.
sudo docker login

# Publish container
sudo docker build -t <username>/<repo> .
sudo docker push <username>/<repo>
```
