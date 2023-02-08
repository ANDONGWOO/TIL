import sys

sys.stdin = open("26489.txt", "r")

s=0


while 1:
    try:
        a=input()
        s+=1
    except EOFError:
        break
print(s)
