# 문자열 
# 작은 따옴표(''), 큰 따옴표("") 같은 결과를 반환한다.
from sys import prefix


product='spam eggs'
print(product)   # result: spam eggs

special='dosen\'t'
print(special)  # result: dosen't

special2="dosen't"
print(special2)  # result: dosen't

# print()는 따옴표 생략함
statement='"Yes, " they said.'
print(statement) # result: "Yes, " they said.

# \뒤에 문자 특수 문자 취급하지 않는 경우
## 첫따옴표 앞에 r 붙인다.
print('C:\some\name')
print(r'C:\some\name')


# 문자열에서 연산 
# + 연산: 문자열을 이어 붙인다.
# * 연산: 문자열을 반복한다.
repeat = 3 * 'un'+ 'ium'
print(repeat)   # result: unununium

# 연속된 문자열 리터럴
python = 'I' + 'love' + 'Python'
print(python)   # result: IlovePython

text = ('Put serveral strings within parenthess '
        'to have them joined together.')
print(text)   # result: Put serveral strings within parenthess to have them joined together.

## 연속된 문자열 리터럴은 변수, 표현식에 해당되지 않음
prefix = 'py'
prefix = 'thon'
print(prefix)  # result: thon

# 변수 또는 문자열 리터럴을 이어 붙일 때 + 사용한다.
prefix2 = 'py'
prefix3 = 'thon'
print(prefix2 + prefix3)

# 인덱스 접근 
# 범위가 벗어난 인덱스는 에러를 반환함
# 문자열은 변경안된다. => 새로운 문자열을 생성한다.
print(prefix2[0])  # result: firstIndex => p
print(prefix2[1])  # result: secondIndex => y
print(prefix2[-1]) # result: lastIndex => y

print(prefix3[0:4])  #result: thon
print(prefix3[:1])   #result: t
print(prefix3[3:])   #result: n
print(prefix3[-1:])   #result: n

# 문자열 길이
longString = 'happyfunnylovelycutebeautiful' 
print(len(longString))   # 29


# 실습

# 기본
sentence = 'You are a nice person'
print(sentence)       # result: You are a nice person

# 문자열 반복
repeat2 = 5 * 'happy'+ 'python'
print(repeat2)        # result: happyhappyhappyhappyhappypython

# 연속된 문자열 리터럴
continuity = 'I' + 'like' + 'Python'
print(continuity)     # result: IlikePython

# 문자열 인덱스 접근
word = 'AppleMangoOrangeKiwi'
print(word[0:5])      # result: Apple
print(word[4:])       # result: eMangoOrangeKiwi
print(word[:6])       # result: AppleM
print(word[-3:])      # result: iwi

# 총 문자열 길이
print(len(word))      # result: 20

