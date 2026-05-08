# 튜플
tuple = (1, "홍길동", True, [2,3,4])
print(tuple)
print(tuple[1]) # index 1번째
print(tuple[-1]) # index 뒤에서 0번째
print(tuple[1:]) # index 1부터 끝까지
# print(tuple[4]) 에러(4번째 인덱스 없음)

# tuple[0] = 100 # tuple은 수정이 불가능!, 선언할때의 값이 유지됨.
print(tuple)