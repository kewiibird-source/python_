# 학생 2명의 이름과 점수를 입력받아서 리스트에 저장
# 리스트를 활용해

names = []
scores = []

names.append(input("이름을 입력하세요 : "))
scores.append(int(input("점수를 입력하세요 : ")))

names.append(input("이름을 입력하세요 : "))
scores.append(int(input("점수를 입력하세요 : ")))

grade = {
    names[0] : scores[0],
    names[1] : scores[1]    
}

name = input("검색할 학생 이름 : ")
if name in grade :
    print(f"{name} 학생의 점수는 {grade[name]}점 입니다.")
else :
    print("등록되지 않은 학생입니다.")