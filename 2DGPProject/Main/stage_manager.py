import stage1
import stage2
import stage3


class StageManager:
    cur_stage = None
    stage_idx = 0
    stage_list = None

    def __init__(self):
        if StageManager.cur_stage is None:
            StageManager.stage_list = [stage1, stage2, stage3]
            StageManager.cur_stage = StageManager.stage_list[0]
            StageManager.stage_idx = 0


    @staticmethod
    def set_index(value):
        StageManager.stage_idx = value
        StageManager.cur_stage = StageManager.stage_list[value]

    @staticmethod
    def get_stage_idx():
        return StageManager.stage_idx

    @staticmethod
    def enter():
        StageManager.cur_stage.enter()

    @staticmethod
    def update():
        StageManager.cur_stage.update()

    @staticmethod
    def draw():
        StageManager.cur_stage.draw()

    @staticmethod
    def handle_events():
        StageManager.cur_stage.handle_events()

    @staticmethod
    def pause():
        StageManager.cur_stage.pause()

    @staticmethod
    def resume():
        StageManager.cur_stage.resume()

    @staticmethod
    def exit():
        StageManager.cur_stage.exit()

    @staticmethod
    def next_stage():
        StageManager.stage_idx += 1
        StageManager.cur_stage.exit()
        StageManager.cur_stage = StageManager.stage_list[StageManager.stage_idx]
        StageManager.cur_stage.enter()


