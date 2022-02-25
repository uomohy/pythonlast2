# 사용자로부터 문자열을 입력받아서 알파벳 문자의 개수, 숫자의 개수,
# 스페이스의 개수를 출력하는 프로그램

sentence = input("문자열을 입력(영문자, 숫자, 공백) : ")

alpha_cnt = 0  # 알바벳 문자 개수
digit_cnt = 0  # 숫자 개수
spaces = 0     # 공백

for ch in sentence:
    if ch.isalpha():        # 알파벳이라면
        alpha_cnt += 1
    elif ch.isdigit():     # 숫자라면
        digit_cnt += 1
    elif ch.isspace():      # 공백이라면
        spaces += 1
    else:
        print("해당하는 문자는 알파벳, 숫자, 공백이 아닙니다.")

print("알파벳 문자는", alpha_cnt, "개입니다.")
print("숫자 문자는", digit_cnt, "개입니다.")
print("공백 문자는", spaces, "개입니다.")