import sys
sys.stdin = open("21567.txt", "r")

a=int(input())
b=int(input())
c=int(input())
for i in range(10):
    print(str(a*b*c).count(str(i)))

#a*b*c합 17,037,300
#출력 합에  수 카운터
