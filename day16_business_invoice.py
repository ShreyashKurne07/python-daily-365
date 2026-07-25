# Day 16: Simple Business Invoice Generator

def generate_invoice(company_name, amount, tax_rate):
    tax = amount * tax_rate
    total = amount + tax
    
    print(f"--- {company_name} ---")
    print(f"Base Amount: ₹{amount:,.2f}")
    print(f"Tax ({tax_rate * 100}%): ₹{tax:,.2f}")
    print(f"Total Due: ₹{total:,.2f}")
    print("------------------------")

generate_invoice("Yash Electricals", 12500, 0.18)
