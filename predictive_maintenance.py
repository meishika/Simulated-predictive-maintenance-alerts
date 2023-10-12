# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:55:50 2023

@author: meish
"""
import random
import time

# Simulated sensor data generation
def generate_sensor_data():
    temperature = random.uniform(60, 90)
    vibration = random.uniform(0.1, 1.0)
    pressure = random.uniform(20, 50)
    return temperature, vibration, pressure

# Predefined maintenance thresholds
TEMPERATURE_THRESHOLD = 80
VIBRATION_THRESHOLD = 0.8
PRESSURE_THRESHOLD = 40

# Simulate equipment monitoring and maintenance alerts
def simulate_equipment():
    while True:
        temperature, vibration, pressure = generate_sensor_data()
        print(f"Temperature: {temperature:.2f}°C | Vibration: {vibration:.2f} | Pressure: {pressure:.2f} psi")

        # Check for maintenance alerts
        if temperature > TEMPERATURE_THRESHOLD:
            print("Maintenance Alert: High Temperature Detected")
        if vibration > VIBRATION_THRESHOLD:
            print("Maintenance Alert: Excessive Vibration Detected")
        if pressure > PRESSURE_THRESHOLD:
            print("Maintenance Alert: High Pressure Detected")

        time.sleep(2)  # Simulate data every 2 seconds

if __name__ == "__main__":
    print("Simulating Equipment Monitoring and Maintenance Alerts...")
    try:
        simulate_equipment()
    except KeyboardInterrupt:
        print("Monitoring stopped.")

