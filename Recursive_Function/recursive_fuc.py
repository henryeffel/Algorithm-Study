#재귀함수
#먼저 팩토리얼을 반복문
def facto(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

#재귀적으로 효현한 팩토리얼
def factos_recursive(n):
    if n <= 1: #n이 1 이하인경우 1을 반환
        return 1
    #n! = n*(n-1)!*
    return n * factos_recursive(n-1)
print("반복적으로 구현:", facto(5))
print("재귀적으로 구현:", factos_recursive(5))

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return (b, a%b)
print(gcd(192,162))