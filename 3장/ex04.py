# 문자열에 대한 실습

# 큰따옴표(double quotation)로 묶으면 문자열이 됨(권장)
welcome = "Happy New Year 2021"
print(welcome)
# 작은따옴표(single quotation)로 묶어도 문자열이 됨
welcome = 'Happy New Year 2021'
print(welcome)
# 문자열을 만들때 시작을 "으로 했는데 '으로 끝을 낸다면, EOL(End Of Line)에러가 발생
# 그 이유는 "로 시작을 했는데 "의 끝 내용을 찾을 수 없다라고 하는 것
# welcome = "Happy New Year 2021'
# print(welcome)

# welcome = "Happy New Year 2021
# print(welcome)

# 아래와 같이 ""안에 또 다른 ""이 들어있다면 컴파일러가 혼돈을 일으켜 틀린 문법이다라고
# 에러를 발생시킴
# message = "은혁이가 "안녕하세요"라고 인사했습니다."
# print(message)

message = "은혁이가 '안녕하세요'라고 인사했습니다."
print(message)

# 파이썬에서는 따옴표를 출력하고자 할 때, \를 이용함
# \가 따옴표 앞에 있으면 '는 특수한 의미를 잃어버리고 하나의 문자로 편승이 되어 문자열을 이름
message = 'doesn\'t'
print(message)

message = "\"Yes,\" I can do it"
print(message)

# 특수문자 형태인 \n은 개행(Enter)을 하는 문자
message = "Fist\nSecond\nThird"
print(message)

# 특수문자 \t는 탭만큼 띄우는 문자
message = "c:\temp\name"
print(message)
# 위에서 살펴봤던 \t, \n 이런 이스케이프 문자들의 기능을 제거를 시키기 위해서는
# 문자열 시작 앞에 r을 붙여줌(중요함)
message = r"c:\temp\name\a.mp3"
print(message)


# 문자열(영어나 한글 상관없음)의 길이를 알고자 한다면 len()함수를 이용함
message = "신은혁"
print("문자열의 길이 : ", len(message))

