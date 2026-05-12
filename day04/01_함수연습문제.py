# 1.
# def text_join(*args, sep=" ") :
#     result = args[0] # apple
#     for t in args[1:] :
#         result += (sep + t) # apple-banana
#     return result

# *간단한 밥법 : 문자열의 join 함수! -> sep으로 args를 이어줌
def text_join(*args, sep=" ") :
    return sep.join(args)

print(text_join("apple", "banana", "kiwi", "orange", sep="-"))
# apple-banana-kiwi-orange 출력
print(text_join("Python", "Java", "C++"))
# Python Java C++ 출력


# 2. mode 디폴트는 없음! : 빈값 or None
# 함수 sort()는 원본에 영향을 줌. 
# sorted()는 원본은 그대로 두고 새로운 리스트 만들어서 반환(return)
# def list_tool(*nums, mode=None) :
#     if mode == "reverse" :
#         nums.sort(reverse=True)
#     elif mode == "sum" :
#         return sum(nums)
#     else :
#         nums.sort()
#     return nums

# list_tool([3, 1, 7, 2, 9])  
# # [1, 2, 3, 7, 9] 출력
# list_tool([3, 1, 7, 2, 9], mode="reverse")  
# # [9, 7, 2, 1, 3] 출력
# list_tool([3, 1, 7, 2, 9], mode="sum")  
# # 22 출력

# sorted() 활용
# def list_tool2(nums, mode=None) :
#     if mode == "reverse" :
#         return sorted(nums, reverse=True)
#     elif mode == "sum" :
#         return sum(nums)
#     else :
#         return sorted(nums)

# num_list = [3, 1, 7, 2, 9]
# print(list_tool2(num_list))
# print(list_tool2(num_list, mode="reverse"))
# print(list_tool2(num_list, mode="sum"))
# print(num_list) # sorted 덕분에 원본 영향 없음!


# 3.
def dict_pick(data, option="max") :
    if option == "max" :
        key_ = max(data, key=data.get)
    else :
        key_ = min(data, key=data.get)
    return {key_ : data[key_]}

print(dict_pick({"apple": 3, "banana": 5, "kiwi": 2}))
# {'banana': 5} 출력
print(dict_pick({"apple": 3, "banana": 5, "kiwi": 2}, option="min"))
# {'kiwi': 2} 출력

# 4.
items = {"pen": 10, "note": 5}

def inventory(items, item, count) :
    if item in items :
        items[item] += count
    else : 
        items[item] = count
        
inventory(items, "pen", 3)
print(items)
# {'pen': 13, 'note': 5} 출력
inventory(items, "note", -2)  
print(items)
# {'pen': 10, 'note': 3} 출력
inventory(items, "colored pencil", 5) 
print(items) 
# {'pen': 10, 'note': 3, 'colored pencil' : 5} 출력