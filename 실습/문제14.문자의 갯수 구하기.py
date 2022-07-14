#문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
#count() 메서드 사용 금지

word = 'apple'

c = 'a'

find = [pos for pos, char in enumerate(word) if char == c]


print(len(find))
