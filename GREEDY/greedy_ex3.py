n = int(input())
fear = list(map(int,input().split()))
fear.sort() #그룹을 짜기위해서 공포도 의 수를 오름차순 정렬

count = 0 #현재 그룹에 포함된 모험가의 수
result = 0 #총 그룹의 수

for i in fear:
    count += 1 # 현재 그룹에 모험가를 포함시키면서도 조건문
    if count >= i: #모험가 수 가 공포도보다 크거나 같으면
        result += 1 #그룹 출발해서 결과에 +1
        count = 0 #다음 공포도를 위해 리셋 
print(result)   