human = {"홍길동" : 170, "김철수" : 185, "김영희" : 165}
# 딕셔너리에서 가장 큰 키를 찾아라
print(max(human.values())) # 185

# 벨류값 가져오기
# human["홍길동"]
# human.get("홍길동")

# 딕셔너리에서 가장 큰 키의 키값은?
name = max(human, key=human.get)
print(name)