
# from re import I
# import sys
# sys.stdin = open("1986.txt", "r")
T = int(input())

a=0

for b in range(T):
  N = int(input())
  a=0
  for i in range(1,N +1):
    

    if i % 2 == 0:
      a-=i
    
#짝수는 빼기 
    elif i%2 ==1:
       a+=i
#홀수는 더하고 
  print(f"#{b+1}" ,a)