"""정규 표현식에 유니코드 사용"""
import re
num = re.compile('\d+')
print(num.match('123'))
# print(num.match('\u0661\u0662\u0663'))
