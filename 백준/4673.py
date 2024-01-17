

q=set()#생성이 가능한 수
w=set(range(1,10001))

for i in range(1,10001):
    q.add(sum(map(int,str(i)))+i)
e=sorted(set(w) - set(q))#생성이 가능한 수x
for i in e:
    print(i)