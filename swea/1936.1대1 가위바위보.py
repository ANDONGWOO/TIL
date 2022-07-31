
import sys
sys.stdin = open("1936.txt", "r")


A,B=map(int,(input()).split())
ip1="A"
ip2="B"
if A==2 and B==1:
    print(ip1)
elif A==3 and B==2:
    print(ip1)
elif A==3 and B==1:
    print(ip1)
elif A==1 and B==3:
    print(ip2)
elif A==2 and B==3:
    print(ip2)
elif A==1 and B==2:
    print(ip2)


