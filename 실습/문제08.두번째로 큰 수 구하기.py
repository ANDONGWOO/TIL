#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오
#max()  함수 사용금지
# 중복제거
# 정렬 적용?

numbers =  [0, 20, 100]

a= set(numbers)
b= list(a)
b.sort()
print (b[-2])