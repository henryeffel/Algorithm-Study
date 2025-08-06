from collections import deque

n = int(input())

program = deque(range(1,n+1))
push (int(x)) = program.append(int(x))
pop = 
####### 
#네.. 정답은 fof _ in range(n) 반복문에서 cmd = input().split() 이라는 명령변수를 만들
#고 . if, elif로 무한 반복 합니다
#그리고 pop은 그냥 remove를 잊고, popleft를 사용합시다..
from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1])) ##정수 변환 확인##
    elif cmd[0] == "pop":
        print(queue.popleft() if queue else -1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)
    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)

##################### 시간초과###################

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()
result = []

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop":
        result.append(str(queue.popleft()) if queue else "-1")
    elif cmd[0] == "size":
        result.append(str(len(queue)))
    elif cmd[0] == "empty":
        result.append("1" if not queue else "0")
    elif cmd[0] == "front":
        result.append(str(queue[0]) if queue else "-1")
    elif cmd[0] == "back":
        result.append(str(queue[-1]) if queue else "-1")

print('\n'.join(result))

#sys readline 쓰고.. 프린트할때 \n이랑 마지막에 '\n'.join(...)으로 한꺼번에 출력하면 더 빠름!
## 저거 할려고 result = [] 리스트 만듦!
