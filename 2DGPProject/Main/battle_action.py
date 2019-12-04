import hero
import monster_in_battle
from item import *
from dice import *


class EnemyTurn:
    dice = Dice_manager(0)

    item = item_manager("monster")

    @staticmethod
    def enter(obj):
        EnemyTurn.item.push_item_list(monster_in_battle.Monsterstatus.item_list)
        EnemyTurn.dice.push_dice_monster(3)
        pass

    @staticmethod
    def update(obj):
        EnemyTurn.item.update()
        EnemyTurn.dice.update()

    @staticmethod
    def draw(obj):
        EnemyTurn.item.draw()
        EnemyTurn.dice.draw()

    @staticmethod
    def exit(obj):
        EnemyTurn.dice.dice_clear()
        EnemyTurn.item.item_clear()
        pass


class HeroTurn:
    dice = Dice_manager(0)
    item = item_manager("hero")

    @staticmethod
    def enter(obj):
        HeroTurn.item.push_item_list(hero.HeroStatus.equip_item)
        HeroTurn.dice.push_dice(3)
        pass

    @staticmethod
    def update(obj):
        HeroTurn.item.update()
        if obj.click_dice_idx is not -1:
            HeroTurn.dice.get_dice_to_idx(obj.click_dice_idx).set_position(
                obj.mouse_x_pos, obj.mouse_y_pos)
            for i in HeroTurn.item.itemlist:
                if HeroTurn.dice.collide_to_object(i):
                    obj.click_dice_idx = -1

        HeroTurn.dice.update()
        pass

    @staticmethod
    def draw(obj):
        HeroTurn.item.draw()
        HeroTurn.dice.draw()
        pass

    @staticmethod
    def exit(obj):
        HeroTurn.dice.dice_clear()
        HeroTurn.item.item_clear()
        pass

class ExitState:
    @staticmethod
    def enter(obj):
        pass

    @staticmethod
    def update(obj):
        for i in HeroTurn.item.getlist():
            i.add_x_position(-10)
        HeroTurn.item.update()
        for i in EnemyTurn.item.getlist():
            i.add_x_position(10)
        EnemyTurn.item.update()
        pass

    @staticmethod
    def draw(obj):
        HeroTurn.item.draw()
        EnemyTurn.item.draw()
        pass

    @staticmethod
    def exit(obj):

        pass

class Action:
    def __init__(self):
        self.cur_turn = HeroTurn
        self.click_dice_idx = -1
        self.mouse_x_pos = 0
        self.mouse_y_pos = 0
        self.cur_turn.enter(self)

    def update(self):
        self.cur_turn.update(self)

    def draw(self):
        self.cur_turn.draw(self)

    def change_turn(self):
        self.cur_turn.exit(self)
        if self.cur_turn == HeroTurn:
            self.cur_turn = EnemyTurn
        else:
            self.cur_turn = HeroTurn
        self.cur_turn.enter(self)

    def collide_to_mouse(self, mouse):
        return self.cur_turn.dice.collide_to_mouse(mouse)

    def set_mouse_idx(self, value):
        self.click_dice_idx = value

    def set_mouse_pos(self, x, y):
        self.mouse_x_pos = x
        self.mouse_y_pos = y

    def get_is_hero_turn(self):
        return self.cur_turn == HeroTurn

    def set_state_exit(self):
        if self.cur_turn != ExitState:
            self.cur_turn = ExitState

    @staticmethod
    def action_clear():
        HeroTurn.dice.dice_clear()
        HeroTurn.item.item_clear()
        EnemyTurn.dice.dice_clear()
        EnemyTurn.item.item_clear()












