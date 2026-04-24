# import os
# from datetime import datetime

# keywords = ["ERROR", "CRITICAL", "FAILED LOGIN"]
# try:
#     file = open("server.log", "r")
#     lines = file.readlines()
#     file.close()
# except:
#     print("File not found")
#     exit()

# filtered = []
# count = {}

# for k in keywords:
#     count[k] = 0


# for line in lines:
#     for k in keywords:
#         if k in line.upper():
#             filtered.append(line.strip())
#             count[k] += 1
#             break


# date = datetime.now().strftime("%Y-%m-%d")
# output_file = "security_alert_" + date + ".txt"

# f = open(output_file, "w")
# f.write("SECURITY ALERT REPORT\n\n")

# for line in filtered:
#     f.write(line + "\n")

# f.close()


# size = os.path.getsize(output_file)


# print("\nReport Generated:", output_file)
# print("File Size:", size, "bytes")

# print("\nSummary:")
# print("Total lines:", len(lines))
# print("Filtered lines:", len(filtered))

# print("\nError Count:")
# for k in count:
#     print(k, ":", count[k])


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