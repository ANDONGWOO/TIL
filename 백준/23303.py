import sys

sys.stdin = open("23303.txt", "r")



a=input()
if 'D2' in a or 'd2' in a:
    print('D2')
elif 'D2' not in a or 'd2' not in a:
    print('unrated')