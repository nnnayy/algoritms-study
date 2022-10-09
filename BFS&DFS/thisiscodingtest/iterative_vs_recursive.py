def iterative_factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i
    return result

def recursive_factorial(n): # 팩토리얼은 n이 양의 정수일 때만 유효함
    if n <= 1: # n이 0 혹은 1일 때
        return 1 # n이 1보다 클 때
    
    return n * recursive_factorial(n-1)

print(f"반복적으로 구현 : {iterative_factorial(5)}")
print(f"재귀적으로 구현 : {recursive_factorial(5)}")