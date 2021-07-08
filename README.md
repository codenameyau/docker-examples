# docker-examples
- https://github.com/wsargent/docker-cheat-sheet
- https://docs.docker.com/get-started/part2/
- http://containertutorials.com/docker-compose/flask-simple-app.html
- https://jpetazzo.github.io/2013/12/01/docker-python-pip-requirements/

## Cheatsheet

```bash
# Starts a container.
docker start

# Stop all containers.
docker stop $(docker ps -aq)

# Remove all containers.
docker rm $(docker ps -aq)

# Remove image.
docker rmi <image-id>

# Remove all images.
docker rmi $(docker images -q)

# List running containers.
docker ps

# Lists all containers and list just the container ids.
docker ps -a

# List just the container ids.
docker ps -q
```

### Building and running a local container

```bash
# Find your new docker image.
docker images

# Build the image
docker build -t <image-name> .

# Run container in detached mode.
docker run -d <name>

# Run container (forward ports -> host:guest)
docker run -dit -p 8080:80 <image-id-or-name>

# (Optional) You can also specify the container name.
docker run -dit -p 8080:80 <image-id-or-name> -name <container-name>

# Debug exited containers by removing the '-d' flag.
docker run -it <image-id-or-name>

# Run container with synced volume from host to guest.
docker run -it -p 8080:80 -v $(pwd):<guest-dir> <image-name>

# Example: /darth_varder/ will be available in guest.
docker run -it -v $HOME/Workspace/tf_files:/darth_vader c3efccc5f94f

# SSH into container via attachment (halts process if you exit).
docker attach <container-id>

# SSH into container via new process (won't halt if you exit).
docker exec -it <container-id> bash
```

### Basic Setup
```bash
docker build -t nltk-flask .
docker run -dit -p 5000:5000 nltk-flask
```

Then visit: http://localhost:5000

```bash
# To enter container, run:
docker ps
docker exec -it <container-id-or-name> bash

# While inside container use exit to prevent shutting down container.
$ exit
```

## Publishing container to Dockerhub

```bash
# Build image locally.
docker build -t <username>/<repo> .

# Create a Dockerhub account.
https://hub.docker.com/

# Log into your Dockerhub account in your terminal.
docker login

# Publish container
docker push <username>/<repo>
```

## Docker on MacOS

https://docs.docker.com/docker-for-mac/

This link will tell you everything about setting up docker for Mac, what the GUI does,
how to setup preferences, how to start file sharing, and how to perform more advanced
tasks such as setting up certificates.

### Setup
Try to run this simple command to spin up a new nginx docker webserver.
```bash
docker run -d -p 80:80 --name webserver nginx
```

If you see this error, then open up Docker application via GUI with CMD+space, then
type docker. It will tell you to install and relaunch docker.
```bash
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
```

Once that's complete you can stop or remove the web server container.
```bash
docker stop webserver
docker rm -f webserver
docker rmi nginx
```

## Docker scan
Docker scan is a tool that can be used to scan for container security vulnerabilities. It returns an exit code 1
whenever there is a high severity vulnerabiity and can be added into a CI/CD pipeline.

```sh
# Log into docker hub account.
docker login

# Scan image for vulnerabilities.
docker scan <image>
```


## Anchore
Anchore is a tool that can be integrated with the CI/CD pipeline to automate the process of checking for security
vulnerabilities in a Docker image. To get started follow the instructions on this README:

https://github.com/anchore/anchore-engine


```sh
# Add an image from docker.io
anchore-cli --u admin --p foobar image add node:14

# Add an image from host machine. (TODO)
anchore-cli --u admin --p foobar image add node:14

# List images.
anchore-cli --u admin --p foobar image list

# Get image details.
anchore-cli --u admin --p foobar image get node:12

# See files.
anchore-cli --u admin --p foobar image content node:12 files

# See OS libraries.
anchore-cli --u admin --p foobar image content node:12 os

# See image vulnerabilities
anchore-cli --u admin --p foobar image vuln node:12 os

# See system status.
anchore-cli --u admin --p foobar system status

# See system feed.
anchore-cli --u admin --p foobar system feeds list
```

You can also set the following environment variables for authorization so you can omit the `--u admin` and `--p foobar` options.

```sh
# First set these environment variables.
ANCHORE_CLI_URL=http://localhost:8228/v1
ANCHORE_CLI_USER=admin
ANCHORE_CLI_PASS=foobar
```
