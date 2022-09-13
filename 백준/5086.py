import sys
sys.stdin = open("5086.txt", "r")


while 1:
    a,b=map(int,sys.stdin.readline().split())
    if a==0 and b==0:#케이스 끝 뒤에 배치하면 0,0도 케이스로 인식
        break
    if  b%a==0:#배수
        print('factor')
    elif a%b==0:#약수
        print('multiple')
    elif b%a!=0 and (a%b!=0):#둘다 아니면 
        print('neither')
        

