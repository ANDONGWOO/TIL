
import sys
sys.stdin = open("10820.txt", "r")
while 1:
    try:
        a=list(input())
        s=[0,0,0,0]
        for i in range(len(a)):
            if a[i]==" ":#공백
                s[3]+=1
            elif 65<=ord(a[i])<=90:#대문자
                s[1]+=1
            elif 97<=ord(a[i])<=122:#소문자
                s[0]+=1
            else:#숫자
                s[2]+=1
        print(*s)
    except EOFError:
        break
