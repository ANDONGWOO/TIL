import sys
sys.stdin = open("12605.txt", "r")

a=int(input())

for i in range(1,a+1):
    b=list(map(str,input().split()))
    b.reverse()
    print(f'Case #{i}:',*b)