while True:
    a,b,c = map(int,input().split())
    if a**2 + b**2 == c**2 :
        print("right")
    if a,b,c == 0:
    break
               
    else:
        print("wrong")
    
#1. 종료조건 위치가 잘못되었다.
#a,b,c == 0 은 튜플비교법
#2. 직각삼각형은 빗변이 가장 길어야하는데 그걸 판정안했다
#a,b,c = sorted([a,b,c]) 로 정렬,, 이러면 c가 항상 빗변이 된다
#3.,(콤마는 비교 연산자가 아니다) a,b,c==0 은 (a,b,(c==0)) 이렇게 생각함
#그래서 and논리연산자를 써야함
##수정본##
while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    a,b,c = sorted([a,b,c])
    if  a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")









       
       

    





