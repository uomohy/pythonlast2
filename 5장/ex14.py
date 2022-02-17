# 임의의 숫자를 발생시켜 사용자로부터 입력은 받아 숫자를 맞추는 게임
# 부제 : up down 게임
from random import *

cnt = 0
# 1~100까지 난수 발생시킴
num = randint(1, 100)
print("발생한 숫자: ", num)

print("1부터 100사이에서 발생한 숫자를 맞추기 시작!")
print("기회는 단 10번")

# 10번만 시도하게 하고 10번 넘으면 빠져나감
while cnt < 10:
    guess = int(input("예상하는 숫자 입력 : "))
    cnt += 1

    if guess < num:
        print("up")
    elif guess > num:
        print("down")
    elif guess == num:
        print("정답!! 시도횟수 :", cnt)
        code = input("게임을 계속 하시겠습니까? y(계속), n(중단) : ")
        # 중첩 if 문이 들어가서 게임의 지속 여부를 확인하는 코드
        if code == "n":  # 게임 종료 코드
            print("게임을 종료합니다.")
            break
        else:  # 게임을 지속하는 코드
            print("--------------------")
            # 게임을 재시작을 하기 위해서 다시 난수 발과 cnt 를 초기화를 해야함
            print("게임을 재시작합니다.")
            num = randint(1, 100)
            print("발생한 난수의 값 : ", num)
            cnt = 0

print("기회 10번이 다 소진되어 게임이 종료합니다.")

