import sys
sys.stdin = open("31800.txt", "r")

n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
b=list(map(int, sys.stdin.readline().split()))
q = []
for i in range(n):
    w = a[:i] + a[i+1:]
    e = max(w)
    q.append(e)  
    print(a[i]-((q[i]-b[i])+b[i]), end=' ')
#x