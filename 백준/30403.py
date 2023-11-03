import sys
sys.stdin = open("30403.txt", "r")

n = int(input())
q = input()
z = set(['r', 'o', 'y', 'g', 'b', 'i', 'v'])
x = set(['R', 'O', 'Y', 'G', 'B', 'I', 'V'])
w = set(filter(str.islower, q))
e = set(filter(str.isupper, q))

if z.issubset(w) and x.issubset(e):
    print("YeS")
elif z.issubset(w):
    print("yes")
elif x.issubset(e):
    print("YES")
else:
    print("NO!")