import sys
from collections import Counter
sys.stdin = open("2108.txt", "r")

n=int(sys.stdin.readline())
s=[]

for i in range(n):
    s.append(int(sys.stdin.readline()))
print(round(sum(s)/n))#산술평균
s.sort()
print(s[n//2])#중앙값

c=Counter(s)
x = c.most_common()
if len(x)>1:
    if x[0][1] == x[1][1]:
        print(x[1][0])
    else:
        print(x[0][0])
else:
    print(x[0][0])#최빈값

print(max(s)-min(s))#범위
