list = [1,5,9,2,6]

# list.sort() #오름차순
# list.sort(reverse=True) #내림차순
print(list)

# pop
print("꺼낸 값 => ", list.pop()) # 인자값 안넣으면 맨 뒤에 값
print(list)
print("꺼낸 값 => ", list.pop(2)) # 인자값에 맞는 인덱스 값
print(list)

#remove
print("꺼낸 값 => ", list.remove(5)) # 리턴 없음! list 안에 있는 값
print(list)

# list의 크기 (이거말고 다른거사용함)
print(len(list))