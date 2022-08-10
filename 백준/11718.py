import sys

sys.stdin = open("11718.txt", "r")

while True:
    try:
        for i in range(1,100+1):
            a=input()
            print(a)
    except EOFError:
        break