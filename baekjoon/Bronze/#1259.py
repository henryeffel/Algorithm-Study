#뒤에서 읽어도 똑같은 수를 펠린드롬수 라고 한다
while True:
    n = list(input())
    if n == 0 :
        break
if int(n[:]) == int(n[::-1]):
    print("yes")
else:
    print("no")


    while True:
        n = input()
        if n == "0":
            break
        if n == n[::-1]:
            print("yes")
        else:
            print("no")
#하,, 리스트로 굳이 안해도 된다.. []
#파이썬의 문자열str은 리스트 처럼 인덱싱 슬라이스 다 된다..
#앞으로 리스트해서 뭐 할거있으면 문자열로 받는거 생각해라..