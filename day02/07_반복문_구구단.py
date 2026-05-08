# 입력한 숫자의 구구단을 출력
# 3입력 시 3단 출력

# dan = int(input("숫자를 입력하세요 : "))
# for a in range(1, 10) :
#     print(f"{dan} * {a} = {dan*a}")
    
    
# 2~9단까지 모두 출력
for i in range(2, 10) : 
    print(f'========{i}단=========')
    for a in range(1, 10) :
        print(f"{i} * {a} = {i*a}")
        