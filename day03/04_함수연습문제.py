# 1. 문자열 거꾸로 출력

def reverse_func(*values) :
    for v in values :
        print(v[::-1], end = " ")

reverse_func("java", "python", "html", "css")

## print(word[::-1]) # 거꾸로 출력
# avaj nohtyp lmth ssc 

# 2. 짝수, 홀수의 합

def num_sum(*numbers, option="even") :
    odd_sum = 0
    even_sum = 0
    for a in numbers :
        if a % 2 == 0 :
            even_sum += a
        else :
            odd_sum += a
    if option == "even" :
        print(f"짝수의 합 = {even_sum}")
    elif option == "odd" :
        print(f"홀수의 합 = {odd_sum}")
    else :
        print("옵션 다시 확인하셈")
        
print()
num_sum(1,3,2,4,5,7,1) # 짝수의 합 출력
num_sum(1,3,2,4,5,7,1, option="odd") # 홀수의 합 출력
# 짝수의 합 = 6
# 홀수의 합 = 17

# 3. 큰숫자 작은숫자

def num_pick(*num, option="max") :
    if option == "max" :
        print(f"가장 큰 숫자는 : {max(num)}")
    elif option == "min" :
        print(f"가장 작은 숫자는 : {min(num)}")
    else :
        print("옵션 다시 확인하셈")
        
num_pick(3,7,1,9,4,2,10,19) # 가장 큰 수 출력
num_pick(3,7,1,9,4, option="min") # 가장 작은 수 출력
# 가장 큰 숫자는 : 19
# 가장 작은 숫자는 : 1

# 4. 중복 제거

def dedupe(*num) :
    return list(set(num))

num_list = dedupe(1,3,5,2,4,1,2,3) # 중복 제거된 결과(리스트) 리턴
print(num_list) # [1,3,5,2,4] 

# 5.

def union_list(list1, list2, *list3) :
    result = set(list1) | set(list2) | set(list3)
    return list(result)

list1 = [1,4,2,9,10,3]
list2 = [3,5,9,2,8]
# 결과로 list1, list2, 숫자들(3,5,20,9,15,7)의 중복없는 결과(리스트) 리턴

print(union_list(list1, list2, 3,5,20,9,15,7))
# [1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 20]

# 6. 랜덤한 숫자
## print(random.randint(1, 10)) # 랜덤한숫자 1 - 10 사이

import random
def ran_list(cnt, start=1, end=50) :
    result = []
    while len(result) < cnt :
        ran = random.randint(start, end)
        if ran not in result :
            result.append(ran)
    return result

# 10부터 45숫자 중 6개 중복없는 숫자 리스트 반환 (정렬까지)
result1 = ran_list(6, start=10, end=45)
result1.sort()
print(result1)
# [11, 16, 26, 27, 31, 34]

# 1부터 100숫자 중 5개 중복없는 숫자 리스트 반환
print(ran_list(5, end=100))
# [73, 5, 89, 29, 36]

# 1부터 50숫자 중 10개 중복없는 숫자 리스트 반환
print(ran_list(10))
# [13, 7, 44, 39, 35, 24, 29, 1, 5, 27]

# 7. 문자열도 순차적으로 접근할 수 있다

def str_num_sum(num) :
    sum = 0
    for a in str(num) :
        sum += int(a)
    return sum

print(str_num_sum(1352)) # 각 숫자를 한자리씩 구분한 후 더하기 -> 11
print(str_num_sum(209479)) # 31