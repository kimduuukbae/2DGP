from battle_state_sprite import *
from sound_manager import *
import banner
import main_state
import math
import battle_state
import battle_action
import fadescene
import end_state
import fail_state

class Boss_Battle_Sprite:
    stage_image = []
    back_image = None
    anim_back_image = None
    banner = None
    shake_flag = False
    shake_power = 7.0
    def __init__(self):
        self.hero = HeroStatus()
        self.monster = Monsterstatus()
        self.victory_flag = 0
        self.font = Font()
        self.vertexY = 0

        self.camera_y = 0
        self.time_to_banner = 0.0

        self.shake_float = 0.0

        self.rad = 0.0

        self.monstersprite = make_monster(self.hero.enemy_type)

        self.monster.set_status(self.monstersprite)
        if main_state.stage_collection.get_stage_idx() == 2:
            self.vertexY = 240

        if Boss_Battle_Sprite.anim_back_image is None:
            Boss_Battle_Sprite.anim_back_image = load_image('../Resources/battle/turn_background.png')

        Battle_state_sprite.count_dice = self.monstersprite.get_numeric_dice()
        if self.monstersprite.get_sound() is not None:
            self.monstersprite.get_sound().play()

    def draw(self):
        Boss_Battle_Sprite.anim_back_image.rotate_draw(self.rad, 1300 + self.shake_float, 800 + self.shake_float
                                                       + self.vertexY - self.camera_y, 2300, 1800)
        Battle_state_sprite.stage_image[main_state.stage_collection.get_stage_idx()].draw(960 + self.shake_float,
                                                                                          540 + self.shake_float + self.vertexY - self.camera_y)
        Battle_state_sprite.back_image.draw(200 + self.shake_float, 170 + self.shake_float - self.camera_y)

        self.hero.draw(600 + self.shake_float, 100 + self.shake_float)
        self.font.draw(450 + self.shake_float, 160 + self.shake_float, "전사", (255, 255, 255))
        if self.hero.shield == 0:
            self.font.draw(555 + self.shake_float, 102 + self.shake_float ,
                           str(self.hero.get_hp()) + ' / ' + str(self.hero.get_maxhp()), (255, 255, 255))
        else:
            self.font.draw(535 + self.shake_float, 102 + self.shake_float,
                           str(self.hero.get_hp()) + ' / ' + str(self.hero.get_maxhp()) + ' + ' + str(self.hero.shield),
                           (255, 255, 150))

        self.monster.draw(1750 + self.shake_float, 800 + self.shake_float)

        if self.monstersprite.get_page() == 1:
            self.font.draw(1600 + self.shake_float, 860 + self.shake_float, self.monster.name,
                           (255, 255, 255))

            self.font.draw(1705 + self.shake_float, 802 + self.shake_float ,
                           str(self.monster.hp) + ' / ' + str(self.monster.max_hp), (255, 255, 255))
        else:
            self.font.draw(1600 + self.shake_float, 860 + self.shake_float, self.monster.name,
                           (255, 0, 0))

            self.font.draw(1705 + self.shake_float, 802 + self.shake_float,
                           str(self.monster.hp) + ' / ' + str(self.monster.max_hp), (255, 0, 0))

        self.monstersprite.draw(self.shake_float, self.shake_float + self.camera_y)
        Battle_state_sprite.condition_image.draw(600 + self.shake_float, 45 + self.shake_float)
        Battle_state_sprite.condition_image.draw(1750 + self.shake_float, 745 + self.shake_float)

        for i in range(len(self.hero.status_condition.get_condition_list())):
            condition_name = STATUS_CONDITION[self.hero.status_condition.get_condition_to_idx(i).get_type()]
            get_condition_count = self.hero.status_condition.get_condition_to_idx(i).get_count()
            self.font.draw(470 + (i * 150) + self.shake_float, 46 + self.shake_float // 10 ,
                           condition_name + "  " + str(get_condition_count), (139, 0, 255))


    def update(self):
        self.monstersprite.update()
        self.rad += 0.01
        cur_action = battle_state.battle_action.get_current_action()

        if cur_action == battle_action.WaitTurn:
            self.camera_y = self.camera_y + 1
        elif cur_action == battle_action.HeroTurn:
            self.camera_y = self.camera_y - 10
        elif cur_action == battle_action.EnemyTurn:
            self.camera_y = self.camera_y + 10
        self.camera_y = clamp(0, self.camera_y, 500)

        if self.monstersprite.get_page() == 1 and Monsterstatus.hp < self.monstersprite.get_hp() // 2:
            self.monstersprite.change_page()
            SoundManager.add_effect_sound("../Resources/sound/effect/ladyluck_p.wav", "Raugh")
            SoundManager.set_volume("Raugh", 128)
            SoundManager.play_sound("Raugh", False)
            fadescene.Fade.push_event(fadescene.FadeTwinkle)
            Battle_state_sprite.count_dice = Monsterstatus.save_obj.get_numeric_dice()

        if self.victory_flag == 0:
            if HeroStatus.hp <= 0 or Monsterstatus.hp <= 0:
                self.victory_flag = 1
                SoundManager.stop("Combat")
                if HeroStatus.hp > 0:
                    SoundManager.play_sound("win", False)

        if self.victory_flag == 1:
            self.time_to_banner += game_framework.frame_time
            if self.time_to_banner > 2.0:
                if HeroStatus.hp <= 0:
                    self.victory_flag = 2
                    fadescene.Fade.change_state(fail_state)
                elif Monsterstatus.hp <= 0:
                    self.victory_flag = 3
                    fadescene.Fade.change_state(end_state)
                self.time_to_banner = 0.0


        if Battle_state_sprite.shake_flag:
            self.shake_float = math.sin(Battle_state_sprite.shake_power * 10.0) * math.pow(0.5,
                                                                                           Battle_state_sprite.shake_power) * 20
            Battle_state_sprite.shake_power = Battle_state_sprite.shake_power - 1
            if Battle_state_sprite.shake_power < 0:
                Battle_state_sprite.shake_flag = False
                self.shake_float = 0.0

    def get_victory_flag(self):
        return self.victory_flag

    @staticmethod
    def set_shake(value):
        Battle_state_sprite.shake_flag = True
        Battle_state_sprite.shake_power = value

    @staticmethod
    def set_init():
        if len(Battle_state_sprite.stage_image) == 0:
            Battle_state_sprite.stage_image.append(load_image("../Resources/battle/battle_gameshow.png"))
            Battle_state_sprite.stage_image.append(load_image("../Resources/battle/battle_ice.png"))
            Battle_state_sprite.stage_image.append(load_image("../Resources/battle/finale_back.png"))
        if Battle_state_sprite.back_image is None:
            Battle_state_sprite.back_image = load_image("../Resources/battle/warrior_back.png")
        if Battle_state_sprite.banner is None:
            Battle_state_sprite.banner = banner.WinBanner()
        if Battle_state_sprite.condition_image is None:
            Battle_state_sprite.condition_image = load_image('../Resources/common/condition_text_bar.png')
