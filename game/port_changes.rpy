init python:
    if renpy.android:
        config.basedir = os.environ['ANDROID_PUBLIC']
        config.gamedir = config.basedir + "/game"

        if not os.path.isdir(config.basedir):
            os.mkdir(config.basedir)
        if not os.path.isdir(config.gamedir):
            os.mkdir(config.gamedir)

        config.variants = ['android', 'medium', 'touch', None]

        gesture_dict = {'s' : 'hide_windows'}
        config.gestures.update(gesture_dict)

        config.gl2 = False
        config.autosave_on_quit = True
        config.save_on_mobile_background = True

        renpy.game.preferences.gl_powersave = False


        build.classify("**.vscode", None)

init -999 python:
    version_tuple = list(renpy.version_tuple)
    version_list = version_tuple[:3]
    renpy_version_main = str(version_list[0])+"."+str(version_list[1])+"."+str(version_list[2])
    if ("renpy-"+renpy_version_main+"-sdk" in config.basedir):
        config.developer = True
    else:
        config.developer = False

python early:
    if renpy.android:
        config.savedir = config.basedir + "/" + config.save_directory
