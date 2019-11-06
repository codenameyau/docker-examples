#!/bin/bash
#
# Description:
# Automatically builds or rebuilds a docker image while stopping
# and removing all existing containers that using that image.
#
# Usage:
# $ chmod 766 docker-build.sh
# $ cd <directory-with-dockerfile
# $ sudo docker-build.sh <image-name-or-id>

if [ -z "$1" ]; then
  echo "Specify a docker image to rebuild"; exit
fi

docker_image_name="$1"
echo sudo docker ps -a | grep "codenameyau/dev-flask" | awk '{ print $1 }'
