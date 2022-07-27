#별 증가
#공백*N-i + 문자열 별*i
N=int(input())

for i in  range(1,N+1):
    print(' '*(N-i)+'*'*i)
