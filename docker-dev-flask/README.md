# docker-flask

Application Stack: python3, pip3, flask.

### Container Details
This is a flask docker image that is compatible with AWS Elasticbeanstalk--The WSGI
file is named `application.py` and there is a `requirements.txt`. This image is only
meant to be used for development as a replacement for Vagrant or host provisioned machine.

See [docker-nginx-flask](https://github.com/codenameyau/docker-examples/tree/master/docker-nginx-flask)
if you want to use a image that can be used in both dev and production.

--

### Setup

```bash
# Build the docker image.
docker build -t <image-name> .

# Build a docker container instance.
docker run -dit -p 8080:5000 -v $(pwd):/srv <image-name>

# Attach the container.
sudo docker exec -it <container-id> bash

# Running local flask dev server.
cd /srv/app
python3 run.py

# Then visit your browser or mobile device at:
http://localhost:8080
```
