import sys
sys.stdin = open("31775.txt", "r")

q1,q2,q3 = [input() for _ in range(3)]

if sorted([q1[0], q2[0], q3[0]]) == ['k', 'l', 'p']:
    print("GLOBAL")
else:
    print("PONIX")
