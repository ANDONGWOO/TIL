import sys
sys.stdin = open("4880.txt", "r")



while 1:
    a,b,c=map(int,input().split())
    if a==b==c and a==0:
        break
    if a-b == b-c:#동일한 수 -3  등차수열
        print("AP",c+c-b)
    else:#아니면 등비수열
        print("GP",c*(c//b))