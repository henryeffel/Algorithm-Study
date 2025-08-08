#Binary_Search : 이진탐색이라고 부른다. 시작과 끝지점을 정하고 가운데값을 정한후 앞뒤로 구분
#해가면서 값을 찾는다. 뭔가 퀵정렬 pivot을 활용한 느낌?

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        #찾은경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid +1
    return None

n, target = list(map(int,input().split()))  
array = list(map(int,input().split()))   

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)