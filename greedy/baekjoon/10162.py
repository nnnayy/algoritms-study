import sys
input = sys.stdin.readline

# 300 60 10

t = int(input())

time = [300, 60, 10]

three = 0
six = 0
ten = 0

for second in time:
    if second == 300:
        three += (t//second)
        t %= second
    if second == 60:
        six += (t//second)
        t %= second
    if second == 10:
        ten += (t//second)
        t %= second

print(three, six, ten)