#!/bin/sh

docker-compose rm -f -v
docker volume rm $(docker volume ls | grep data-platform-engineer | awk '{print $2}')