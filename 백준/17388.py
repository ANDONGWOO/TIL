import sys
sys.stdin = open("17388.txt", "r")



a,b,c=map(int,input().split())

if a+b+c>=100:
    print("OK")
else:
    q=min(a,b,c)
    if q==a:
        print("Soongsil")
    elif q==b:
        print("Korea")
    else:
        print("Hanyang")