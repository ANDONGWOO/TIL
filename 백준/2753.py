
N=int(input())
if N%4==0 and N %100 !=0 : # N%4 0이 나오면 4배수  N%100 0나오면 100배수 NOT
    print(1)               #윤년
elif N%4==0 and N%400==0:#N%4 0이 나오면 4배수  N%400 0나오면  400배수 
    print(1)     #윤년
else:
    print(0)
        