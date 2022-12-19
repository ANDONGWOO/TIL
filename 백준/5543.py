import sys
sys.stdin = open("5543.txt", "r")

w=[]#버거최저
r=[]#음료최저
for i in range(1,3+1):
    q=int(input())
    w.append(q)
for j in range(1,2+1):
    e=int(input())
    r.append(e)
print((min(r)+min(w))-50)#합-50