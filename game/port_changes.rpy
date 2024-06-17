init python:
    if renpy.android:
        config.basedir = os.environ['ANDROID_PUBLIC']
        config.gamedir = config.basedir + "/game"

        if not os.path.isdir(config.basedir):
            os.mkdir(config.basedir)
        if not os.path.isdir(config.gamedir):
            os.mkdir(config.gamedir)

        config.variants = ['pc', 'large', 'touch', None]

        gesture_dict = {'n' : 'game_menu', 's' : 'hide_windows'}
        config.gestures.update(gesture_dict)


        build.classify("**.vscode", None)

        try: renpy.file(config.basedir + "/info.txt")
        except: open(config.basedir + "/info.txt", "wb").write("Game: {}\nVersion: {}".format(config.name, config.version))

python early:
    if renpy.android:
        config.savedir = config.basedir + "/" + config.save_directory