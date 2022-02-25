# 입력받은 문자열의 'a'와 공백을 제거한 문자열을 출력하는 프로그램

statements = input("원하는 문자열을 입력하세요 : ")
# 공백을 제거한 부분을 저장하기 위한 스트링 타입의 변수 초기화
result = ""

for ch in statements:
    # 루프문자가 'a'와 공백이 아니라면
    if ch != "a" and ch != " ":
        result += ch

print("입력한 문자열 : " + statements)
print("a와 공백을 제거한 문자열 : " + result)
