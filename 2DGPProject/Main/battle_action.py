import hero
from item import *
from dice import *
from battle_state_sprite import *

class EnemyTurn:
    dice = Dice_manager(0)

    item = item_manager("monster")

    is_ai_using = False

    ai_to_distance_x = 0
    ai_to_distance_y = 0
    ai_dice_idx = -1

    ai_time = 0.0

    ai_change_turn = False
    @staticmethod
    def enter(obj):
        if main_state.stage_collection.get_stage_idx() == 2:
            Monsterstatus.change_item()

        EnemyTurn.item.push_item_list(Monsterstatus.item_list)
        EnemyTurn.dice.push_dice_monster(Battle_state_sprite.count_dice)
        EnemyTurn.is_ai_using = False
        Monsterstatus.m_status_conditon.active_condition(Monsterstatus)


    @staticmethod
    def update(obj):
        EnemyTurn.item.update()
        EnemyTurn.dice.update()
        if EnemyTurn.is_ai_using is False:

            if EnemyTurn.dice.dicelist[len(EnemyTurn.dice.dicelist)-1].get_use() or \
                EnemyTurn.dice.dicelist[len(EnemyTurn.dice.dicelist)-1].get_try_fail():
                EnemyTurn.ai_change_turn = True
                EnemyTurn.is_ai_using = True

            for i in EnemyTurn.dice.dicelist:
                if i.get_use() or i.get_try_fail():
                    continue

                for j in EnemyTurn.item.getlist():
                    if j.check_condition(i):
                        EnemyTurn.is_ai_using = True
                        to_x, to_y = j.get_position()
                        origin_x, origin_y = i.get_position()
                        EnemyTurn.ai_to_distance_x = (to_x - origin_x) / 100
                        EnemyTurn.ai_to_distance_y = (to_y - origin_y) / 100
                        EnemyTurn.ai_dice_idx = i.get_index()
                        break
                if EnemyTurn.is_ai_using:
                    break
                i.set_try_fail()

        if EnemyTurn.is_ai_using:
            EnemyTurn.ai_time += game_framework.frame_time
            if EnemyTurn.ai_time > 1.0:
                if EnemyTurn.ai_change_turn:
                    obj.change_turn()
                else:
                    EnemyTurn.dice.get_dice_to_idx(EnemyTurn.ai_dice_idx).add_position(
                        EnemyTurn.ai_to_distance_x, EnemyTurn.ai_to_distance_y)

                    for i in range(len(EnemyTurn.item.itemlist)):
                        if EnemyTurn.dice.collide_to_object(EnemyTurn.item.itemlist[i], HeroStatus):
                            EnemyTurn.item.itemlist.pop(i)
                            EnemyTurn.is_ai_using = False
                            EnemyTurn.ai_time = 0.0
                            Battle_state_sprite.set_shake(5)
                            break

    @staticmethod
    def draw(obj):
        EnemyTurn.item.draw()
        EnemyTurn.dice.draw()

    @staticmethod
    def exit(obj):
        EnemyTurn.dice.dice_clear()
        EnemyTurn.item.item_clear()
        EnemyTurn.ai_change_turn = False
        EnemyTurn.ai_time = 0.0
        pass


class HeroTurn:
    dice = Dice_manager(0)
    item = item_manager("hero")

    @staticmethod
    def enter(obj):
        HeroTurn.item.push_item_list(hero.HeroStatus.equip_item)
        HeroTurn.dice.push_dice(3)
        HeroStatus.status_condition.active_condition(HeroStatus)
        pass

    @staticmethod
    def update(obj):
        HeroTurn.item.update()
        if obj.click_dice_idx is not -1:
            HeroTurn.dice.get_dice_to_idx(obj.click_dice_idx).set_position(
                obj.mouse_x_pos, obj.mouse_y_pos)
            for i in HeroTurn.item.itemlist:
                if HeroTurn.dice.collide_to_object(i, Monsterstatus):
                    obj.click_dice_idx = -1
                    Battle_state_sprite.set_shake(5)



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

class WaitTurn:
    wait_time = 0.0

    @staticmethod
    def enter(obj):
        WaitTurn.wait_time = 0.0
        pass

    @staticmethod
    def update(obj):
        WaitTurn.wait_time += game_framework.frame_time
        if WaitTurn.wait_time > 5.0:
            obj.cur_turn = HeroTurn
            obj.cur_turn.enter(obj)
        pass

    @staticmethod
    def draw(obj):
        pass

    @staticmethod
    def exit(obj):
        pass


class Action:
    def __init__(self, turn=HeroTurn):
        self.cur_turn = turn
        self.click_dice_idx = -1
        self.mouse_x_pos = 0
        self.mouse_y_pos = 0
        self.cur_turn.enter(self)

    def get_current_action(self):
        return self.cur_turn

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












