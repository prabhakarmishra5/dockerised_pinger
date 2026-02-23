import logging
import random
import subprocess
import time
import os
from datetime import datetime

# Setup logging: to file and stdout
os.makedirs('/app/logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/ping.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

files = ['north.txt', 'east.txt', 'west.txt', 'south.txt']

while True:
    logger.info("Starting ping cycle...")
    
    for file_path in files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    ips = [line.strip() for line in f.readlines() if line.strip()]
                if ips:
                    ip = random.choice(ips)
                    # Cross-platform ping: Linux/Mac (-c 1 -W 2), Windows (-n 1 -w 2000)
                    if os.name == 'nt':  # Windows
                        cmd = ['ping', '-n', '1', '-w', '2000', ip]
                    else:
                        cmd = ['ping', '-c', '1', '-W', '2', ip]
                    
                    response = subprocess.call(cmd, 
                                             stdout=subprocess.DEVNULL, 
                                             stderr=subprocess.DEVNULL)
                    status = "UP" if response == 0 else "DOWN"
                    logger.info(f"{file_path}: Random IP {ip} - {status}")
                else:
                    logger.warning(f"{file_path}: No valid IPs found")
            except Exception as e:
                logger.error(f"{file_path}: Error reading file or pinging - {e}")
        else:
            logger.warning(f"{file_path}: File not found")
    
    logger.info("Ping cycle complete. Sleeping 30 seconds...")
    time.sleep(30)
