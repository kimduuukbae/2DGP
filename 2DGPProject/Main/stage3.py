from Maptile import *
from monster_in_menu import *
from banner import *
import fadescene
from main_state_spritelist import *
from sound_manager import *
from hero import *

map_list = None
bridge_list = None
character = None
collision_object_list = []
banner_list = []
fade_object = None
sprite_list = None

finale_flag = False
finale_time = 0.0


def collision_hero_object(hero_object, collision_object):
    global finale_flag
    if hero_object.get_id() == collision_object.get_id() and \
    not hero_object.get_in_battle() and not collision_object.get_in_battle():
        if collision_object.get_type() == 1:
            collision_object.set_in_battle()
            hero_object.set_in_battle()
            HeroStatus.set_enemy_type(collision_object.get_name())
        elif collision_object.get_type() == 3 and finale_flag is False:
            hero_object.add_event(WaitState)
            fadescene.Fade.push_event(fadescene.FadeTwinkle)
            sprite_list.list_pop()
            sprite_list.add_image('../Resources/stage/finale2.png')
            sprite_list.set_shake(40)
            finale_flag = True
            hero_object.set_in_battle()
            HeroStatus.set_enemy_type(collision_object.get_name())


def enter():

    global character, map_list, bridge_list, sprite_list
    character = Hero('../Resources/stage/character.png')
    sprite_list = main_state_spritelist()
    sprite_list.add_image('../Resources/stage/finale1.png')

    collision_object_list.append(FinaleBoss())
    collision_object_list[0].set_position(960, 550)

    map_list, bridge_list = make_map(3)
    character.set_position(960, 300)
    character.set_image_pivot(20, 50)
    character.set_image_size(260, 150)

    SoundManager.pop_sound("Combat")
    SoundManager.add_sound("../Resources/sound/combatboss.ogg", "Combat")

    SoundManager.change_sound("../Resources/sound/ladyluckfloor.ogg", "BackGround")
    SoundManager.play_sound("BackGround", True)

    SoundManager.add_effect_sound("../Resources/sound/effect/ladyluck.wav", "Raugh")

def exit():

    global character, finale_flag, finale_time
    del character
    collision_object_list.clear()
    banner_list.clear()
    sprite_list.clear()
    map_list.clear()
    finale_flag = False
    finale_time = 0.0


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                x = event.x
                y = 1080 - 1 - event.y
                if character.get_moving() or character.get_in_battle():
                    pass
                for i in map_list:
                    if i.click_tile(x, y):
                        tile_x, tile_y, tile_id = i.get_tileinfo()
                        if tile_id == character.get_id() or character.get_moving():
                            break
                        clear_maplist()
                        for j in map_list:
                            j.set_visited(False)
                        if check_map(character.get_id(), tile_id):
                            insert_map(map_list, character.get_id(), tile_id)
                            character.move_to_tile(get_maplist())
                            break
            if event.type == SDL_MOUSEMOTION:
                x = event.x
                y = 1080 - 1 - event.y
                for i in map_list:
                    i.overlap_tile(x, y)


def update():
    global finale_flag, finale_time
    character.update()
    for i in collision_object_list:
        i.update()
        collision_hero_object(character, i)
    for i in banner_list:
        i.update()
    fadescene.Fade.update()
    sprite_list.update()
    if finale_flag:
        finale_time += game_framework.frame_time
        if finale_time > 2.0:
            finale_flag = False
            finale_time = 0.0
            collision_object_list[0].set_in_battle()



def draw():
    clear_canvas()
    sprite_list.draw()
    for i in bridge_list:
        i.draw()
    for i in map_list:
        i.draw()
    for i in collision_object_list:
        i.draw()
    character.draw()
    for i in banner_list:
        i.draw()
    fadescene.Fade.draw()
    update_canvas()


def pause():
    SoundManager.play_sound("Raugh", False)
    for i in range(len(collision_object_list)):
        if collision_object_list[i].get_in_battle():
            collision_object_list.pop(i)
    banner_list.pop()




def resume():
    character.add_position_x(131)
    banner_list.pop()

    sprite_list.reset()

    if len(collision_object_list) == 0:
        collision_object_list.append(Door())
        collision_object_list[-1].set_position(1550, 850)
    pass
