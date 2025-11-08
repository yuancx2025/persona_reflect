# Frontend Dockerfile for PersonaReflect
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Expose Vite dev server port
EXPOSE 5173

# Run development server
CMD ["npm", "run", "dev", "--", "--host"]
