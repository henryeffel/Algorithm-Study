n = int(input()) #n개의 단어수 입력
words = set() #set으로 받아야 정렬,짧은것부터 됨
for i in range(n):#i 부터 n까지 새로운 단어를 받는다
    words.add(input().strip()) #공백없이의 strip

result = sorted(words, key=lambda x: (len(x),x))
#람다 쓰기 싫으면
'''def my_key(word):
        return(len(word),word)
sorted(words,key = my_key)'''

for w in result: #result 의 모든값을 w에 저장 그래서 print(w)
    print(w)

n = int(input())
words = set()
for_in range(n):
    words.add(input().strip())
restult = sorted(words, key = lambda x: (len(x),x)
for w in result:
    print(W)