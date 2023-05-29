import sys

sys.stdin = open("15813.txt", "r")
w=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n=int(input())

q=list(input())
q.sort()
s=0
for i in range(len(w)):
    for j in q:
        if w[i]==j:
            s+=i+1
print(s)
#알파벳 리스트