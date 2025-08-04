array = [1,5,3,7,2,4,6,8,9]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[i] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i]

#선택 정렬 코드 요약.
#리스트에서 맨 처음의 수를 i = min_index로 설정
#그 뒤에 두번재 인덱스[i+1],매개변수를 j 로 하고
#만약에 array[i]가 array[j]보다 크면
#min_index = j 가 된다.
#array[i],array[min_index] = array[i],array[min_index] 로 스왑한다!