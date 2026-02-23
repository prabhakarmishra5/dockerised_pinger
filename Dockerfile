FROM python:3.12-slim
# Install ping utility
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY ping_random_ip_address_v2.py .
RUN mkdir -p /app/logs
CMD ["python", "ping_random_ip_address_v2.py"]