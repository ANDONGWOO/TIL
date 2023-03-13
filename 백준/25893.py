import sys
sys.stdin = open("25893.txt", "r")
z=['zilch','double','double-double','triple-double']
for i in range(int(input())):
    a=list(map(int,input().split()))
    s=0
    for i in a:
        if i>=10:
            s+=1
    if s==0:
        print(*a)
        print(z[s])
        print()
    elif s==1:
        print(*a)
        print(z[s])
        print()
    elif s==2:
        print(*a)
        print(z[s])
        print()
    else:
        print(*a)
        print(z[s])
        print()