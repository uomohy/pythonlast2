# 사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램
# 사용자가 몇 개의 상품을 살지 모르니깐 무한루프를 이용을 하고
# 사용자가 "끝"이라고 입력을 하면 루프를 탈출하게끔 조건을 주도록 함
# from operator import eq
import operator
total = 0
# price는 str 타입
price = ""
# 무한루프 코드
while True:
    # '끝'이라는 단어를 입력받으면 종료되기 때문에 int를 사용하지 않음
    price = input("상품 금액을 입력 ('끝'을 입력하면 종료) : ")
    # "끝"이라는 입력 문구가 있는지 확인하는 코드, 무한 루프를 탈출하는 코드
    if operator.eq(price, "끝"):      # if price == "끝" / if price.eq("끝") 동일한 코드
        # total은 + 연산자를 쓰려면 str 함수를 써야함
       print("상품의 총 가격 : " + str(total) + "원!")
       break
    # 상품의 가격을 누적하는 코드
    # 문자열로 넘어오기 때문에 int함수를 써서 누적을 시켜줌
    total += int(price)

