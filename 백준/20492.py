import sys
sys.stdin = open("20492.txt", "r")

s=int(input())

q=(s/100)*22#제세공과금22%
w=(s/100)*80#경비
e=((s-w)/100)*22#경비빼고 남은 상금에 제세공과금22%
print(round(s-q),round(s-e))