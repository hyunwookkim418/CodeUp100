# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

while 1:
    n = input()
    if n != 'q':
        print(n)
    elif n == 'q':
        print(n)
        break