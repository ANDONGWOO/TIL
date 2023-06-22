import sys
sys.stdin = open("11816.txt", "r")

x=input()
if x[:2]=="0x":#16진수
    print(int(x,16))
    sys.exit(0)#종료
elif x[0]=="0":#8진수
    print(int(x,8))
else:#10진수
    print(int(x))