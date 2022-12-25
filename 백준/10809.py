import sys
sys.stdin = open("10809.txt", "r")


s=input()
q ='abcdefghijklmnopqrstuvwxyz'

for i in q:
    if i in s:#i는 알파벳 하나씩 알파벳 순서로/ 
        print(s.index(i), end=" ")
    else:#중복제거 필요x 중복있다면 -1
        print(-1, end=" ")