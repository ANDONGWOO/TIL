import sys

sys.stdin = open("26264.txt", "r")

n=int(input())

q=input()

if q.count("bigdata")>q.count("security"):
    print("bigdata?")
elif  q.count("bigdata")<q.count("security"):
    print("security!")
else:
    print("bigdata? security!")
