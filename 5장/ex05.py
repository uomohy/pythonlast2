# for 문을 이용하여 팩토리얼(factorial)을 계산하는 프로그램을 작성해보기
# 팩토리얼 n! 은 1부터 n 까지의 정수의 모두 곱한 것을 의미함
# f(1) = 1임

fact = 1.0
n = int(input("팩토리얼 값을 구할 정수를 입력 : "))

# stop 값은 포함하지 않기 때문에 n+1
for i in range(1, n+1):
    fact *= i      # fact = fac * i 를 복합대입연산자를 사용한 코드

print(n, "!은", fact, "입니다.")
