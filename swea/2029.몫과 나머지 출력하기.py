# import sys

# f = open("2029.txt", "r" )
# line = f.readline()
# sys.stdin = open("2029.txt", "r")


T = int(input())
for i in range(T):
    a, b = map(int, input().split()) 
    c=a//b 
    d= a%b
    print(f"#{i+1} {c} {d}")