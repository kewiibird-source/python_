# 숫자 3개를 입력받아서 리스트에 저장한 후 평균구하기
num_list = []
num_list.append(int(input("첫번째 숫자 : ")))
num_list.append(int(input("두번째 숫자 : ")))
num_list.append(int(input("세번째 숫자 : ")))
print(num_list)
avg = sum(num_list) / len(num_list)
print(f"평균 : {avg}")
# sum_ = num_list[0] + num_list[1] + num_list[2]
# avg = sum_ / len(num_list)

    

