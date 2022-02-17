# 플래그 변수를 사용한 무한 루프 문제
# 1.증속, 2.감속, 3.중지 를 출력하고 사용자의 입력을 1, 2, 3 받아서
# 증속을 하면 속도를 10씩 증가하고 출력해줌
# 감속을 하면 속도를 10씩 감소하고 출력해줌
# 중지를 하면 플래그 변수를 이용하여 무한 루프를 빠져나감

run = True
# print(type(run))
# bool이라는 클래스 객체타입
speed = 0
# 1,2,3번을 누를 때 받는 값
keyCode = 0

# while True -> 무한루프
while run:
    print("----------------------------")
    print("1.증속  |  2.감속  |   3.중지")
    print("----------------------------")
    keyCode = int(input("선택 : "))

    # 증속일 경우
    if keyCode == 1:
        speed += 10
        print("현재 속도는", speed, "입니다.")
    # 감속일 경우
    elif keyCode == 2:
        speed -= 10
        if speed < 0:
            print("속도는 음수일 수 없습니다. 뒤로 갈까요?")
            speed = 0
        else:
            print("현재 속도는", speed, "입니다.")
    # 중지일 경우 플래그 변수를 False 로 설정해줌으로써 무한 루프를 탈출하는 코드
    elif keyCode == 3:
        run = False
    # 사용자가 잘못 입력했을 경우
    else:
        print("잘못된 입력값입니다.")

print("프로그램을 종료합니다.")