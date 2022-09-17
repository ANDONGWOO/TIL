import sys
sys.stdin = open("15726.txt", "r")

a,b,c=map(int, input().split())
q=a*b/c#문제에서 한 번은 곱하고 한 번은 나누고 값 두 개를 만들고
w=a/b*c#문제에서 한 번은 나누고 한 번은 곱하고  값 두 개를 만들고

if q>w:
    print(int(q))#q가 크다면, 정수로출력
else:
    print(int(w))#q가 작다면, 정수로출력

