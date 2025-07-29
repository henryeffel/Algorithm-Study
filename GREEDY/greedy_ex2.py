#곱하기 혹은 더하기:
#문자열 s를 받은다음, 0부터9까지의 정수 요소를 다 더하거나 곱해서
#가장 큰 값을 만드는 greedy문제입니다.
#중요한점은 0,1 이면 먼저 더하는게 이득입니다.

s = input()

#첫번째 문자를 숫자로 변경하여 대입
result = int(s[0])

for i in range(1,len(s)):
    #두 수 중에서 하나라도 "0" 혹은 1인경우, 곱하기보다 더하기
    num = int(s[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num

data = input()

result = int(data[0]) #첫번째 문자열을 숫자로 변경.(두 수의 합or곱 결정권)

for i in range(1,len(data)):#입력받은 문자열 그룹의 대한 정의
    #문자열 안의 1수랑 2수 가 1이하일때 더하기
    #1수는 result로 정했고, 2수를 정해야한다 -> 변수설정
    numm = int(data[i])
    if numm <= 1 or result <=1:
        result += num
    else:
        result *= num
    print(result)
