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

# Expose port (Railway will set the PORT environment variable)
EXPOSE $PORT

# Start production server
CMD ["sh", "-c", "serve -s dist -p $PORT"]
