FROM python:3.8-alpine

# Set working directory inside container
WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of backend code
ADD . .

# Expose backend port
EXPOSE 8000

# Run the app
ENTRYPOINT [ "python" ]
CMD ["app.py"]
