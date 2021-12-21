#!/bin/sh

docker-compose build
sudo bash ./clean.sh
docker-compose up