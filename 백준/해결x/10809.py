import sys
sys.stdin = open("10809.txt", "r")


s=list(input())

for i in range(len(s)):
    v=[]#값
    if 'a'in s:
        v.append(s.index('a'))#a
    if 'a'not in s:
        v.append('-1')#a
    if 'b'in s:
        v.append(s.index('b'))#b
    if 'b'not in s:
        v.append('-1')#b
    if 'c'in s:
        v.append(s.index('b'))#c
    if 'c'not in s:
        v.append('-1')#c
    if 'd'in s:
        v.append(s.index('b'))#d
    if 'd'not in s:
        v.append('-1')#d
    if 'e'in s:
        v.append(s.index('e'))#e
    if 'e'not in s:
        v.append('-1')#e
    if 'f'in s:
        v.append(s.index('f'))#f
    if 'f'not in s:
        v.append('-1')#f
    if 'g'in s:
        v.append(s.index('g'))#g
    if 'g'not in s:
        v.append('-1')#g
    if 'h'in s:
        v.append(s.index('h'))#h
    if 'h'not in s:
        v.append('-1')#h
    if 'i'in s:
        v.append(s.index('i'))#i
    if 'i'not in s:
        v.append('-1')#i
    if 'j'in s:
        v.append(s.index('j'))#j
    if 'j'not in s:
        v.append('-1')#j
    if 'k'in s:
        v.append(s.index('k'))#k
    if 'k'not in s:
        v.append('-1')#k
    if 'l'in s:
        v.append(s.index('l'))#l
    if 'l'not in s:
        v.append('-1')#l
    if 'm'in s:
        v.append(s.index('m'))#m
    if 'm'not in s:
        v.append('-1')#m
    if 'n'in s:
        v.append(s.index('n'))#n
    if 'n'not in s:
        v.append('-1')#n
    if 'o'in s:
        v.append(s.index('o'))#o
    if 'o'not in s:
        v.append('-1')#o
    if 'p'in s:
        v.append(s.index('p'))#p
    if 'p'not in s:
        v.append('-1')#p
    if 'q'in s:
        v.append(s.index('q'))#q
    if 'q'not in s:
        v.append('-1')#q
    if 'r'in s:
        v.append(s.index('r'))#r
    if 'r'not in s:
        v.append('-1')#r
    if 's'in s:
        v.append(s.index('s'))#s
    if 's'not in s:
        v.append('-1')#s
    if 't'in s:
        v.append(s.index('t'))#t
    if 't'not in s:
        v.append('-1')#t
    if 'u'in s:
        v.append(s.index('u'))#u
    if 'u'not in s:
        v.append('-1')#u
    if 'v'in s:
        v.append(s.index('v'))#v
    if 'v'not in s:
        v.append('-1')#v
    if 'w'in s:
        v.append(s.index('w'))#w
    if 'w'not in s:
        v.append('-1')#w
    if 'x'in s:
        v.append(s.index('x'))#x
    if 'x'not in s:
        v.append('-1')#x
    if 'y'in s:
        v.append(s.index('y'))#y
    if 'y'not in s:
        v.append('-1')#y
    if 'z'in s:
        v.append(s.index('z'))#z
    if 'z'not in s:
        v.append('-1')
print(*v)