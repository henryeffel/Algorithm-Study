#두개의 배열 a = [] b = [] n개의 원소개수
# a원소,b원소 스왑 a배열의 합이 최대가 되게

n,k = map(int,(input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
# a리스트 오림차순 -> b리스트 네름차순 정렬
a.sort()
b.sort(revers=True) # reverse=True 는 내림차순 정렬이닷

#첫번째 인덱스 부터 확인하여 k번 비교한다
for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))