from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n+1))
result = [] #result 에 리스트 저장

while queue: #어지간하면 큐 문제엔 while을 쓰는듯
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")