init python:
    if renpy.android:
        config.basedir = os.environ['ANDROID_PUBLIC']
        config.gamedir = config.basedir + "/game"

        if not os.path.isdir(config.basedir):
            os.mkdir(config.basedir)
        if not os.path.isdir(config.gamedir):
            os.mkdir(config.gamedir)

        config.variants = ['pc', 'large', 'touch', None]

        gesture_dict = {'s' : 'hide_windows'}
        config.gestures.update(gesture_dict)

        config.gl2 = False
        config.autosave_on_quit = True
        config.save_on_mobile_background = True


        build.classify("**.vscode", None)

python early:
    if renpy.android:
        config.savedir = config.basedir + "/" + config.save_directory
