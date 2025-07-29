a , b = input().split() #두 수를 문자열로 받아들인다. 리스트화 하기 쉽게
reverse_a = int(a[::-1])#바로 리버스 [인덱싱 ::-1]은 역순으로 출력
reverse_b = int(b[::-1])
print(max(reverse_a, reverse_b))#max()함수로 최댓값 활용