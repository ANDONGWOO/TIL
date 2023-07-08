import sys

sys.stdin = open("28289.txt", "r")

while 1:
    n = input()
    if n == '0':
        sys.exit(0)
    q = len(n)+1
    for i in n:
        if i == '0':
            q += 4 
        elif i == '1':
            q += 2
        else:
            q += 3
    print(q)