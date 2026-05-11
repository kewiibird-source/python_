class Counter :
    def __init__(self, v=0) :
        self.count = v
    def increment(self) :
        self.count += 1

c1 = Counter(); print(c1.count) # 0
c2 = Counter(100); print(c2.count) # 100

