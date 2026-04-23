#!/bin/bash
set -e

IMAGE_NAME="myapi"
PORT=${PORT:-8000}

echo "Stopping old container..."
docker compose down 2>/dev/null || true

echo "Building Docker image..."
docker build -t $IMAGE_NAME .

echo "Starting container on port $PORT..."
PORT=$PORT docker compose up -d

echo "Waiting for app to start..."
sleep 3
curl -f http://localhost:$PORT/health && echo "App is healthy!"
