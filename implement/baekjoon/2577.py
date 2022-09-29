import sys
input = sys.stdin.readline

data = [int(input()) for _ in range(3)]
numbers = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

sum = 1

for i in range(3):
    sum *= data[i]

    if '0' in str(sum):
        numbers['0'] += 1
    if '1' in str(sum):
        numbers['1'] += 1
    if '2' in str(sum):
        numbers['2'] += 1
    if '3' in str(sum):
        numbers['3'] += 1
    if '4' in str(sum):
        numbers['4'] += 1
    if '5' in str(sum):
        numbers['5'] += 1
    if '6' in str(sum):
        numbers['6'] += 1
    if '7' in str(sum):
        numbers['7'] += 1
    if '8' in str(sum):
        numbers['8'] += 1
    if '9' in str(sum):
        numbers['9'] += 1


print(numbers['0'])
print(numbers['1'])
print(numbers['2'])
print(numbers['3'])
print(numbers['4'])
print(numbers['5'])
print(numbers['6'])
print(numbers['7'])
print(numbers['8'])
print(numbers['9'])
