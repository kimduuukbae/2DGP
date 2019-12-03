from object import *
import game_framework
import main_state
import banner
import winsound


class IdleState:
    @staticmethod
    def enter(monster):
        pass

    @staticmethod
    def do(monster):
        monster.frameTime += game_framework.frame_time
        if monster.frameTime > 1.0:
            monster.frame = (monster.frame + 1) % 2
            monster.frameTime = 0.0

    @staticmethod
    def exit():
        pass


class BattleState:
    count = 0

    @staticmethod
    def enter(monster):
        BattleState.count = 0

    @staticmethod
    def do(monster):
        monster.frameTime += game_framework.frame_time
        if monster.frameTime > 1.0:
            monster.frame = (monster.frame + 1) % 2
            monster.frameTime = 0.0
        monster.x += 3
        BattleState.count += 2
        if BattleState.count > 100:
            monster.event_que.append(ExitState)

    @staticmethod
    def exit():
        pass


class ExitState:
    count = 0

    @staticmethod
    def enter(monster):
        ExitState.count = 0

    @staticmethod
    def do(monster):
        monster.frameTime += game_framework.frame_time
        if monster.frameTime > 1.0:
            monster.frame = (monster.frame + 1) % 2
            monster.frameTime = 0.0
        monster.x -= 3
        ExitState.count += 2
        if ExitState.count > 20:
            main_state.stage_collection.cur_stage.banner_list.append(banner.BattleBanner())
            winsound.PlaySound('../Resources/stage/fightfxSound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                               winsound.SND_ASYNC)
            monster.event_que.append(WaitState)

    @staticmethod
    def exit():
        pass


class WaitState:
    @staticmethod
    def enter(monster):
        pass

    @staticmethod
    def do(monster):
        pass

    @staticmethod
    def exit():
        pass


class Monster_in_menu(Object):
    def __init__(self, name):
        super().__init__(None)
        self.name = name
        self.frame = 0
        self.frameTime = 0.0
        self.type = 1
        self.cur_state = IdleState
        self.event_que = []

    def draw(self):
        self.image.clip_draw(self.clipWidth*self.frame, 0, self.clipWidth, self.clipHeight,
                             self.x + self.pivotX, self.y + self.pivotY, self.imageWidth/2, self.imageHeight)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit()
            self.cur_state = event
            self.cur_state.enter(self)

    def get_in_battle(self):
        return self.cur_state != IdleState

    def set_in_battle(self):
        if self.cur_state is IdleState:
            self.event_que.append(BattleState)

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def push_event(self, state):
        self.event_que.append(state)

    def set_id(self, value):
        self.id = value


class Slime(Monster_in_menu):
    def __init__(self):
        super().__init__("슬라임")
        self.image = pico2d.load_image("../Resources/stage/slimeStage.png")
        self.imageWidth = self.image.w
        self.imageHeight = self.image.h
        self.clipWidth = self.imageWidth // 2
        self.clipHeight = self.imageHeight
        self.id = 8
        self.pivotX = 0
        self.pivotY = 70


class Door(Monster_in_menu):
    def __init__(self):
        super().__init__("문")
        self.image = pico2d.load_image('../Resources/stage/door.png')
        self.imageWidth = self.image.w
        self.imageHeight= self.image.h
        self.clipWidth = self.imageWidth // 2
        self.clipHeight = self.imageHeight
        self.pivotX = 0
        self.pivotY = 40
        self.id = 6
        self.type = 2


class BabySquid(Monster_in_menu):
    def __init__(self):
        super().__init__("새끼오징어")
        self.image = pico2d.load_image("../Resources/stage/babysquidStage.png")
        self.imageWidth = self.image.w
        self.imageHeight = self.image.h
        self.clipWidth = self.imageWidth // 2
        self.clipHeight = self.imageHeight
        self.id = 8
        self.pivotX = 0
        self.pivotY = 70


