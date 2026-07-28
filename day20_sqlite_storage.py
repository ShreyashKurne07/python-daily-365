import sqlite3

conn = sqlite3.connect("metrics.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS system_logs (id INTEGER PRIMARY KEY, service TEXT, cpu_usage REAL)")
cursor.execute("INSERT INTO system_logs (service, cpu_usage) VALUES ('ml-inference', 74.5)")
cursor.execute("INSERT INTO system_logs (service, cpu_usage) VALUES ('data-pipeline', 32.1)")
conn.commit()

cursor.execute("SELECT * FROM system_logs WHERE cpu_usage > 50")
rows = cursor.fetchall()

for row in rows:
    print(f"High CPU Warning -> Service: {row[1]} | CPU: {row[2]}%")

conn.close()
