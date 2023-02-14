import sys

sys.stdin = open("5800.txt", "r")

n=int(input())

for i in range(1,n+1):
    q=list(map(int,input().split()))
    del q[0]
    q.sort()
    x=[]
    print('Class',i)
    for j in range(len(q)-1):
        x.append(q[j+1]-q[j])
    print('Max', str(max(q))+',','Min', str(min(q))+',', 'Largest gap', max(x))
