import sys

sys.stdin = open("1157.txt", "r")
n=input().upper()#출력 값을 대문자

q=list(set(n))
e=[]
for i in q:#q원소 반복문돌려서
    w=n.count(i)
    e.append(w)
if e.count(max(e)) >= 2:
    print("?")
else:
    print(q[e.index(max(e))])