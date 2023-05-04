import sys
import datetime
sys.stdin = open("1924.txt", "r")
a,b=map(int,input().split())#a월 b일
d=datetime.datetime(2007,a,b)#문제에서 2007년 a월b일 d할당하고
z=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']
#z는월~일
#d.weekday에서 월0,화1,수2,목3,금4,토5,일6
for i in range(7):#0~6
    if d.weekday()==i:
        print(z[i])