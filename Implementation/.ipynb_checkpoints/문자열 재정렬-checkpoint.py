#알파벳 대문자와 숫자0~9 로만 문자열이 제공
#알파벳을 오름차순으로 정렬(sorted),그뒤에 모든숫자더함(sum)

s = input().split()
letters = [] #리스트를 하나하나 확인하며 문자열은 따로 저장
total = 0 #숫자면 다 더함

for i in s:
    if s.isalpha():
        letters.append(i)
    else:
        total += int(i)
letters.sort()
answer = "".joint(letters + str(total))

#letters = ['A', 'B', 'C', 'K', 'K']
#total = 13
#answer = ''.join(letters) + str(total)
#print(answer)   # ABCKK13
#"" = 프린트 할때 붙여서 문자열이 나왔으면 할때
#.isalpha() 라는 내장함수가 있었다.. 첨알았네

for i in s:
    if ("A" <= i <= "Z") or ("a"<= i <= "i"):
        letters.append(i)
    else:
        total += int(i) # 만약 알파벳이 아니라면
                        # 정수로 바꿔서 토탈에 더함
letters.sort()
answer = "".joint(letters + str(total))
#answer 이란 변수에 (1)원소들을 붙여서,더한숫자들을
#문자열로 바꾼다.