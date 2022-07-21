
# 1부터 N의 배수인 양만 세기

#배수 1배2배3배


import sys
sys.stdin = open("1288.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N= int(input())
    a=0
    c = [0]*10

    while (True):
        if 0 not in c:
            break
        else :
            a +=1
            num =str(N*a)
            for j in range(len(num)):
                c[int(num[j])]=1
    print("#{} {}".format(test_case,num))