# start가 end보다 더 크면 '시작 숫자가 더 큽니다.' 출력후
# 두 숫자를 다시 입력 받을 수 있도록

# start = int(input("시작 : "))
# end = int(input("끝 : "))
# while end < start :
#     print("시작 숫자가 더 큽니다." )
#     start = int(input("시작 : "))
#     end = int(input("끝 : "))

# sum = 0
# for a in range(start, end+1) :
#     sum += a
# print(f"합 : {sum}")


while True :
    start = int(input("시작 : "))
    end = int(input("끝 : "))
    if end < start :
        print("시작 > 끝 !! 다시 입력하셈")
        continue
    sum = 0
    for a in range(start, end+1) :
        sum += a
    print(f"합 : {sum}")
    break