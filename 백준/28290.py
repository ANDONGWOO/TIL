import sys

sys.stdin = open("28290.txt", "r")

s=input()
if s=='fdsajkl;' or s=='jkl;fdsa':
    print("in-out")
elif s=='asdf;lkj' or s==';lkjasdf':
    print("out-in")
elif s=='asdfjkl;':
    print("stairs")
elif s==";lkjfdsa":
    print("reverse")
else:#위에 해당x  
    print("molu")

