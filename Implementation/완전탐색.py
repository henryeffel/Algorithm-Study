#이 문제는 가능한 모든 시각의 경우를 하나씩 세서 풀수있습니다.
#하루는 86400초이므로, "단순히 1씩 증가시켜서 3이 들어간걸 찾으면 됩니다."
#옛날 오븐 타이머 문제처럼 시간 문제가 나오면 대체로 다 더하면 되더리..

h = int(input())

count = 0
for i in range(h+1): #시간
    for j in range(60):#분
        for k in range(60):#초
            #매 시각 안에 "3"이 포함되었다면 카운트
            if "3" in str(i) + str(j) + str(k):
                count += 1
print(count)