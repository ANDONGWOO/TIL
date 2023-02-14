import sys
from itertools import combinations
sys.stdin = open("1182.txt", "r")
input=sys.stdin.readline
a,b=map(int,input().split())

q=list(map(int,input().split()))
s=0
for i in range(1,a+1):
    z= combinations(q,i)#반복문 1~a으로 조합 할수있는 경우수 z 할당
    for j in z:#z의 요소
        if sum(j)==b:#j의 합이 b 같다면 
            s+=1#s +1
print(s)