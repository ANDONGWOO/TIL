
#import sys
    
#sys.stdin = open("1989.txt", "r")

T = int(input())
for i in range(T):
    a = input().strip()
    print( f'#{i+1} {int(a==a[::-1])}' )