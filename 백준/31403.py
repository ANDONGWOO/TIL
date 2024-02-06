import sys
sys.stdin = open("31403.txt", "r")

a=int(input())
b=int(input())
c=int(input())
print(a+b-c)

print(int(str(a)+str(b))-c)