import sys

sys.stdin = open("30224.txt", "r")

s=input()
if not s.isdigit():
    print("Not an integer!")
else:
    num = int(s)
    has_7 = '7' in s
    divisible_by_7 = num % 7 == 0

    if not has_7:
        if divisible_by_7:
            print(1)
        else:
            print(0)
    else:
        if divisible_by_7:
            print(3)
        else:
            print(2)