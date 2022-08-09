import sys

sys.stdin = open("2587.txt", "r")

s=[]
q=0
for i in range(5):
    s.append(int(input()))
    q+=s[i]
s.sort()
print(q//5)
print(s[2])




    