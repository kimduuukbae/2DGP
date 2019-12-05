from Maptile import *
from monster_in_menu import *
from banner import *
import fadescene
from main_state_spritelist import *
import winsound
from hero import *

map_list = None
bridge_list = None
character = None
collision_object_list = []
banner_list = []
fade_object = None
sprite_list = None


def collision_hero_object(hero_object, collision_object):
    if hero_object.get_id() == collision_object.get_id() and \
    not hero_object.get_in_battle() and not collision_object.get_in_battle():
        if collision_object.get_type() == 1:
            collision_object.set_in_battle()
            hero_object.set_in_battle()
            HeroStatus().set_enemy_type(collision_object.get_name())
        else:
            collision_object.push_event(WaitState)
            fadescene.Fade.push_event(fadescene.FadeInStage)


def enter():

    global character, map_list, bridge_list, sprite_list
    character = Hero('../Resources/stage/character.png')
    sprite_list = main_state_spritelist()
    sprite_list.add_image('../Resources/stage/stageArea.png')
    collision_object_list.append(Slime())
    collision_object_list[0].set_position(550, 850)

    map_list, bridge_list = make_map()
    character.set_position(300, 600)
    character.set_image_pivot(20, 50)
    character.set_image_size(260, 150)


def exit():
    global character
    del character
    sprite_list.clear()
    map_list.clear()


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
    character.update()
    for i in collision_object_list:
        i.update()
        collision_hero_object(character, i)
    for i in banner_list:
        i.update()
    fadescene.Fade.update()


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
    for i in range(len(collision_object_list)):
        if collision_object_list[i].get_in_battle():
            collision_object_list.pop(i)
    pass


def resume():
    character.add_position_x(131)
    banner_list.pop()
    winsound.PlaySound('../Resources/intro/introSound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                       winsound.SND_LOOP | winsound.SND_ASYNC)
    sprite_list.reset()

    if len(collision_object_list) == 0:
        collision_object_list.append(Door())
        collision_object_list[-1].set_position(1550, 850)
    pass
