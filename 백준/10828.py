import sys
sys.stdin = open("10828.txt", "r")
n=int(sys.stdin.readline())

stack=[]
for i in range(n):
    s=sys.stdin.readline().split()
    w=s[0]
    if w=='push':
        stack.append(s[1])
    elif w=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())       
    elif w=='size':
        print(len(stack))
    elif w=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif w=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])