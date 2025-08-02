#!/bin/bash
docker stop agent-hub || true
docker rm agent-hub || true
cd /home/ec2-user/app
docker run -d --name agent-hub -p 8000:8000 -e GITHUB_TOKEN="${GITHUB_TOKEN}" agent-hub
