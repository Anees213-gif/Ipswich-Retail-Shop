# Use Node.js 18 Alpine image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Install serve globally for static hosting
RUN npm install -g serve

# Verify build output
RUN ls -la dist/

# Expose port
EXPOSE $PORT

# Start production server using npm script
CMD ["sh", "-c", "echo 'Starting React app on port ${PORT:-3000}' && npm run start:prod"]
