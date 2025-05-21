import sys

s = list(sys.stdin.readline().rstrip())

biggest = ""
now = ""

for i in s:
    if i == "M":
        now += "M"
    else:
        biggest += "5"
        if now:
            for _ in range(len(now)):
                biggest += "0"
            now = ""

if len(now) >= 1:
    biggest += "1"
    for i in range(len(now) - 1):
        biggest += "1"

print(biggest)

smallest = ""
now = ""

for i in s:
    if i == "M":
        now += "M"
    else:
        if now:
            smallest += "1"
            for _ in range(len(now)-1):
                smallest += "0"
            now = ""
        smallest += "5"

if len(now) >= 1:
    smallest += "1"
    for i in range(len(now) - 1):
        smallest += "0"

print(smallest)
