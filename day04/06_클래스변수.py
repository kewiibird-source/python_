class Student :
    auto_increment = 0
    
    @classmethod
    def change_num(cls, num) : #self -> cls
        cls.auto_increment = num
    
    def __init__(self, name, dept):
        Student.auto_increment += 1
        self.__stu_no = Student.auto_increment
        self.__stu_name = name
        self.__stu_dept = dept
    def get_stu_no(self) :
        return self.__stu_no
    
hong = Student("홍길동", "컴퓨터")
kim = Student("김철수", "기계")
park = Student("박영희", "디자인")

print(f"홍길동 학번 : {hong.get_stu_no()}")
print(f"김철수 학번 : {kim.get_stu_no()}")
print(f"박영희 학번 : {park.get_stu_no()}")

Student.auto_increment = 100
# auto_increment에 직접적으로 접근하고 싶다면 클래스명으로 접근. (이것도 바람직한 방법은 아님)
# hong.auto_increment = 100 
# auto_increment에 직접 접근한게 아닌 auto_increment라는 새로운 변수를 만들어서 추가한거임!!
print(hong.__dict__)
print(kim.auto_increment)

kewi = Student("키위새", "호텔경영")
print(kewi.__dict__)