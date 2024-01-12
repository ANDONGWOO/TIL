import sys
sys.stdin = open("31090.txt", "r")

t=int(input())

for i in range(t):
    q=input()
    if (int(q)+1)%int(q[2:])==0:
        print("Good")
    else:
        print("Bye")