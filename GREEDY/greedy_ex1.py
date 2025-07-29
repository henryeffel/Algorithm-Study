n,k = map(int,input().split()) #사용자에게 n,k를 받음
result  = 0 #연산횟수를 지정할 변수
while True: #무한반복
    target = (n//k)*k
    result += (n-target)
    n = target
    if n < k:
        break
    #n을 k로 나눴을때 나머지가 0 인 가장 가까운수로 만든다.
    #예를 들어 n = 25,k=3이면 target = 24
    #n에서 target까지 1씩 빼주는 연산을 한번에 처리
    #그리고 n 을 target값으로 갱신
    #n이 k보다 작아지면 종료
    result += 1
    n//=k
    result +=(n-1)
    print(result)
