import sys
sys.stdin = open("2566.txt", "r")
input=sys.stdin.readline


# e=0
# q,w = 0,0
# for i in range(9):
#     b=list(map(int,input().split()))
#     if max(b)> e:
#         e=max(b)#최대값 출력
#         q=i
#         w=b.index(e)#0시작
# print(e)
# print(q+1,w+1)

a=[]

for i in range(9):
    b=list(map(int,input().split()))
    a.append(b)
e=0
q=0
w=0
for z in range(9):
    for x in range(9):
        if a[z][x] > e:
            e=a[z][x]#최대값 출력
            q=z
            w=x
               
print(e)
print(q+1,w+1)