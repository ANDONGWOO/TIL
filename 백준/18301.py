import sys
sys.stdin = open("18301.txt", "r")

a,b,c=map(int,input().split())

N=(a + 1)*(b  + 1)//(c + 1) - 1

print(N)
