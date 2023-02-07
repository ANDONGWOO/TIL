import sys
sys.stdin = open("4592.txt", "r")

while 1 :
    q,w= input(),''
    if q=='0':break
    for i in q.split()[1:]:
        if i==w:
            continue
        print(i,end=' ')
        w=i
    print('$')