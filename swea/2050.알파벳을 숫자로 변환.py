
import sys
sys.stdin = open("2050.txt", "r")

english=input()
result=0
for i in english:
  result=ord(i)-64
  print(result,end=" ")