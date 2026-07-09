import sys
sys.stdout.reconfigure(encoding="utf-8")
# Day 1: Basic SIP Compound Interest Calculator

def calculate_sip_return(monthly_investment, annual_rate, years):
    # Convert annual rate to a decimal monthly rate
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    
    # Future Value of SIP formula
    future_value = monthly_investment * (((1 + monthly_rate)**months - 1) / monthly_rate) * (1 + monthly_rate)
    return round(future_value, 2)

# Your actual financial parameters
my_investment = 10000 
expected_return = 12 # 12% estimated annual return for Nifty 50
time_horizon = 10 # 10 years

total_value = calculate_sip_return(my_investment, expected_return, time_horizon)
total_invested = my_investment * 12 * time_horizon
wealth_gained = total_value - total_invested

print(f"--- SIP Projection for {time_horizon} Years ---")
print(f"Total Invested: ₹{total_invested:,.2f}")
print(f"Wealth Gained: ₹{wealth_gained:,.2f}")
print(f"Estimated Total Value: ₹{total_value:,.2f}")
