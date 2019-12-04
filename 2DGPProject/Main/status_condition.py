# 상태이상에 대한 내용을 작성합니다.


class ConditionPoison:  # 독 상태이상
    def __init__(self, count):
        self.count = count

    def add_count(self, value):
        self.count += value

    def min_count(self, value):
        self.count -= value

    def active(self, obj):
        obj.sethp(obj.gethp()-1)
        self.min_count(-1)

    def get_count(self):
        return self.count


class StatusCondition:
    def __init__(self):
        self.condition_list = []        # 전투 오브젝트들이 현재 턴에 가진 상태이상

    def active_condition(self, obj):
        for i in self.condition_list:
            i.active(obj)
