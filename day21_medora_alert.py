def medora_alert_system(bpm, spo2):
    if bpm < 50 or bpm > 120 or spo2 < 90:
        return f"ALERT: Abnormal Vitals - BPM: {bpm}, SpO2: {spo2}%"
    return "Status: Stable"

patient_readings = [{"bpm": 72, "spo2": 98}, {"bpm": 130, "spo2": 88}]
for reading in patient_readings:
    print(medora_alert_system(reading["bpm"], reading["spo2"]))
