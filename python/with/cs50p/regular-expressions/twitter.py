import re
url = input("Twitter URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url.strip())
print(f"Username is {username}")


"""
# removeprefix like replace("https://twitter.com", "")
username = url.removeprefix("https://twitter.com/")
"""