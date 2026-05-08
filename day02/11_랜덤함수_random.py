import random

print(random.random())
print(random.randint(1, 10)) # 랜덤한숫자 1 - 10 사이

fruits = ["사과", "오렌지", "바나나", "키위", "수박"]
print(random.choice(fruits)) # 리스트에서 랜덤!
print(random.sample(fruits, 2)) # 리스트에서 랜덤하게 2개

print(f"셔플 전 => {fruits}")
random.shuffle(fruits)
print(f"셔플 후 => {fruits}")