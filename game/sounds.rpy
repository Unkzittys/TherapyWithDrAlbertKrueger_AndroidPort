init -1 python:
    renpy.music.register_channel("beep", "voice", True)

    def clack_play_albert(on=False):
        if on:
            renpy.music.set_volume(0.15, delay=0, channel='beep')
            renpy.music.play("audio/beep1.ogg", channel="beep", loop=True)
            global albert_is_talking
            albert_is_talking = True
        else:
            renpy.music.stop(channel="beep", fadeout = 0.5)
            global albert_is_talking
            albert_is_talking = False

    def beep_albert(event, **kwargs):
        if event == "show" or event == "begin":
            clack_play_albert(True)
        
        if event == "slow_done":
            clack_play_albert(False)

    def clack_play_taylor(on=False):
        if on:
            renpy.music.set_volume(0.2, delay=0, channel='beep')
            renpy.music.play("audio/beep2.ogg", channel="beep", loop=True)
            global taylor_is_talking
            taylor_is_talking = True
        else:
            renpy.music.stop(channel="beep", fadeout = 0.5)
            global taylor_is_talking
            taylor_is_talking = False

    def beep_taylor(event, **kwargs):
        if event == "show" or event == "begin":
            clack_play_taylor(True)
        if event == "slow_done":
            clack_play_taylor(False)

    def clack_play_question(on=False):
        if on:
            renpy.music.set_volume(1.0, delay=0, channel='beep')
            renpy.music.play("audio/beep3.ogg", channel="beep", loop=True)
        else:
            renpy.music.stop(channel="beep", fadeout = 0.5)

    def beep_question(event, **kwargs):
        if event == "show" or event == "begin":
            clack_play_question(True)
        if event == "slow_done":
            clack_play_question(False)

    def clack_play_nurse(on=False):
        if on:
            renpy.music.set_volume(0.25, delay=0, channel='beep')
            renpy.music.play("audio/beep4.ogg", channel="beep", loop=True)
        else:
            renpy.music.stop(channel="beep", fadeout = 0.5)

    def beep_nurse(event, **kwargs):
        if event == "show" or event == "begin":
            clack_play_nurse(True)
        if event == "slow_done":
            clack_play_nurse(False)

    def clack_play_vincent(on=False):
        if on:
            renpy.music.set_volume(0.25, delay=0, channel='beep')
            renpy.music.play("audio/beep5.ogg", channel="beep", loop=True)
        else:
            renpy.music.stop(channel="beep", fadeout = 0.5)

    def beep_vincent(event, **kwargs):
        if event == "show" or event == "begin":
            clack_play_vincent(True)
        if event == "slow_done":
            clack_play_vincent(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
