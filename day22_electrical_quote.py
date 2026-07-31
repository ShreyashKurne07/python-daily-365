def generate_quote(materials_cost, labor_hours, labor_rate=450):
    return round((materials_cost + (labor_hours * labor_rate)) * 1.18, 2)

projects = {"Residential Wiring": (15000, 24), "Panel Installation": (8000, 10)}
print("--- Yash Electricals Quotes ---")
for proj, (mat, hrs) in projects.items():
    print(f"{proj}: ₹{generate_quote(mat, hrs)}")
