import sys
sys.stdin = open("5300.txt", "r")

t=int(input())
q=[]
for i in range(1,t+1):
    q.append(i)
    if i==t:
        q.append('Go!')
    if i%6==0:
        q.append('Go!')
if t%6==0:#6배수이면 예)1 2 3 4 5 6 Go! 7 8 9 10 11 12 Go! 13 14 15 16 17 18 Go! Go! 
    del q[-1]#그래서 마지막 요소 삭제 
print(*q)