def parse_hardware_specs(text):
    keywords = ["sensor", "esp32", "relay", "actuator"]
    return [kw for kw in keywords if kw in text.lower()]

doc = "The monitoring unit uses an ESP32 connected to a 5V relay and a temp sensor."
print(f"Detected Hardware Components: {parse_hardware_specs(doc)}")
