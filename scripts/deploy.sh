#!/bin/bash

set -e

# echo "======================================="
echo " Starting SecureAuth Deployment..."
# echo "======================================="

cd /home/ubuntu/secure-authhentication-sysytem

echo "Rebuilding containers..."
docker compose up -d --build

echo "Cleaning unused Docker images..."
docker image prune -f

echo "Running containers:"
docker ps

echo " Deployment Successful!"

'''
#!/bin/bash

echo "🚀 Starting deployment..."

git pull origin main

docker compose down

docker compose up -d --build

docker image prune -f

echo "✅ Deployment completed successfully."
'''