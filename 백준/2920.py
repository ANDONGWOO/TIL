import sys

sys.stdin = open("2920.txt", "r")
a=['1', '2', '3', '4', '5', '6', '7', '8']
b=['8', '7', '6', '5', '4', '3', '2', '1']


t=list(input().split())
if t==a:
    print("ascending")
elif t==b:
    print("descending")
else:
    print("mixed")