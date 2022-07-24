#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오
#max()  함수 사용금지
# 중복제거
# 정렬 적용?
#
numbers = [0, 20, 100, 50, -60, 50, 100]

new_list = []
a = new_list[0]
for v in numbers:
    if v not in new_list:
        new_list.append(v)
    
         
print(new_list)