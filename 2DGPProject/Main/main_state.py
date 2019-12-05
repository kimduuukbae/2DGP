import stage_manager
import hero
stage_collection = None


def enter():
    global stage_collection
    stage_collection = stage_manager.StageManager()
    stage_collection.enter()


def exit():
    stage_collection.exit()


def handle_events():
    stage_collection.handle_events()


def update():
    stage_collection.update()


def draw():
    stage_collection.draw()


def pause():
    stage_collection.pause()


def resume():
    hero.HeroStatus.shield = 0
    stage_collection.resume()
