# 입력받은 문자열을 거꾸로 출력하는 프로그램
statements = input("문자열 입력 : ")
s_reverse = ""
# for 문을 활용한 방법
for ch in statements:
    # 복합대입연산자는 사용하면 안 됨
    s_reverse = ch + s_reverse

print("입력한 문자열입니다 : " + statements)
print("역순으로 출력한 문자열입니다 : " + s_reverse)

# list() 함수는 문자열을 리스트 타입으로 바꾸는 함수
print("--------------------")
s_list = list(statements)
# print(type(s_list))
# reverse() 는 리스트 타입만을 역순으로 바꿔주는 함수
s_list.reverse()
# join() 함수는 역순으로 된 문자열을 연결해서 출력을 하고 있는 코드
print("".join(s_list))

print("--------------------")
s1 = statements
# reversed() 는 문자열에만 역순으로 하는 함수
print("".join(reversed(s1)))

# 파이썬에서는 [::-1]를 사용해서 문자열을 역순으로 출력할 수 있음
print("--------------------")
print(statements[::-1])
print("--------------------")
# 문자열 2번째 인덱스부터 역순으로 출력하는 방법
print(statements[2::-1])