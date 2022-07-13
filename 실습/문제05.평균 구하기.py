#주어진 숫자의 평균을  구하는 코드를 작성하시오
#sum(), len() 함수 사용금지
numbers = [3, 10, 20]

total = 0

rotation=0

for i in numbers:
    total += i
    rotation +=1
print(total/rotation)
