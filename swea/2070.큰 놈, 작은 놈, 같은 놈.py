
import sys
sys.stdin = open("2070.txt", "r")

T=int(input())


for i in range(1,T+1):
    a,b=map(int,(input()).split())
    if a!=b and a<b:
        c="<"
    elif a==b:
        c="="   
    elif (a>b and a!=b):
        c=">"
    
    
    print("#{} {}".format(i,c))

        


