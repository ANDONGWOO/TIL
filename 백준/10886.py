import sys
sys.stdin = open("10886.txt", "r")
input=sys.stdin.readline

q=int(input())#투표참가수
z=[]
e=0#투표결과 카운터
r=0#투표결과 카운터

for i in range(q):
    w=int(input())#투표 결과
    z.append(w)#투표 결과 리스트 만들고
for j in z:
    if j==1:
        e+=1#투표결과 카운터
    elif j==0:
        r+=1#투표결과 카운터
if e>r:#e가 작다면
    print('Junhee is cute!')
else:#r이 작다면
    print("Junhee is not cute!")