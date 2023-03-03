import sys

sys.stdin = open("10480.txt", "r")

t=int(input())
for i  in range(t):
    s=int(input())
    if s%2==0:
        print(s,'is even')
    else:
        print(s,'is odd')