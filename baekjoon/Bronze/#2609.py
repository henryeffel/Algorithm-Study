#최대공약수,, 최소공배수 구하기..
n = input().split()
for i in range(1,n):
    m = int(n[0]) % i == 0 and int(n[1]) % i == 0
    M = int(n[0]) // i and int(n[1]) // 1
print(m)
print(M)
#############
a,b = map(int,input().split())

gcd = 1 #곱하기의 토탈은 1로 하더라
for i in range(min(a,b),0,-1): #a,b의 최솟값을 0까지 1씩 빼면서 나열
    if a % i == 0 and b % i == 0:
        gcd = i
        break
lcm = a*b
for i in range(max(a,), a*b+1):
    if i % a ==0 and b % i == 0:
        lcm = i
        break

print(gcd)
print(lcm) 

##########################
#네 저렇게 하니까 시간초과가 나오네요..쩝..
#울며 겨자먹기로 유클리드 호제법을 합니다..
a,b = map(int,input().split())
def gcd(x,y):
    while y: # y 값이 0이 될때까지 나누기를 한답니다
        x,y = y, x%y
    return x
g = gcd(a,b)
lcm = a*b //g

print(g)
print(lcm)


    
              