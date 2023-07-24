
import sys

sys.stdin = open("25285.txt", "r")

n=int(input())

for i in range(n):
    a,b=map(float,input().split())
    if a<159.0:
        if a<140.1:
            print(6)
        elif a>=140.1 and a<146.0:
            print(5)
        else:
            print(4)
    else:
        Bmi=b/((a/100) **2)
        if a>=159.0 and a<161:
            if Bmi>=16.0 and Bmi<35.0:
                print(3)
            else:
                print(4)
        elif a>=161.0 and a<204:
            if Bmi >=20.0 and Bmi<25.0:
                print(1)
            elif (Bmi >=18.5 and Bmi<20.0) or (Bmi >=25.0 and Bmi<30.0):
                print(2)
            elif (Bmi >=16.0 and Bmi<18.5) or (Bmi >=30.0 and Bmi<35.0):
                print(3)
            else:
                print(4)
        else:
            print(4)