#첫재줄엔 온라인 저지 회원의 수 n 이 주어진다
#두번재 줄부터 나이와 이름이 주어진다
#출력은 나이순 (sort?) 그리고  if 나이가 같으면, 먼저 입력된 순서대로

n = int(input())
members = []
#입력을 받아야지ㅣㅣㅣ 
for _ in range(n):
    age,name = input().split()
    members.append(int(age),input()) # age는 숫자니까 변형
members.sort()
for member in members:
    print(members[0],members[1])

#lambda 함수도 있는데요..
#members.sort(key=lambda x:x[0]) 나이 기준으로 만 정렬

n = int(input())
members = []
for _ in range(n):
    age,name = input().split()
    members.append(int(age),input())
members.sort(key=lambda x: x[0])
for member in mebers:
    print(members[0],members[1])
























    n = int(input()) # n 받기
    members = []
    for _ in range(n):
        age,name = input().split()
        members.append((int(age),name)) #name 이랑 age를 튜플 처리해서 괄호?
    members.sort(key=lambda x: x[0])
    members.sort()
    for member in members:
        print(member[0],member[1])