import sys

sys.stdin = open("5585.txt", "r")

n=1000-int(input())

count=0
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += n // coin #매수
    n %= coin #나머지

print(count)