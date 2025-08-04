def quick_sort(array):
    if len(array) <=1:
        return array #원소가 1개 이하면 그대로 리턴(정렬끝)
    pivot = array[0] #첫번째 원소를 피벗으로 선택
    tail = array[1:] #피벗을 제외한 리스트 [0]은 피벗

    left_side = [x for x in tail if x <= pivot ] #피벗보다 작거나
    right_side = [x for x in tail if x > pivot] #피벗보다 큰 값

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)