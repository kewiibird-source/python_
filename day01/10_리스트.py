# 파이썬의 리스트에는 다 들어간다.
list = [1, "홍길동", True, [2,3,4]]
print(list)
print(list[1]) # index 1번째
print(list[-1]) # index 뒤에서 0번째
print(list[1:]) # index 1부터 끝까지
# print(list[4]) 에러(4번째 인덱스 없음)

list[0] = 100 # list의 0번째(1)를 100으로 변경
print(list)
list[1:3] = ["메롱",False] # 슬라이스 활용
print(list)