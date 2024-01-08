#!/bin/bash

# This script is used to deploy the AI Content Generation Project.

# Exit on any non-zero status.
set -e

# Navigate to the directory containing the Dockerfile
cd "$(dirname "$0")"

# Load environment variables from .env file if it exists
if [ -f .env ]; then
  export $(cat .env | xargs)
fi

# Build the Docker image
echo "Building Docker image..."
docker build -t ai-content-generation-project .

# Check if a container with the same name is already running
CONTAINER_NAME="ai_content_generation_app"
if [ "$(docker ps -aq -f name=^${CONTAINER_NAME}$)" ]; then
    # Stop and remove the existing container
    echo "An existing container found. Stopping and removing it..."
    docker stop ${CONTAINER_NAME}
    docker rm ${CONTAINER_NAME}
fi

# Run the Docker container
echo "Running Docker container..."
docker run -d --name ${CONTAINER_NAME} -p 80:80 ai-content-generation-project

echo "Deployment completed successfully."
