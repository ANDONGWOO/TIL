import sys

sys.stdin = open("30087.txt", "r")
t=int(input())
for i in range(t):
    q=input()
    if q=="Algorithm":
        print('204')
    if q=="DataAnalysis":
        print('207')
    if q=="ArtificialIntelligence":
        print('302')
    if q=="CyberSecurity":
        print('B101')
    if q=="Network":
        print('303')
    if q=="Startup":
        print('501')
    if q=="TestStrategy":
        print('105')