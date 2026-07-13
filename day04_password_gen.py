# Day 4: 5-Line Password Generator
import random
import string

chars = string.ascii_letters + string.digits + "!@#$%"
password = ''.join(random.choice(chars) for i in range(12))

print(f"Generated Password: {password}")
