import sys
import re
sys.stdin = open("5637.txt", "r")

q=[]
while 1:
    q.extend(input().split())
    if q[-1]=="E-N-D":
        break
q=[re.sub('[^a-z-]','',i.lower()) for i in q]    
q.sort(key=lambda x:len(x),reverse=True)
print(q[0].lower())