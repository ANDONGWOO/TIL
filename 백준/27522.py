import sys
sys.stdin = open("27522.txt", "r")
q=[]
for _ in range(8):
    a=input().split()
    q.append(a)
q.sort()
s1=0#점수
s2=0#점수
#1등,2등,3등
if q[0][1]=="B":
    s1+=10
else:
    s2+=10
if q[1][1]=="B":
    s1+=8
else:
    s2+=8
if q[2][1]=="B":
    s1+=6
else:
    s2+=6
#4등~8등
for i in range(3,8):
    if q[i][1]=="B":
        s1+=8-i#점수5,4,3,2,1
    else:
        s2+=8-i#점수5,4,3,2,1
if s1<s2:
    print('Red')
else:
    print('Blue')
