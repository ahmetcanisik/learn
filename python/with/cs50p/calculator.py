x = float(input("What's x? "))
y = float(input("What's y? "))

# z = round(x / y, 2) # Show last two characters.
# print(f"{z:,}") # 1,000,000

z = x / y

print(f"{z:.2f}")

"""
format string f""
float("1000000"):, => 1,000,000
float("0.66666"):.2f => 
"""
