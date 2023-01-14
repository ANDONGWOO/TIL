import sys
sys.stdin = open("17249.txt", "r")


t1,t2=input().split('(^0^)')

print(t1.count('@'),t2.count('@'))