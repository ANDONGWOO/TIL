import sys
sys.stdin = open("31306.txt", "r")

def count_vowels(w):
    s1 = sum(1 for i in w if i in 'aeiou')
    s2 = sum(1 for i in w if i in 'aeiouy')
    return s1, s2


q = input().strip()

s = count_vowels(q)
print(s[0], s[1])