n = int(input()) # 수 받기
nums = [] #리스트로 받기
for _ in range(n): # n받은만큼 계속 반복 입력하기
    nums.append(int(input())) #입력받은수들을 리스트에 저장
nums.sort() #리스트들을 솔트 정렬하기
for num in range(nums): #리스트 범위에서 ~ 요소들을 출력..
    print(num)

    import sys
input = sys.stdin.readline #인풋 느릴까봐

n = int(input()) #수 받기
nums = [] #리스트로 만들기
for _ in range(n): #n까지 범위안에서 반복
    nums.append(int(input())) #append로 리스트에 값 저장
    
nums.sort()#정렬하기
for num in range(nums): #nums 범위에서 num 출력하기 #range() 은 리스트 쓰면 안돼!
    print(num)

#sort()와 sorted() 차이는 전자는 원본이 바뀌고 후자는 아예 새로운게 나온다
nuumbers = [ 1,2,3,4]
result = sorted(nuumbers) #--> 이렇게 해도 nuumbers와 sorted된 버전 둘다 유지