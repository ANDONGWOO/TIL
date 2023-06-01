import sys
sys.stdin = open("7600.txt", "r")


w=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while True:
    q=input().upper()
    s=0
    if q=="#":
        break

    for i in set(q):
        if i in w:
            s+=1
    print(s)
