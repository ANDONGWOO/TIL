import sys

sys.stdin = open("26265.txt", "r")

n=int(input())
s=[]

for i in range(n):
    s.append(list(input().split()))

s.sort(key=lambda x: x[1], reverse=True)
s.sort(key=lambda x: x[0])
for a,b in s:
    print(a,b)


#n번 반복
#멘토의 이름/멘티의 이름 리스트에 저장(문자열로)
#리스트 정렬
