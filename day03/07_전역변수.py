# 전역변수 수정은? global
# 권장하진 않음!
num = 10

def test() :
    global num
    num += 5
    print(num)
    
test()