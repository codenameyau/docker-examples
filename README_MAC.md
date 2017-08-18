# Docker on MacOS

https://docs.docker.com/docker-for-mac/

This documentation link will tell you everything about setting up docker for Mac, what the GUI does, how to setup preferences, how to start file sharing, and how to perform more advanced tasks such as setting up certificates. 

### Setup
Try to run this simple command to spin up a new nginx docker webserver.
```bash
sudo docker run -d -p 80:80 --name webserver nginx
```

If you see this error, then open up Docker application via GUI with CMD+space, then
type docker. It will tell you to install and relaunch docker.
```bash
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
```

Once that's complete you can stop or remove the web server container.
```bash
sudo docker stop webserver
sudo docker rm -f webserver
sudo docker rmi nginx
```
