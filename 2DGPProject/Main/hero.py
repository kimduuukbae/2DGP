from object import *
import pico2d
import item

class IdleState:

    @staticmethod
    def enter(hero):
        pass

    @staticmethod
    def do(hero):
        pass


class WalkState:

    @staticmethod
    def enter(hero):
        pass

    @staticmethod
    def do(hero):
            hero.x += hero.distanceX
            hero.y += hero.distanceY
            hero.count += 1
            if hero.count == 100:
                hero.count = 0
                hero.id = hero.moveLists[0][2]
                hero.moveLists.pop(0)
                hero.cur_state = IdleState
                if len(hero.moveLists):
                    hero.move_to_tile(hero.moveLists)

class BattleState:
    count = 0
    @staticmethod
    def enter(hero):
        BattleState.count = 0

    @staticmethod
    def do(hero):
        hero.x -= 3
        BattleState.count += 2
        if BattleState.count > 100:
            hero.event_que.append(ExitState)


class ExitState:
    count = 0

    @staticmethod
    def enter(hero):
        ExitState.count = 0

    @staticmethod
    def do(hero):
        hero.x += 3
        ExitState.count += 2
        if ExitState.count > 20:
            hero.event_que.append(IdleState)

class Hero(Object):
    def __init__(self, image_name = None):
        super().__init__(image_name)
        self.id = 1
        self.name = "전사"
        self.toX = 0
        self.toY = 0
        self.distanceX = 0
        self.distanceY = 0
        self.count = 0
        self.moveLists = []

        self.cur_state = IdleState
        self.event_que = []

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state = event
            self.cur_state.enter(self)

    def get_id(self):
        return self.id

    def move_to_tile(self, lists):
        if self.cur_state is IdleState:
            self.moveLists = lists
            self.toX = self.moveLists[0][0]
            self.toY = self.moveLists[0][1]
            self.distanceX = (self.toX - self.x) / 100
            self.distanceY = (self.toY - self.y) / 100
            self.cur_state = WalkState

    def get_moving(self):
        return self.cur_state == WalkState

    def get_in_battle(self):
        return self.cur_state == BattleState

    def set_in_battle(self):
        self.event_que.append(BattleState)

    def add_position_x(self, value):
        self.x += value


class Hero_status:
    hp = 24
    maxhp = 24  # 24 = 6 28 = 5.5 32 = 5
    pivot = 6
    shield = 0
    background_image = None
    img = None
    enemy_type = None
    equip_item = []

    def __init__(self):
        if Hero_status.background_image is None and Hero_status.img is None:
            Hero_status.background_image = pico2d.load_image("../Resources/common/hpbarback.png")
            Hero_status.img = pico2d.load_image("../Resources/common/hpbar.png")

            Hero_status.equip_item.append("baseattack")
            Hero_status.equip_item.append("ironshield")
            Hero_status.equip_item.append("reloaddice")

    @staticmethod
    def get_hp():
        return Hero_status.hp

    @staticmethod
    def set_hp(hp):
        Hero_status.hp = hp

    @staticmethod
    def set_maxhp(hp):
        Hero_status.maxhp = hp
        Hero_status.pivot -= 0.5

    @staticmethod
    def get_maxhp():
        return Hero_status.maxhp

    @staticmethod
    def draw(x, y):
        Hero_status.background_image.draw(x, y)
        Hero_status.img.draw(x - int((Hero_status.maxhp - Hero_status.hp) * Hero_status.pivot), y, \
                             Hero_status.img.w - (int((Hero_status.img.w / Hero_status.maxhp) * (Hero_status.maxhp - Hero_status.hp))), \
                             Hero_status.img.h)

    @staticmethod
    def add_hp(value):
        Hero_status.hp += value

    @staticmethod
    def add_shield(value):
        Hero_status.shield += value

    @staticmethod
    def set_enemy_type(enemytype):
        Hero_status.enemy_type = enemytype

    @staticmethod
    def push_equip_item(item_name):
        Hero_status.equip_item.append(item.itemfactory(item_name))
        Hero_status.equip_item.pop(0)

