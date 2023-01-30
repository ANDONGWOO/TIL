import sys

sys.stdin = open("1453.txt", "r")

print(int(input())-len(list(set(list(map(int, input().split()))))))