# 상태이상에 대한 내용을 작성합니다.


class ConditionPoison:  # 독 상태이상

    def __init__(self, count):
        self.count = count

    def add_count(self, value):
        self.count += value

    def min_count(self, value):
        self.count -= value

    def active(self, obj):
        obj.add_hp(-obj.min_shield(self.count))
        self.min_count(1)

    def get_count(self):
        return self.count

    @staticmethod
    def get_type():
        return ConditionPoison


class ConditionFrozen:  # 빙결 상태이상

    def __init__(self, count):
        self.count = count

    def add_count(self, value):
        self.count += value

    def min_count(self, value):
        self.count -= value

    def active(self, obj):
        obj.max_dice -= 1
        self.min_count(1)

    def get_count(self):
        return self.count

    @staticmethod
    def get_type():
        return ConditionFrozen


STATUS_CONDITION = {ConditionPoison: "독", ConditionFrozen: "빙결"}
STATUS_CONDITION_NAME = {"독": ConditionPoison, "빙결": ConditionFrozen}


class StatusCondition:

    def __init__(self):
        self.condition_list = []        # 전투 오브젝트들이 현재 턴에 가진 상태이상

    def active_condition(self, obj):
        for i in range(len(self.condition_list)):
            self.condition_list[i].active(obj)
            if self.condition_list[i].get_count() == 0:
                self.condition_list.pop(i)

    def add_condition(self, condition, count):
        for i in self.condition_list:
            if STATUS_CONDITION_NAME[condition] == i.get_type():
                i.add_count(count)
                return None

        self.condition_list.append(STATUS_CONDITION_NAME[condition](count))

    def get_condition_list(self):
        return self.condition_list

    def get_condition_to_idx(self, idx):
        return self.condition_list[idx]

    def clear_condition(self):
        self.condition_list.clear()

