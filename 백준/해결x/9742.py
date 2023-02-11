import sys
from itertools import permutations
sys.stdin = open("9742.txt", "r")

def h():
    g=''
    for i in list(permutations(list(a),len(a)))[b-1]:
        g+=i
    return g
while 1:
    try:
        a,b=input().split()
    except:
        break
    b=int(b)
    if len(list(permutations(list(a),len(a))))<b:
        print(a,b,'= No permutation')
    else:
        print(a,b,'=',h())