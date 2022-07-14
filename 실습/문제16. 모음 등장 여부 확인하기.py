#문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
#모음 : a, e, i, o, u 
#count() 사용 금지

word = 'zxcvb'
word1 = 'a'
word2 = 'e'
word3 = 'i'
word4 = 'o'
word5 = 'u'
find1 = [pos for pos, char in enumerate(word) if char == word1]
find2 = [pos for pos, char in enumerate(word) if char == word2]
find3 = [pos for pos, char in enumerate(word) if char == word3]
find4 = [pos for pos, char in enumerate(word) if char == word4]
find5 = [pos for pos, char in enumerate(word) if char == word5]
print(len(find1+find2+find3+find4+find5))
