import sys

sys.stdin = open("2755.txt", "r")

T=int(input())
q=0
w=0
for i in range(1,T+1):
    a,b,c=map(str,input().split())
    w+=int(b)
    if c=="A+":
        q+=4.3*int(b)
    elif c=="A0":
        q+=4.0*int(b)
    elif c=="A-":
        q+=3.7*int(b)
    elif c=="B+":
        q+=3.3*int(b)
    elif c=="B0":
        q+=3.0*int(b)
    elif c=="B-":
        q+=2.7*int(b)
    elif c=="C+":
        q+=2.3*int(b)
    elif c=="C0":
        q+=2.0*int(b)
    elif c=="C-":
        q+=1.7*int(b)
    elif c=="D+":
        q+=1.3*int(b)
    elif c=="D0":
        q+=1.0*int(b)
    elif c=="D-":
        q+=0.7*int(b)
    else:
        q+=0.0*int(b)
print("%.2f" % round(q/w+10**-10,2))