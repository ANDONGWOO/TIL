import sys
sys.stdin = open("23037.txt", "r")


s=list(map(int,input()))#입력 값리스트
q=0#5제곱 저장할 q
for i in range(len(s)):
   q+=s[i]**5
print(q)