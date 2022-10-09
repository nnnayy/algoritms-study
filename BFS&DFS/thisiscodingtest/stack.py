stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop() # 7 삭제

stack.append(1)
stack.append(4)

stack.pop() # 4 삭제

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력