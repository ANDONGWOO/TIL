import sys
sys.stdin = open("28295.txt", "r")

s = 0

for _ in range(10):
    q = int(input())
    if q == 1:
        s = (s + 1) % 4 
    elif q == 2:
        s = (s + 2) % 4  
    elif q == 3:
        s = (s + 3) % 4  

print(['N', 'E', 'S', 'W'][s])