array = [7,5,9,0,3,1,4,2,6,8]

for i in range(1,len(array)): #두번재 원소부터 하는 이유는 일단 왼쪽으로 정렬 해야하기때문
    for j in range(i,0,-1): #인덱스 i부터 첫번재 원소까지 1씩감소하는 문법
        if array[j] < array[j-1]: #한깍씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기보다 작은데이터 만나면 그 자리에서
            break
print(array)