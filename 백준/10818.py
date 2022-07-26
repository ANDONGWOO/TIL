
T=int(input())
N=list(map(int,input().split()))

value1=N[0]
value2=N[0]
for i in  N:
    if i<value1:
        value1=i
    if i>value2:
        value2=i

print(value1 , value2)