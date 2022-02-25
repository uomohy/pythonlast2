# 반복문으로 문자열 관련 처리하기 실습
dessert = "coffee"
# dessert 문자열 변수에 값을 하나씩 문자형태로 가져와서 출력하는 코드
for letter in dessert:
    print(letter, end=" ")
print("")
# 사용자로부터 문자열(영문)을 입력받아서 모음을 전부 없애는 코드
print("---------------------------")
s = input("문자열을 입력(영문자만) : ")
# 영문자의 모음의 문자열
vowels = "aeiouAEIOU"
result = ""
for letter in s:
    # 하나씩 반복하는 문자가 모음 문자열에 존재하지 않는다면 참을 반환
    if letter not in vowels:
        result += letter

print("자음 : " + result)

# 문자열을 입력받아서 자음과 모음의 개수를 집계하는 코드
print("--------------------------------")
original = input("문자열을 입력(영문자만) : ")
# 입력 받은 문자열을 전부 대문자로 변경함
word = original.upper()      # 소문자로 바꾸고 싶다면 lower()사용
vowels = 0
consonants = 0 # 자음
# 문자열의 길이가 0을 초과하고, 알파벳이라면 참을 반환함
if len(original) > 0 and original.isalpha():
    for ch in word:
        # 루프변수의 값이 모음에 해당하면
        if ch in "AEIOU":
            vowels += 1
        else:      # 자음이라면
            consonants += 1

print("모음은", vowels, "개 입니다.")
print("자음은", consonants, "개 입니다.")