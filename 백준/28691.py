import sys

sys.stdin = open("28691.txt", "r")

s={"M":"MatKor","W":"WiCys","C":"CyKor","A":"AlKor","$":"$clear"}
q=input()
if q in s:
    print(s[q])#key 사용 value얻기