import sys
sys.stdin = open("27889.txt", "r")

q=input()

if q=="NLCS":
    print("North London Collegiate School")
elif q=="BHA":
    print("Branksome Hall Asia")
elif q=="KIS":
    print("Korea International School")
else:
    print("St. Johnsbury Academy")

