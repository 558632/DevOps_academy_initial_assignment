Task C - Docker Build Fails (no space left on device)
Diagnose the CI disk full issue:
The disk capacity is limited and the Docker build spends too much of the space.
Why this occurred:
1/ usadge of large UBUNTU image
2/ command "COPY . /app" copies everything
3/ installation of nodejs using apt-get - APT cache from package installation
4/ npm install downloads many packages and temporary files.
Propose temporary and permanent fixes:
Temporary fixes:
1/ Check Docker disk usage - docker system df
2/ Remove unused containers, images, and networks - docker system prune -af
3/ Clean Docker build cache - docker builder prune -af
4/ Remove unused Docker volumes - docker volume prune -f
Permanent fixes:
1/ Use a smaller base image - FROM node:18-alpine
2/ Optimize npm installation (Faster installs, Lower disk usage, Reproducible builds) - RUN npm ci --only=production
Permanent fix:
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
CMD ["node", "index.js"]
Define monitoring measures to detect/prevent it:
1/ Monitor Docker Storage Usage - docker system df
2/ Prevent accumulation of unused resources - docker system prune -af --volumes
