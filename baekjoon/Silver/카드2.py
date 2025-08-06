#제가 생각한것은.. 반복문으로 카드를 버리고 스왑하는 식으로 한무반복하는걸 생각했는데요..
#그럼 시간복잡도가 초과된데서 deque + popleft 기법을 쓰라고 한답니다..
n = int(input())
cards = [int(input()) for _ in range(1,n)]

from collections import deque

n = int(input())
cards = deque(range(1,n+1))

while len(cards) > 1:
    cards.popleft() #첫번째 카드 삭제 -> 내가 생각했던 remove
    cards.append(cards.popleft()) #-> 내가 생각했던 수왑,,

print(cards[0]) 