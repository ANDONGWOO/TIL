import sys
import datetime
sys.stdin = open("2948.txt", "r")
a,b=map(int,input().split())
x=datetime.datetime(2009,b,a)#b는월 a일
#x에서 년월일할당하고
#x.weekday()/요일 월0,화1,수2,목3,금4,토5,일6
#x.weekday() 숫자가 출력
z=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#z는월요일~일요일까지 리스트
for i in range(7):#0~6
    if x.weekday()==i:
        print(z[i])#z에서 i인덱스
