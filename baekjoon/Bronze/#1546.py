n = int(input())
score = list(map(int,input().split()))
m = max(score)
for i in range(1,n):
    new_score = sum(score[i]//m*100)
new_ave = sum(new_score) // n
print(new_ave)

#4,5 줄에서 에러가 났는디
new_score = [i / m * 100 for i in score] #원래 점수 원소들을 i
# or 원래 4,5줄에서 할거엿으면 이렇게 했어야함
total = 0
for i in range(n): # range 범위가 인덱스 0부터 해야해서
    total += score[i] / m * 100
    new_ave = total / n #sum 안쓰는 이유는 이미 더한값이기 때문