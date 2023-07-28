import sys
sys.stdin = open("21573.txt", "r")


a,b=map(int,input().split())
q=input()

if q=="heat":
    print(max(a,b))
elif q=="freeze":
    print(min(a,b))
elif q == "auto":
    print(b)
else:
    print(a)