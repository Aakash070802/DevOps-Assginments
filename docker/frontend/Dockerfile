FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy package files first
COPY package*.json ./

# Install node dependencies
RUN npm install

# Copy rest of frontend code
ADD . .

# Expose frontend port
EXPOSE 3000

# Start frontend app
ENTRYPOINT [ "npm" ]
CMD ["start"]
