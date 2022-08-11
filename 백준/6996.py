
import sys
sys.stdin = open("6996.txt", "r")

T=int(input())
for i in range(T):
    a,b=map(str,input().split())
    q=sorted(a)
    w=sorted(b)
    if q==w:  
        print(f'{a} & {b}',('are anagrams.'))
    else:
        print(f'{a} & {b}',('are NOT anagrams.'))
