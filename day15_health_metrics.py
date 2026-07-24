# Day 15: Basic BMI Calculator

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

my_weight = 65
my_height = 163
my_bmi = calculate_bmi(my_weight, my_height)

print("--- Health Metrics ---")
print(f"Metrics: {my_weight}kg, {my_height}cm")
print(f"Calculated BMI: {my_bmi}")
