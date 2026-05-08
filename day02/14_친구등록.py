# 1) 친구 등록 2) 검색 그 외) 종료 : 1
# 이름 : 키위
# 번호 : 123
# 1) 친구 등록 2) 검색 그 외) 종료 : 2
# 이름 : 키위
# 키위의 번호는 123입니다
user = {}
while True :
    menu = int(input("1) 친구 등록 2) 검색 그 외) 종료 : "))
    if menu == 1 :
        name = input("이름 : ")
        phone = input("번호 : ")
        user[name] = phone
        continue
    elif menu == 2 :
        name = input("이름 : ")
        if name in user :
            print(f"{name}의 번호는 {user[name]}입니다")
        else :
            print("해당 이름 없음")
    else :
        print("종료!")
        break
    
# {"철수" : "1234", "철수" : "1234", "철수" : "1234"}
# [
#   {name : "철수", addr : "인천", phone : "1234"}
#   {name : "키위", addr : "인천", phone : "1234"}
#]