#!/bin/bash

git pull

docker-compose -f docker-compose.prod.yaml down
docker-compose -f docker-compose.prod.yaml up -d
docker exec sto_sunn_web python /app/sto_sunn/manage.py migrate --no-input
docker exec sto_sunn_web python /app/sto_sunn/manage.py collectstatic --no-input


