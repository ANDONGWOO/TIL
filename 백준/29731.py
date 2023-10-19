import sys

sys.stdin = open("29731.txt", "r")


w=[
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
]
t=int(input())
e=False
for _ in range(t):
    q=input()
    if q not in w:
        e=True
        break
if e == True:
    print("Yes")
else:
    print("No")


