#n 장에서 3장을 고른다
n,m = int(input().split())
cards = list(map(int,input().split())) #카드들을 리스트에 저장

result = 0 #3장의 카드 합 중에서 가장 큰 값을 저장할 값

#3중 for문으로 카드 다 탐색하기

for i in range(n):
    for j in range(i+1,n): #j 는 i보다 커야 하브로 +1 부터 범위
        for k in range(j+1,n):#also k should be 커야한다 j보다 +1
            total = cards[i] + cards[j] + cards[k] #블랙잭처럼 카드리스트요소들끼리 더해
if total <= m and total > result: #근데 그 더한값이 m 이하여야하고
    result = total
print(result)

n,m = map(int,input().split())
cards = list(map(int,input().split()))
result = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            total = cards[i]+cards[j]+cards[k]
            if total <= m and total > result:
                result = total
print(result)

#부르트 포스,, 3중 반복문으로 탐색..