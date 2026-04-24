import re

pattern = re.compile(r"ERROR|CRITICAL|FAILED LOGIN", re.IGNORECASE)

filtered = []
count = {"ERROR": 0, "CRITICAL": 0, "FAILED LOGIN": 0}

file = open("server.log", "r")
lines = file.readlines()
file.close()

for line in lines:
    match = pattern.search(line)
    if match:
        word = match.group().upper()
        filtered.append(line.strip())
        count[word] += 1

print("Filtered Lines:")
for line in filtered:
    print(line)

print("\nCount:")
for k in count:
    print(k, ":", count[k])
