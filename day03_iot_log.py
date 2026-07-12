# Day 3: Short IoT Log Writer
from datetime import datetime
import random

# mock ESP32 temperature reading
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
mock_temp = round(random.uniform(36.5, 42.0), 1) 

with open("sensor_logs.txt", "a") as file:
    file.write(f"[{current_time}] Device: ESP32 | Temp: {mock_temp}°C\n")

print(f"Logged: [{current_time}] Temp: {mock_temp}°C")
