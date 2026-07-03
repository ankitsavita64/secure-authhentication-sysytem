#!/bin/bash

set -e

echo "======================================="
echo "🚀 Starting SecureAuth Deployment..."
echo "======================================="

cd /home/ubuntu/secure-authhentication-sysytem

echo "📥 Pulling latest code..."
git pull origin main

echo "🐳 Rebuilding containers..."
docker compose up -d --build

echo "🧹 Cleaning unused Docker images..."
docker image prune -f

echo "📋 Running containers:"
docker ps

echo "======================================="
echo "✅ Deployment Successful!"
echo "======================================="