# 왼쪽 공백만 제거하는 함수 (lstrip())
statements = "    멍멍!"
print("제거하기 전 문자열: " + statements)
print("왼쪽 공백 제거한 후: " + statements.lstrip())

print("----------------------------------")
# 오른쪽 공백만 제거하는 함수 (rstrip())
statements = "멍멍!                 "
print("제거하기 전 문자열: " + statements)
print("오른쪽 공백 제거한 후: " + statements.rstrip())
print("----------------------------------")
# 양쪽 공백만 제거하는 함수 (strip())
statements = "             멍멍!         "
print("제거하기 전 문자열:" + statements)
print("양쪽 공백 제거한 후:" + statements.strip())

# 문자열 나누가 split() 리스트 타입
print("----------------------------------")
statements = "강아지가 월월 짖는다."
print(statements.split())