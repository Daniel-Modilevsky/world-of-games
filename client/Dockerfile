# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install Python and necessary build dependencies
RUN apk add --no-cache python3 make g++

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY ../client .

# Build the React app
RUN npm run build

# Expose the container port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
