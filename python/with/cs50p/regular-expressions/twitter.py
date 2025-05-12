import re

user: str | None = None
url = input("Twitter Profile (Enter username or profile url): ").strip()

if matches := re.search(
    r"^(?:(?:https?://)?(?:www\.)?(?:twitter|x)\.com\/)?(@?[a-zA-Z][\w]+)",
    url.strip(),
    re.IGNORECASE,
):
    # (www\.) = first group.
    # (.+)    = second group

    # (?:www\.) = this is not a capturing group. so then (.+) is now first group.
    username = matches.group(1).replace("@", "")
    if len(username) <= 15 and len(username) >= 4:
        user = username

if user is not None and isinstance(user, str):
    print(f"Username is {username}")
else:
    print("This is not a twitter user!")


"""
# removeprefix like replace("https://twitter.com", "")
username = url.removeprefix("https://twitter.com/")
"""
