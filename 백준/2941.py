import sys

sys.stdin = open("2941.txt", "r")

q=input()
w=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in w:
    q=q.replace(i,'/')#i /으로 변경
# print(q)#/e//ak
print(len(q))
    