# 학번, 이름, 학과, 학년(디폴트:1)
class Student :
    def __init__(self, stu_no, stu_name, stu_dept, stu_grade=1) :
        self.__stu_no = stu_no
        self.__stu_name = stu_name
        self.__stu_dept = stu_dept
        self.__stu_grade = stu_grade
    
# __stu_grade를 기준으로 get, set 메소드 만들기
# grade의 값은 1부터 4까지만 허용. 그 외 값은
# '1부터 4까지만 가능합니다' 출력 후 저장은 X
# set_stu_grade, get_stu_grade

    def set__stu_grade(self,stu_grade) :
        if 1 > stu_grade > 4 :
            print("1부터 4까지 가능합니다")
        else :
            self.__stu_grade = stu_grade
    def get__stu_grade(self) :
        return self.__stu_grade
    
hong = Student("1234", "홍길동", "컴퓨터")
print(hong.__dict__)
# {'_Student__stu_no': '1234', '_Student__stu_name': '홍길동', 
# '_Student__stu_dept': '컴퓨터', '_Student__stu_grade': 1}
hong.__stu_grade = 2
print(hong.__dict__)
# {..., '__stu_grade': 2}
print(hong.__stu_grade)