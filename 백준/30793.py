import sys
sys.stdin = open("30793.txt", "r")

a,b=map(int,input().split())

if a/b<0.2:
    print("weak")
elif 0.2<=a/b<0.4:
    print("normal")
elif 0.4<=a/b<0.6:
    print("strong")
else:
    print("very strong")
