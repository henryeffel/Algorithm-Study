#주어진 수 n개중에서 소수가 몇 개인지 찾아서 출력하시오
#첫줄에 수의 개수 n이 주어진다, n은 100이하이다 다음으로 n개의수가 주어진다.
#주어진 수들 중 소수의 개수를 출력한다.
#ex) 4 -> 1,3,5,7  --> 3 출력..

n = int(input())
sosu = list(map(int,input().split()))
result = 0
for i in range(1,n-1):
    if sosu[i] % i == 0 and sosu[i] > 1  :
        result += 1
print(result)


def prime(n):
    if n < 2:
        return False
    for i in range(2,n-1):
        if n % 1 == 0:
            return False
    return True
n = int(input())
sosu = list(map(int,input().split()))
count = 0
for i in sosu:
    if prime(i):
        count += 1

print(count)


def primee(n) :
    if n < 2:
        return False #소수의 조건중 1이 아닌경우
    for i in range(2,n): #2부터 n-1 까지 다 다눠본다
        if n%i == 0:
            return False
    retrun True

for i in sosu:
    if prime(i) :
        count+=1