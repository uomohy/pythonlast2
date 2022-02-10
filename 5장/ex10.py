# 터틀 그래픽을 활욯하여 별 모양을 그려보는 프로그램을 for 문을 이용하여 작성
# 터틀 모듈 사용
import turtle

# 펜의 기능을 t라는 변수에 저장함.
t = turtle.Pen()

for i in range(5):
    # 50픽셀만큼 이동
    t.forward(50)
    # 우측 방향으로 144도를 틈
    t.right(144)

# 터틀 그래픽 창이 클릭이 되어야 화면에서 사라지게 하는 코드
turtle.exitonclick()
