import sys

sys.stdin = open("2822.txt", "r")

s=[]
q=[]
t=0

for i in range(8):
    s.append(int(input()))

for j in range(5):
    t += max(s)
    a = s.index(max(s))
    q.append(a+1)
    s[a] = 0

print(t)
print(*(sorted(q)))
    

