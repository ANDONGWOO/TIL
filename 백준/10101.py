import sys

sys.stdin = open("10101.txt", "r")

a=int(input())
b=int(input())
c=int(input())

if a==b==c and a==60:
    print('Equilateral')
elif a+b+c==180:#Isosceles 조건/Scalene 조건 합180이면 조건1 같다
    if a==c or a==b or b==c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
