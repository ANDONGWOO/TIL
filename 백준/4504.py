import sys
sys.stdin = open("4504.txt", "r")

n=int(input())

while 1:
    t=int(input())
    if t==0:
        break
    if t<n or t%n!=0:#n작다면 배수x 나머지가 0이 아니면 배수 x
        print(t,'is NOT a multiple of',str(n)+'.')
    else:
        print(t,'is a multiple of',str(n)+'.')
