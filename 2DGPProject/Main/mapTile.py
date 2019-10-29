class tile:
    def __init__(self, ID,  x, y): # 현재 tile이 만들어질 장소와 ID
        self.x = x
        self.y = y
        self.id = ID
    def setRule(self, *args): # 자신과 연결 된 타일들의 정보
        self.Rule = []
        for i in args:
            self.Rule.append((i.getInfo()))
    def getInfo(self):
        return self.x,self.y,self.id


if __name__ == "__name__":
    print("Module")
    exit(1)