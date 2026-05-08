num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))

print(f"첫번째 숫자는 {num1}")
print(f"두번째 숫자는 {num2}")

# d는 정수 2는 자릿수
# 첫번째 숫자는  3
# 두번째 숫자는 15
print(f"첫번째 숫자는 {num1:2d}")
print(f"두번째 숫자는 {num2:2d}")

# d는 정수 2는 자릿수 0은 자릿수에따라 빈공간 0으로
# 첫번째 숫자는 03
# 두번째 숫자는 15
print(f"첫번째 숫자는 {num1:02d}")
print(f"두번째 숫자는 {num2:02d}")

price = 10000000
print(f"{price:,d}원")
# 10,000,000원