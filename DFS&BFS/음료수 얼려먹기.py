#1. 입력 받기
n,m = map(int,input().split())
ice_map = []
for _ in range(n):
    ice_map.append(list(map(int,input().strip())))
#2. DFS 함수정의
def dfs(x,y): #함수를 선언한다 (x,y)는 현제 위치
    if x < 0 or x >= n or y < 0 or y >= m :
        return False   #벽치기 or 벽 넘기 방지
    if ice_map[x][y] == 0:
        #방문처리 -> 이 위치가 "0" 아직 방문하기 전 이라면
        ice_map[x][y] = 1
        #이제 이 자리는 방문완료! 했다고 1로 바뀜, 이걸안하면 중복 도르마무 생김
        dfs(x-1,y)#위
        dfs(x+1,y)#아래
        dfs(x,y-1)#왼쪽
        dfs(x,y-1)#오른쪽 // 현재 칸의 네 방향 한칸씩 이동하면서 0을 찾는다! (재귀)
        return True #처음 발견된 0 인거라면 트루 를 반환
    return False
#모든 아이스크림 갯수 세기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1
print(result)
