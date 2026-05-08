# 딕셔너리
menu = {"김밥" : 3000, "라면" : 5000}
print(menu['김밥'])

#직접 접근해서 값 변경하기
menu['라면'] = 6000 
print(menu['라면'])

# 값 추가하기
menu['떡볶이'] = 100000 
print(menu)

# 키값이 뭐가 들었는지 확인
print(menu.keys())
print(menu.values())
print(menu.items()) # 튜플의 형태로 나옴 (수정X)

# dict_keys(['김밥', '라면', '떡볶이'])
# dict_values([3000, 6000, 100000])
# dict_items([('김밥', 3000), ('라면', 6000), ('떡볶이', 100000)]) 