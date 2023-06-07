import sys
sys.stdin = open("5656.txt", "r")
s=0
while True:
    a,b,c=map(str, input().split())
    if b=='E':
        break
    if b==">":
        s+=1
        z=int(a)>int(c)
        print(f"Case {s}: {str(z).lower()}")
    if b==">=":
        s+=1
        z=int(a)>=int(c)
        print(f"Case {s}: {str(z).lower()}")
    if b=="<":
        z=int(a)<int(c)
        s+=1
        print(f"Case {s}: {str(z).lower()}")
    if b=="<=":
        z=int(a)<=int(c)
        s+=1
        print(f"Case {s}: {str(z).lower()}")
    if b=="==":
        s+=1
        z=int(a)==int(c)
        print(f"Case {s}: {str(z).lower()}")
    if b=="!=":
        s+=1
        z=int(a)!=int(c)
        print(f"Case {s}: {str(z).lower()}")
