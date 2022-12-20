
import sys
sys.stdin = open("10867.txt", "r")

n=int(input())
s=list(map(int,input().split()))
q=[]
q=sorted(set(s))
print(*q)
#set(s)중복 제거
#q에 정렬하고 할당
#중복 제거후 정렬