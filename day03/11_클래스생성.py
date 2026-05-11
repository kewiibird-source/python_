# 클래스 생성 예제!

class Television :
    def __init__(self, channer, volume, on) :
        self.channer = channer
        self.volume = volume
        self.on = on
    def show(self) :
        print(self.channer,self.volume,self.on)
    def setChannel(self, channer) :
        self.channer = channer
    def getChanner(self) :
        return self.channer
    
tv = Television(10, 15, True)
tv.show() # 결과 : 10 15 True
tv.setChannel(12) # 결과 : channel값이 12로 변경
tv.getChanner() # 결과 : channel에 있는 값 리턴
tv.show()