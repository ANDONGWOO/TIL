import sys

sys.stdin = open("2010.txt", "r")
input=sys.stdin.readline
q=int(input())#멀티탭 개수
z=[]
for i in range(q):
    w=int(input())#멀티탭의  플러그개수
    z.append(w)#z리스트에 멀티탭의플러그개수
print(sum(z)-(q-1))#멀티탭 개수-1
