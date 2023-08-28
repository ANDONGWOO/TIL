import sys
sys.stdin = open("7510.txt", "r")

n=int(input())

for i in range(1,n+1):
    s=list(map(int,input().split()))
    s.sort()

    if s[0]**2+s[1]**2==s[2]**2:
        print(f'Scenario #{i}:')
        print("yes")
        print()
    else:
        print(f'Scenario #{i}:')
        print("no")
        print()