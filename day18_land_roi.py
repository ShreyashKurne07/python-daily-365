def calculate_land_value(base_investment, annual_growth_rate, years):
    return round(base_investment * ((1 + annual_growth_rate) ** years), 2)

corridors = {
    "Khed Shivapur": 0.12,
    "Saswad": 0.14,
    "Uruli Kanchan": 0.10
}

investment = 1500000
horizon = 5

print(f"--- 5-Year Land Investment Projection (₹{investment:,.2f}) ---")
for location, rate in corridors.items():
    projected = calculate_land_value(investment, rate, horizon)
    profit = projected - investment
    print(f"📍 {location}:")
    print(f"   Proj. Value: ₹{projected:,.2f} | Profit: ₹{profit:,.2f}")
