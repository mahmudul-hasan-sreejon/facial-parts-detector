#!/bin/bash

# docker stop container_name
# docker rm container_name
# docker rmi -f image_name

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)