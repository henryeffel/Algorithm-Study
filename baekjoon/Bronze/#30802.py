#30802 // 웰컴키트

n = int(input())
sizes = map(int,input().split()) # list 호러쇼//
t ,p = map(int,input().split())
#결국 티셔츠_묶음 을 구해야합니다. 사이즈들의합+t-1을 t로 나누어요, 그리고 더해
tshirts_bundle = sum((n+t-1)//t for _ in sizes)

pen_bundles = n//p #몫
pen_single = n%p #나머지

print(tshirts_bundle)
print(pen_bundles,pen_single)

# 입력 예시
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠 묶음 계산
tshirt_bundles = sum((size + T - 1) // T for size in sizes)

# 펜 묶음 계산
pen_bundles = N // P
pen_singles = N % P

print(tshirt_bundles)
print(pen_bundles, pen_singles)

##list까먹지 말자
