#주어진 리스트의 요소 중에서 5의 개수를 출력하시오


numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

exoneration=5

rotation=0
for char in numbers:

        if char==exoneration:
            rotation += 1
            
print(rotation)