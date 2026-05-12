class Student :
    def __init__(self, stu_no, stu_name, stu_dept, stu_grade=1) :
        self.__stu_no = stu_no
        self.__stu_name = stu_name
        self.__stu_dept = stu_dept
        self.__stu_grade = stu_grade
        self.__subject = []
    def set__stu_grade(self,stu_grade) :
        if 1 > stu_grade > 4 :
            print("1부터 4까지 가능합니다")
        else :
            self.__stu_grade = stu_grade
    def get__stu_grade(self) :
        return self.__stu_grade
    def get__stu_name(self) :
        return self.__stu_name
    def get__stu_dept(self) :
        return self.__stu_dept
    def get__stu_no(self) :
        return self.__stu_no
    