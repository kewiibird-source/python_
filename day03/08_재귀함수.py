# 팩토리얼 
# 5! => 5 * 4 * 3 * 2 * 1
# 무한루프가 되기 때문에 빠져나가는 조건이 중요함!

def factor(x) :
    if x == 1 :
        return 1
    else : 
        return x * factor(x-1) # 5 * 4 * 3 * 2 * 1

print(factor(5))