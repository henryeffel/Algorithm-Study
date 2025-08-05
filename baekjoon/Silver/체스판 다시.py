n,m = map(int(input().split()))
#보드 데이터 입력받기
board = []
b,w = input().split()
for _ in range(n):
    board.append(input().split())
board = [input().strip() for _ in range(n)]

min_count = 64

for row in range(n-7):
    for col in range(m-7):
        count1 = 0 #0,0이 w
        coutn2 = 0 #0,0이 b
        for i in range(8):
            for j in range(8):
                current = board[row + i][col + j]
                if (i+j)%2 == 0:
                    if current != "w":
                        count1 += 1
                    if current != "b":
                        count2 += 1
                else :
                    if current != "b":
                        count1 += 1
                    if current != "w":
                        count2 += 1
min_count = min(min_count,count1,count2)
print(min_count)