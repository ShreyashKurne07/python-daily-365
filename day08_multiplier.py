# Day 8: Multiplication Table Generator

user = int(input("Enter a number for its multiplication table: "))
print(f"\n--- Table for {user} ---")
for i in range(1, 11):
    result = user * i
    print(f"{user} x {i} = {result}")
