#!/bin/bash

set -e

echo "======================================="
echo "🚀 Starting SecureAuth Deployment..."
echo "======================================="

cd /home/ubuntu/secure-authhentication-sysytem

echo "📝 Updating Nginx configuration..."
sudo cp deployment/nginx/secureauth.conf /etc/nginx/sites-available/secureauth
sudo ln -sf /etc/nginx/sites-available/secureauth /etc/nginx/sites-enabled/secureauth

echo "🔍 Testing Nginx..."
sudo nginx -t

echo "🔄 Reloading Nginx..."
sudo systemctl reload nginx

echo "🐳 Rebuilding Docker containers..."
docker compose down --remove-orphans
docker compose up -d --build

echo "🧹 Cleaning Docker images..."
docker image prune -f

echo "📦 Running containers..."
docker ps

echo "======================================="
echo "✅ Deployment Successful!"
echo "======================================="