
import sys
sys.stdin = open("10995.txt", "r")

t=int(input())


if t == 1:
    print('*')
    
else: 
    for   i in range(t):# t의길이 따라 줄수출력
        if i% 2 == 0:
            print('* ' * t)#짝수면'* '별 t의개수 출력
        else:
            print(' *' * t)#홀수면' *'별 t의개수 출력
#그래서 for에서 줄수 print에서 ('* ')별공백,(' *')공백별 이런식으로 t의개수 곱하고 출력