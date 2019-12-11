from object import *
from status_condition import *
from sound_manager import *

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

class WaitState:

    @staticmethod
    def enter(hero):
        pass

    @staticmethod
    def do(hero):
        pass

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
        return self.cur_state == BattleState or self.cur_state == WaitState

    def set_in_battle(self):
        self.event_que.append(BattleState)

    def add_position_x(self, value):
        self.x += value

    def add_event(self, event):
        self.event_que.append(event)



class HeroStatus:
    hp = 24
    maxhp = 24  # 24 = 6 28 = 5.5 32 = 5
    pivot = 6
    shield = 0
    background_image = None
    img = None
    enemy_type = None
    equip_item = []
    max_dice = 3
    status_condition = StatusCondition()

    def __init__(self):
        if HeroStatus.background_image is None and HeroStatus.img is None:
            HeroStatus.background_image = pico2d.load_image("../Resources/common/hpbarback.png")
            HeroStatus.img = pico2d.load_image("../Resources/common/hpbar.png")

            HeroStatus.equip_item.append("baseattack")
            HeroStatus.equip_item.append("ironshield")
            HeroStatus.equip_item.append("reloaddice")

    @staticmethod
    def get_hp():
        return HeroStatus.hp

    @staticmethod
    def get_condition():
        return HeroStatus.status_condition

    @staticmethod
    def set_hp(hp):
        HeroStatus.hp = hp

    @staticmethod
    def set_maxhp(hp):
        HeroStatus.maxhp = hp
        HeroStatus.pivot -= 0.5

    @staticmethod
    def get_maxhp():
        return HeroStatus.maxhp

    @staticmethod
    def draw(x, y):
        HeroStatus.background_image.draw(x, y)
        HeroStatus.img.draw(x - int((HeroStatus.maxhp - HeroStatus.hp) * HeroStatus.pivot), y, \
                            HeroStatus.img.w - (int((HeroStatus.img.w / HeroStatus.maxhp) * (HeroStatus.maxhp - HeroStatus.hp))), \
                            HeroStatus.img.h)

    @staticmethod
    def add_hp(value):
        HeroStatus.hp += value
        if HeroStatus.hp > HeroStatus.maxhp:
            HeroStatus.hp = HeroStatus.maxhp

    @staticmethod
    def add_shield(value):
        HeroStatus.shield += value
        if HeroStatus.shield > 10:
            HeroStatus.shield = 10

    @staticmethod
    def min_shield(value):
        if value > 3:
            SoundManager.play_sound("thdamage", False)

        elif value > 1 and value < 4:
            SoundManager.play_sound("tbdamage", False)

        HeroStatus.shield -= value
        if HeroStatus.shield < 0:
            count = HeroStatus.shield
            HeroStatus.shield = 0
            return -count
        return 0

    @staticmethod
    def set_enemy_type(enemytype):
        HeroStatus.enemy_type = enemytype

    @staticmethod
    def push_equip_item(item):
        HeroStatus.equip_item.append(item)
        HeroStatus.equip_item.pop(0)
