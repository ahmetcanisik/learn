proxies = []

with open("proxies.txt", "r") as file:
    for line in file:
        proxies.append(line.rstrip())

for proxy in sorted(proxies):
    print(f"testing proxy.. {proxy}")
