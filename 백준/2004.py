import sys

sys.stdin = open("2004.txt", "r")
a,b=map(int, input().split())


def test(a,b):
    s=0
    while a>=b:
        s+=a//b
        a//=b
    return s#test()에서 b인자가 크다 s 리턴
s_2=test(a,2)-test(b,2)-test(a-b,2)
s_5=test(a,5)-test(b,5)-test(a-b,5)
print(min(s_2,s_5))