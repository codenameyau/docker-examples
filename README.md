# docker-examples

### Cheatsheet

```bash
# Stop all containers.
sudo docker stop $(sudo docker ps -aq)

# Remove all containers.
sudo docker rm $(sudo docker ps -aq)

# Remove image.
sudo docker rmi <image-id>

# Remove all images.
sudo docker rmi $(sudo docker images -q)
```

--

### Building and running a local container

```bash
# Build image locally.
sudo docker build -t <username>/<repo> .

# Find your new docker image.
sudo docker images

# Run container (forward ports -> host:guest)
sudo docker run -dit -p 8080:80 <image-id>
sudo docker run -dit -p 8080:80 <image-name>
sudo docker run -dit -p 8080:80 <image-name> -name <container-name>

# SSH into container via attachment (halts process if you exit).
sudo docker ps
sudo docker attach <container-id>
sudo docker attach <container-name>

# SSH into container via new process (won't halt if you exit).
sudo docker exec -it <container-id> bash
```

--

### Publishing container to Dockerhub

```bash
# Create a Dockerhub account.
https://hub.docker.com/

# Log into your Dockerhub account in your terminal.
sudo docker login

# Publish container
sudo docker push <username>/<repo>
```
