import pico2d


class SoundManager:
    sound_dict = {}

    @staticmethod
    def change_sound(music_direction, before):
        if before in SoundManager.sound_dict:
            obj = SoundManager.sound_dict.pop(before)
            obj.stop()
            del obj
        SoundManager.sound_dict[before] = pico2d.load_music(music_direction)

    @staticmethod
    def add_sound(music_direction, music_name):
        if music_name not in SoundManager.sound_dict:
            SoundManager.sound_dict[music_name] = pico2d.load_music(music_direction)

    @staticmethod
    def add_effect_sound(music_direction, music_name):
        if music_name not in SoundManager.sound_dict:
            SoundManager.sound_dict[music_name] = pico2d.load_wav(music_direction)
        else:
            obj = SoundManager.sound_dict.pop(music_name)
            del obj
            SoundManager.sound_dict[music_name] = pico2d.load_wav(music_direction)

    @staticmethod
    def play_sound(music_name, repeat):
        if music_name not in SoundManager.sound_dict:
            return None

        if repeat is True:
            SoundManager.sound_dict[music_name].repeat_play()
        else:
            SoundManager.sound_dict[music_name].play()
        return True

    @staticmethod
    def set_volume(music_name, volume):
        SoundManager.sound_dict[music_name].set_volume(volume)

    @staticmethod
    def stop(music_name):
        if music_name in SoundManager.sound_dict:
            SoundManager.sound_dict[music_name].stop()

    @staticmethod
    def pop_sound(music_name):
        if music_name in SoundManager.sound_dict:
            ob = SoundManager.sound_dict.pop(music_name)
            ob.stop()
            del ob
