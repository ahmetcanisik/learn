# up is user prompt
up = input("Greeting: ").strip().lower()

if up.startswith("hello"):
    print("$0")
elif up.startswith("h"):
    print("$20")
else:
    print("$100")
