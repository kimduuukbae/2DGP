from fadescene import *
import battle_state_sprite
import boss_state_sprite
from sound_manager import *
from button import *
from battle_action import *
import stage_manager

sprites = None
turnbtn = None
battle_action = None


def enter():
    global sprites, turnbtn, battle_action
    if stage_manager.StageManager.stage_idx is not 2:
        sprites = battle_state_sprite.Battle_state_sprite()
    else:
        sprites = boss_state_sprite.Boss_Battle_Sprite()
    SoundManager.play_sound("Combat", True)
    turnbtn = Turnbutton()
    turnbtn.set_position(1700, 200)

    if main_state.stage_collection.get_stage_idx() == 2:
        battle_action = Action(WaitTurn)
    else:
        battle_action = Action()

def exit():
    battle_action.action_clear()
    HeroStatus.shield = 0


def handle_events():
    global battle_action
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_o:
                hero.HeroStatus.hp += 5

        if event.type == SDL_MOUSEMOTION:
            x = event.x
            y = 1080 - 1 - event.y
            battle_action.set_mouse_pos(x, y)

        if event.type == SDL_MOUSEBUTTONDOWN:
            x = event.x
            y = 1080 - 1 - event.y
            if battle_action.get_is_hero_turn():
                if collide_to_mouse((x, y), turnbtn):
                    battle_action.change_turn()
                dice_idx = battle_action.collide_to_mouse((x, y))
                if dice_idx is not None:
                    battle_action.set_mouse_idx(dice_idx)

        if event.type == SDL_MOUSEBUTTONUP:
            battle_action.set_mouse_idx(-1)


def update():
    sprites.update()
    battle_action.update()
    if sprites.get_victory_flag() == 1:
        battle_action.set_state_exit()

    Fade.update()


def draw():
    clear_canvas()
    sprites.draw()
    battle_action.draw()
    if battle_action.get_is_hero_turn():
        turnbtn.draw()
    Fade.draw()
    update_canvas()
