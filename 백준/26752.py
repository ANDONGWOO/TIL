import sys
sys.stdin = open("26752.txt", "r")

a,b,c=map(int,input().split())



s=a*3600 + b*60 + c+1

a=str(s//3600%24)
b=str(s%3600//60)
c=str(s%60)

print(f"{a.zfill(2)}:{b.zfill(2)}:{c.zfill(2)}")


#문자열 앞 0