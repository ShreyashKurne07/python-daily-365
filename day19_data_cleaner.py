import json

raw_logs = '[{"status": 200, "latency": 120}, {"status": 500, "latency": 450}, {"status": 200, "latency": 95}]'
data = json.loads(raw_logs)

valid_latencies = [entry["latency"] for entry in data if entry["status"] == 200]
avg_latency = sum(valid_latencies) / len(valid_latencies)

print(f"Total Requests: {len(data)}")
print(f"Successful Requests: {len(valid_latencies)}")
print(f"Average Latency (200 OK): {round(avg_latency, 2)}ms")
