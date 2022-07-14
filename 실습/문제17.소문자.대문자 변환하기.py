#소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
#.upper(), .swapcase() 사용 금지




word = 'banana'
result=''
for char in word:
    number = ord(char)

    number= number-32

    result += chr(number)
print(result)

