n = int(input().split()) #흔한 n 받기
points = [] #리스트로 받기
for _ in range(n):
    x,y = map(int,input().split())#좌표니까 xy값 받기
    points.append((x,y))#리스트에 추가

points.sort(key = lambda point:(point[0],point[1])) #람다함수로 정렬

for x,y in points:
    print(x,y)