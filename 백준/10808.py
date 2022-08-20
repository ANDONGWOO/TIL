import sys
sys.stdin = open("10808.txt", "r")

s=list(input())
z=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in s:
    w=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
    for q in range(len(w)):
        if  i == w[q]:
            z[q]+=1
print(*z)