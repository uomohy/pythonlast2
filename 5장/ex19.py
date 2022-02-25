# 더블 루프를 이용하여 아래와 같이 출력하는 프로그램
# 출력결과
#   *
#  ***
# *****

# 1. 더블루프 사용
for i in range(1, 4):
    # 공백을 찍는 내부루프
    for j in range(3-i):
        print(" ", end="")
    # 별표를 찍는 부분
    # stop 값은 포함이 안됨
    # j는 지역변 수이기 때문에 상관없음
    for j in range(1, i*2):
        print("*", end="")
    # 줄바꿈
    print("")

# 2. format() 이용 풀이
print("------------------")
for i in range(1, 6, 2):
    # 중앙 정렬을 위해서는 ^ 특수문자를 사용하면 됨
    print("{:^5}".format("*" * i))

# 더블 루프를 이용하여 아래와 같이 출력하는 프로그램을 작성
# 출력결과
#   *
#  ***
# *****
# *****
#  ***
#   *
print("------------------")
# 위의 삼각형 부분을 별로 찍는 코드
for i in range(1, 4):
    for j in range(3-i):
        print(" ", end="")
    for j in range(1, i*2):
        print("*", end="")
    print("")
# 아래의 역삼각형 부분을 별로 찍는 코드
for i in range(4):
    for j in range(i):
        print(" ", end="")
    for j in range(6, (i*2)+1, -1):
        print("*", end="")
    print("")
