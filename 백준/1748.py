import sys

sys.stdin = open("1748.txt", "r")


t=int(input())
q=0
if t<10:
    print(t)
else:
    for i in range(len(str(t))-1):
        q+=9*(10**i)*(i+1)
    print(q+(t-10**(len(str(t))-1)+1)*len(str(t)))

