# 딕셔너리로 저장후 과일 이름을 입력받아 가격을 출력
# 없는 과일이면 "판매하지 않는 상품입니다"
fruit = {"사과" : 1000, "바나나" : 1500, "딸기" : 2000}
name = input("과일을 입력 하세요 : ")

if name in fruit :
    print(f"{fruit[name]}원")
else :
    print("판매하지 않는 상품입니다")
    

