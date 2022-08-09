import sys

sys.stdin = open("1264.txt", "r")

s=['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
while 1:
    a=input()
    if a== '#':
        break# #나오면 
    q0=a.count(s[0])
    q1=a.count(s[1])
    q2=a.count(s[2])
    q3=a.count(s[3])
    q4=a.count(s[4])
    q5=a.count(s[5])
    q6=a.count(s[6])
    q7=a.count(s[7])
    q8=a.count(s[8])
    q9=a.count(s[9])
    print(q0+q1+q2+q3+q4+q5+q6+q7+q8+q9)
