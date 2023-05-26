import sys
sys.stdin = open("28074.txt", "r")

q=['M', 'O', 'B', 'I', 'S']

w=list(input())
for i in q:
    if w.count(i)==0:
        print("NO")
        sys.exit(0)#조건문 해당이면 종료
print("YES")