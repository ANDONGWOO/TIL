import sys
sys.stdin = open("16503.txt", "r")

q,w,e,r,t=map(str,input().split())
q=int(q)
e=int(e)
t=int(t)
a=0#총합
b=0#총합
if r=="+":
    b+=e+t
elif r=="-":
    b+=e-t
elif r=="/":
    b+=e//t
elif r=="*":
    b+=e*t
if w=="+":
    b=q+b
elif w=="-":
    b=q-b
elif w=="/":
    b=q//b
elif w=="*":
    b=q*b
#b
if w=="+":
    a+=q+e
elif w=="-":
    a+=q-e
elif w=="/":
    a+=q//e
elif w=="*":
    a+=q*e
if r=="+":
    a=a+t
elif r=="-":
    a=a-t
elif r=="/":
    a=a//t
elif r=="*":
    a=a*t
#a
if a<b:
    print(a)
    print(b)
else:
    print(b)
    print(a)

