import sys
sys.stdin = open("27541.txt", "r")

q=int(input())

w=input()

if w[q-1]!="G":
    print(w+"G")
else:
    print(w[:q-1])