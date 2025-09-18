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

# Install serve globally
RUN npm install -g serve

# Verify build output
RUN ls -la dist/

# Expose port
EXPOSE $PORT

# Start production server with explicit port and host handling
CMD sh -c "echo 'Starting server on host 0.0.0.0 port ${PORT:-3000}' && serve -s dist -l ${PORT:-3000} -H 0.0.0.0"
