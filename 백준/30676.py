import sys
sys.stdin = open("30676.txt", "r")

s=int(input())

if 620<=s and s<=780:
    print("Red")
elif 590<=s and s<620:
    print("Orange")
elif 570<=s and s<590:
    print("Yellow")
elif 495<=s and s<570:
    print("Green")
elif 450<=s and s<495:
    print("Blue")
elif 425<=s and s<450:
    print("Indigo")
elif 380<=s and s<425:
    print("Violet")