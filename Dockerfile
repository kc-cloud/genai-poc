# Use a lightweight Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install basic OS packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY inference-server.py .
COPY hf_model ./hf_model

# Expose port
EXPOSE 8000

# Start the server
CMD ["uvicorn", "inference-server:app", "--host", "0.0.0.0", "--port", "8000"]
