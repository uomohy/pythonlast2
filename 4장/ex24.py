# 숫자 추측 게임을 만들기
# random 모듈을 사용
from random import *
# randint(a, b) 함수는 a 부터 b 까지의 사이에 있는 정수를 반환해주는 함수
# 1~100까지 임의의 수(난수)를 발생시키는 코드
rand_num = randint(1, 100)
print("발생한 난수 : ", rand_num)
user_num = int(input("숫자를 맞춰보세요.(1~100) : "))
# count 변수 생성
cnt = 0
# 무한 루프
while True:
    if user_num == rand_num:
        cnt += 1
        print("정답입니다.게임을 종료합니다.(시도횟수 : ", cnt, ")")
        break
    elif user_num > rand_num:
        print("입력한 숫자가 큽니다.")
        # 파이썬에서는 ++, -- 이런 증감 연산자는 없음
        # 복합대입 연산자를 사용하도록 하기
        cnt += 1
        print("시도 횟수 : ", cnt)
    else:
        print("입력한 숫자가 작습니다.")
        cnt += 1
        print("시도 횟수 : ", cnt)
    user_num = int(input("다시 입력해주세요 : "))

