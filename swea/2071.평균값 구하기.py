# from operator import truediv
# import sys

# sys.stdin = open("2071.txt", "r")


#10개 더하고 10으로 나누고

#반올림하고 정수 출력 round
T = int(input())
total=0
b=0

for test_case in range(1,T+1):
   
    a =list(map(int, input().split()))
    for i in a:
        
        while(True):
            total+=i
            b+=1
            b==10
            break 
        b=round(total/10)
    total=0 #중첩때문에 0 할당
    print(f"#{test_case} {b}") 
