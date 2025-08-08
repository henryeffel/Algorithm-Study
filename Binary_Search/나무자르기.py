n,m = map(int,input().split())
dduck = list(map(int,input().split()))

left = 0
right = max(dduck)
result = 0

while left <= right:
    mid = (left + right) // 2 #여기까지 입력값,떡리스트,결과리스트 미드값
    total = sum((d-mid) for d in dduck if d > mid) #떡의 총 합 계싼하기
    if total >= m:
        result = mid
        left = mid + 1
    else: #total < m 
        right = mid -1

print(result)
