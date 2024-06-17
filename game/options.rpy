





define config.nearest_neighbor = True
define config.image_cache_size = 50
define config.default_fullscreen = True








define config.name = _("Therapy With Dr. Albert Krueger")





define gui.show_name = True




define config.version = "1.2.1"





define gui.about = _p("""
    Solo-developed by dino999z (Twitter: {a=https://twitter.com/dino999z/}@dino999z{/a})

    Other contributers:
    Harmless (music),
    Michael Brazeau (ad narration)

    Used libraries:
    Audioblocks,
    Freesound.org

    SE:
    Xtrgamer, Fellur, Mrthenoronha, Sapisvr, Repairedgnome, Syna-max, Bobby Cole
""")






define build.name = "Therapy_with_Dr_Albert_Krueger"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = None










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 40





default preferences.afm_time = 15
















define config.save_directory = "Taylor_1_2_1"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.gif', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/images/**.png', 'archive')
    build.classify('game/audio/**.ogg', 'archive')
    build.classify('game/audio/**.mp3', 'archive')
    build.classify('game/audio/**.wav', 'archive')
    build.classify('game/**.rpyc', 'archive')









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
