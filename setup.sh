#!/bin/bash

# Check if docker-compose-template.yml exists
if [ ! -f docker-compose-template.yml ]; then
    echo "Error: docker-compose-template.yml does not exist."
    exit 1
fi

# Ask for the hostname and port
read -p "Enter the desired hostname (e.g., myapp): " HOSTNAME
read -p "Enter the desired port (e.g., 8000): " PORT

# Generate actual docker-compose.yml from the template
echo "Generating docker-compose.yml from template..."
sed "s/{{PORT}}/$PORT/" < docker-compose-template.yml > docker-compose.yml

# Check the generated content
echo "Generated docker-compose.yml content:"
cat docker-compose.yml

# Check if docker-compose.yml was created successfully
if [ ! -f docker-compose.yml ]; then
    echo "Error: docker-compose.yml was not generated."
    exit 1
fi

# Replace placeholders in nginx configuration
echo "Updating nginx configuration..."
sed -i "s/{{HOSTNAME}}/$HOSTNAME/g" nginx/default.conf

# Start the Docker Compose setup
docker-compose up -d
