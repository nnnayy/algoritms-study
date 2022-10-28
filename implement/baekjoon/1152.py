import sys
input = sys.stdin.readline

count = 0

str = input().split(" ")

for i in str:
    count = len(str)
    
    if i == '':
        count -= 1
        str = str[1:]

    if i == '\n':
        count -= 1
        str = str[:-1]

print(count)