from student import Student
student_dict = {}

# 1. 학번, 이름, 학과를 입력받아서 student_add에 저장
# 저장 방법은 {"학번" : Student객체}
def student_add() :
    stu_no = input("학번 : ")
    name = input("이름 : ")
    dept = input("학과 : ")
    s = Student(stu_no, name, dept)
    student_dict[stu_no] = s
    print(student_dict)
    
# 2. 학번 입력 > 있으면 학번 수정 > 없으면 '없는학생' 출력후 메뉴로 
def student_grade_update() :
    stu_no = input("학번 : ")
    if stu_no in student_dict :
        s = student_dict[stu_no]
        grade = int(input("학번 : "))
        s.set__stu_grade(grade)
    else :
        print("해당 학번 없음")

# 3. 학번입력 > 있으면 학번,이름,학과,학년 출력 > 없으면 '없는학생' 출력후 메뉴로
def student_search() :
    stu_no = input("학번 : ")
    if stu_no in student_dict :
        s = student_dict[stu_no]
        print(f"학번 : {stu_no}, 이름 : {s.get__stu_name()}, 학과 : {s.get__stu_dept()}, 학년 : {s.get__stu_grade()}")
    else :
        print("해당 학생 없음")

while True :
    menu = input("[(1) 학생추가 (2) 학년수정 (3) 학생조회 (4) (5) 종료 ]")
    if menu == "1" :
        student_add()
    elif menu == "2" :
        student_grade_update()
    elif menu == "3" :
        student_search()
    elif menu == "4" :
        pass
    else : 
        break    

# hong = Student("1234", "홍길동", "컴퓨터")
# print(hong.get__stu_grade())

# test = []
# test.append(hong)
# print(test)