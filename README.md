Step 1: Create a docker file in same dir: 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Name [Dockerfile]
FROM python:3.12-slim
# Install ping utility
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY ping_random_ip_address_v2.py .
RUN mkdir -p /app/logs
CMD ["python", "ping_random_ip_address_v2.py"]
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Step 2  : Build the image

docker build -t ping_random_ip_address_v2 .

Step 2_1: Verify build success

docker images | findstr ping_random_ip_address_v2

Step 3: Create the dir

mkdir "C:\Users\prabh\logs"
mkdir "C:\Users\prabh\Downloads"  # If missing, but Downloads usually exists

Step 3_1: Stop and remove pinger before you start (if any previous events)
docker stop pinger
docker rm pinger

Step 4: Now run (updated for your file names: north.txt, etc.):
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Multi-line
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
docker run -d --name pinger --restart unless-stopped ^
  -v "C:\Users\prabh\Downloads\north.txt:/app/north.txt" ^
  -v "C:\Users\prabh\Downloads\east.txt:/app/east.txt" ^
  -v "C:\Users\prabh\Downloads\west.txt:/app/west.txt" ^
  -v "C:\Users\prabh\Downloads\south.txt:/app/south.txt" ^
  -v "C:\Users\prabh\logs:/app/logs" ^
  ping-script
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
​Single line
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
docker run -d --name pinger --restart unless-stopped -v "C:\Users\prabh\Downloads\north.txt:/app/north.txt" -v "C:\Users\prabh\Downloads\east.txt:/app/east.txt" -v "C:\Users\prabh\Downloads\west.txt:/app/west.txt" -v "C:\Users\prabh\Downloads\south.txt:/app/south.txt" -v "C:\Users\prabh\logs:/app/logs" ping_random_ip_address_v2
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Check Info
docker ps
docker logs pinger

Kill pinger
docker stop pinger
docker rm pinger
