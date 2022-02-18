# 변수의 두 개의 값을 서로 바꾸는 예제

# one이라는 변수에 100을 저장함.
one = 100
two = 200
# one의 데이터 타입을 확인하는 방법은 type함수를 사용하면 됨
# print(type(one))
print("one : ", one, "two : ", two)

# 두 개의 변수값을 바꾸기 위해서는 임시변수가 필요함
temp = one
one = two
two = temp
print("one : ", one, "two : ", two)