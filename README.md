# docker-examples
- https://github.com/wsargent/docker-cheat-sheet
- https://docs.docker.com/get-started/part2/
- http://containertutorials.com/docker-compose/flask-simple-app.html
- https://jpetazzo.github.io/2013/12/01/docker-python-pip-requirements/

### Cheatsheet

```bash
# Starts a container.
docker start

# Stop all containers.
sudo docker stop $(sudo docker ps -aq)

# Remove all containers.
sudo docker rm $(sudo docker ps -aq)

# Remove image.
sudo docker rmi <image-id>

# Remove all images.
sudo docker rmi $(sudo docker images -q)
```

### Building and running a local container

```bash
# Find your new docker image.
sudo docker images

# Run container (forward ports -> host:guest)
sudo docker run -dit -p 8080:80 <image-id-or-name>
sudo docker run -dit -p 8080:80 <image-id-or-name> -name <container-name>

# Debug exited containers by removing the '-d' flag.
sudo docker run -it <image-id-or-name>

# Run container with synced volume from host to guest.
sudo docker run -dit -p 8080:80 -v $(pwd):<guest-dir> <image-name>

# Example: /darth_varder/ will be available in guest.
sudo docker run -it -v $HOME/Workspace/tf_files:/darth_vader c3efccc5f94f

# Lists all available containers and list just the container ids.
sudo docker ps -aq

# SSH into container via attachment (halts process if you exit).
sudo docker attach <container-id>

# SSH into container via new process (won't halt if you exit).
sudo docker exec -it <container-id> bash
```

### Basic Setup
```bash
sudo docker build -t nltk-flask .
sudo docker run -dit -p 5000:5000 nltk-flask
```

Then visit: http://localhost:5000

```bash
# To enter container, run:
sudo docker ps
sudo docker exec -it <container-id-or-name> bash

# While inside container use exit to prevent shutting down container.
$ exit
```

### Publishing container to Dockerhub

```bash
# Build image locally.
sudo docker build -t <username>/<repo> .

# Create a Dockerhub account.
https://hub.docker.com/

# Log into your Dockerhub account in your terminal.
sudo docker login

# Publish container
sudo docker push <username>/<repo>
```
