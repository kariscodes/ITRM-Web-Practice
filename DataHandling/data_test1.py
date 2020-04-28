# 1. 숫자 앞에 0으로 자리 수 채우기
vStr = str(1).zfill(3)
print(vStr)

# join : 문자열을 합치는데 사용합니다. 구분자가 앞에서 사용되어집니다.
vStr = ' | '.join(['a','b','cde'])
print(vStr, type(vStr))

# 2. 기호로 문자열 나누기 (Split)
import re
vStr = re.split('~', '2020.01.01~2020.12.31')
print(vStr)

# 3. 문자열의 특정 문자 대체하기 (Replace)
vStr = '2011.01.01'.replace('.', '-')
print(vStr, vStr.__class__)

# 4. 문자형 날짜 날짜형으로 바꾸기
import datetime
# format: '%Y-%m-%d' - 유의: 'Y'가 대문자
vDate = datetime.datetime.strptime('2020-03-25', '%Y-%m-%d').date()
print(vDate, vDate.__class__)

# 5. 문자열 양끝 공백 제거하기
# 문자열 중간 공백은 그대로 두고 양 끝 공백들만 제거하기
vStr = '   2011-01-01 ~ 2011-12-31          '.strip()
print(vStr)

# 6. 날짜형 데이터 만들기
# 2011년 3월 27일이라는 날짜형 데이터 만들고 출력하기
from datetime import date
vDate = date(2011, 3, 27)
print(vDate, vDate.__class__)

# 7. 날짜형 데이터를 문자형 YYYYMMDD로 만들기
# format: '%Y-%m-%d' - 유의: 'Y'가 대문자
vStr = vDate.strftime("%Y%m%d"); print(vStr, vStr.__class__)
vStr = vDate.strftime("%Y-%m-%d"); print(vStr, type(vStr))

# capitalize: 첫 글자 대문자 나머지 문자 소문자로 변환합니다.
t = "abcdef"
vStr = t.capitalize()
print(t, vStr)

# 문자열 길이
vStr = "abcd12345abcdefg"; print(vStr, len(vStr))