from collections import deque

#1. 입력 받기
n,m = map(int,input().split())
map = []
for _ in range(n):
    map.append(list(map(int,input().strip())))
#4방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y): # 최단 거리 이므로, bfs 실행
    queue = deque() #탐색할 좌표들의 리스트
    queue.append((x,y))  #큐에 (x,y) 추가?
    while queue: #큐가 빌때까지 계속
        x,y = queue.popleft() #선입선출 가장 앞에있는 원소를 뺀다
        for i in range(4): #dx dy 상하좌우의 갯수 4
            nx = x + dx[i] # 움직인 좌표 = 원래좌쵸 + dx,dy 원소들 더함
            my = x + dy[i]
            #queue 에서 xy를 꺼냄, 상하좌우 nxny구해, 벽 확인해(0 or 1)
            #1이면 큐에 추가 +1 해서 저장, 큐가 빌때가지 반복
            if nx < 0 or nx >= n or my < 0 or my >= m:
                continue #범위 넘어가면 re
            if map[nx][my] == 0:
                continue #벽을 만나면 re
            if map[nx][my] == 1:
                map[nx][my]= map[x][y] + 1
                queue.append((nx,my)) #누적 거리를 계속 저장
    return map[n-1][m-1] #마지막 도착 좌표 (인덱스 개념 0부터 시작이라)
print(bfs(0,0))
