#문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

from unittest import result


word = 'banana'

result={}
for char in word:

    if not char in result:

        result[char] = 1

    else:
        result[char] = result.get(char,0) +1

print(result)
    
