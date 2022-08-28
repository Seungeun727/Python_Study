# 숫자 

# 숫자-더하기
addNumber = 2 + 2
print('더하기 연산(1)', addNumber)    # result 4

addNumber2 = 2 + 2.0
print('더하기 연산(2)', addNumber2)   # result: 4.0
# 숫자-나눗셈 
# 1.나눗셈연산 -float 반환(/ 사용)
floatNumber = 17 / 3
print('float형 나눗셈 연산 몫', floatNumber)   # result: 5.666666666666667

# 2. 나눗셈연산- 정수 반환(// 사용)
intNumber = 17 // 3
print('정수형 나눗셈 연산 몫', intNumber)  # result: 5

# 3. 나눗셈연산- 나머지 얻기
remainder = 17 % 3
print('나눗셈 계산 나머지', remainder)   # result: 2


# 숫자 - 거듭제곱 계산
powerNumber = 5 ** 2
print('거듭제곱 연산', powerNumber)  # result: 25


# 변수 생성 및 초기화
# 변수에 값 대입은 대입연산자(=) 사용한다.
width = 200
height = 300
print('너비와 높이 곱셈 연산', width * height)  # result: 60000

# 예시) 변수 값이 없는 경우
# n => NameError: 이름 'n'이(가) 정의되지 않았습니다. 'N'을 의미했나요?

# 실수 연산 
print(4 * 3.56 - 1)  # result : 13.24


## 실습

# 1) 변수 값 대입
nickName = 'knswe120'
age = 35
print('저의 닉네임은', nickName,'이고 나이는', age,'입니다')

# 산술 연산
addNumber2 = 4 + 8
print('더하기 연산', addNumber2)    # result: 12

minusNumber = 10 - 1 
print('빼기 연산', minusNumber)     # result: 9

multipleNumber = 2 * 9 
print('곱셈 연산', multipleNumber)   # result: 18

divideNumber = 10 / 5 
print('나눗셈 연산(1)', divideNumber)   # result: 2.0

divideNumber2 = 30 / 5
print('나눗셈 연산(2)', divideNumber2)  # result: 6.0

remainder2 = 50 / 3 
print('나눗셈 나머지 연산', remainder2)  # result: 16.666666666666668