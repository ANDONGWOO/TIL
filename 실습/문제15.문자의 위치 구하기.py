#문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
#a 가 없는 경우에는 -1을 출력해주세요.
#find() index() 메서드 사용 금지

from operator import le

word = 'banana'
c = 'a'
lst = []
for pos,char in enumerate(word):
    if(char == c):
        lst.append(pos)
   
i = lst
if len(lst) == 0:
    print(-1)
else:
   print(i.pop(0))
 



