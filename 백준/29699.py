import sys

sys.stdin = open("29699.txt", "r")
s="WelcomeToSMUPC"
n=int(input())
print(s[(n%14)-1])