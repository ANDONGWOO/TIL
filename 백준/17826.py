
import sys
sys.stdin = open("17826.txt", "r")

s=list(map(int,input().split()))
s.sort(reverse=True)
grades1=[0,1,2,3,4]
grades2=[5,6,7,8,9,10,11,12,13,14]
grades3=[15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
grades4=[30,31,32,33,34]
grades5=[35,36,37,38,39,40,41,42,43,44]
grades6=[45,46,47]
grades7=[48,49]


q=int(input())
for i in range(len(s)):
    if s[i]==q:
        w=i
        if w in grades1 :#1등에서5등
            print('A+')
        if  w in grades2 :#6등에서15등
            print('A0')
        if  w in grades3 :#16등에서30등
            print('B+')
        if   w in grades4:#31등에서35등
            print('B0')
        if   w in grades5 :#36등에서45등
            print('C+')
        if  w in grades6 :#46등에서48등
            print('C0')
        if  w in grades7 :#49등에서50등
            print('F')
