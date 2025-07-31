n = int(input())
x , y  = 1 , 1
plans = input().split()
# 상하좌우 "l r u d"
dx = [0,0,-1,1]  
dy = [-1,1,0,0]
moving_type = ["L", "R", "U","D"]

for plan in plans:
    for i in range(len(moving_type)):
        if plan == moving_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue # 필드에서 나갈려고 할땐 그 단계를 스킵한다.
x,y = nx , ny
print(nx,ny)
