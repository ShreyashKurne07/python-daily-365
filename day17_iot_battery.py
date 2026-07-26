def estimate_battery_life(capacity_mah, active_ma, sleep_ma, active_hours_per_day):
    sleep_hours = 24 - active_hours_per_day
    daily_consumption = (active_ma * active_hours_per_day) + (sleep_ma * sleep_hours)
    return round(capacity_mah / daily_consumption, 1)

battery = 3000
active_draw = 240
sleep_draw = 0.15
active_time = 0.5

life_span = estimate_battery_life(battery, active_draw, sleep_draw, active_time)

print("--- Edge Node Power Profile ---")
print(f"Device: ESP32 | Battery: {battery}mAh")
print(f"Estimated Lifespan: {life_span} days")
