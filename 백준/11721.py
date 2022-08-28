
import sys
sys.stdin = open("11721.txt", "r")

s=input()

for i in  range(0,len(s),10):
    print(s[i:i+10])