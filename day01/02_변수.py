age = 20
name = '홍길동'
height = 170.5
hobbyList = ['게임', '운동', '코딩']

# print는 오버로딩 된 애다 라는걸 알 수 있음
# end = "\n" 프린트문이 끝날떄 end가 붙음 (줄바꿈이 디폴트)
print("이름 : " , name, end = "\n") # 디폴트
print("나이 : " , age)

# sep 구분자 변수 사이사이에 붙음
print(name, age, height, sep="/")
