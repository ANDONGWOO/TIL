#주어진 리스트 numbers에서 최소값을 구하여 출력하시오
#min()  함수 사용금지

numbers = [0, 20, 100]

a = numbers[0]

for i in numbers:
    if a > i:
       a = i          
print(a)