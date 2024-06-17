screen skip_confirm:


    on "show" action Function(clack_play_albert)

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _("Are you sure you want to skip?"):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action [Hide('skip_confirm'), Show("albert_deny_skip")]
            textbutton _("No") action Hide('skip_confirm')

screen albert_deny_skip:


    on "show" action Function(clack_play_albert)

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _("No, Taylor. It is incredibly rude to skip all our conversation."):
            style "confirm_prompt"
            xalign 0.5

        add "albert_face_complete" xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Eh...Okay") action [SetVariable('persistent.try_skipping', True), Hide('albert_deny_skip')]

screen reset_screen:

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _("You have reached the good ending of this game. Playing this game again would require resetting the game. Are you sure about that?"):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action [Hide('reset_screen'), Jump('reset_game')]
            textbutton _("No") action Hide('reset_screen')


label reset_game:


    $ persistent.num_finish = 0
    $ persistent.try_skipping = False
    $ persistent.save_tut = False
    $ persistent.unlock_bad_end = False
    $ persistent.unlock_true_end = False
    $ persistent.forced_quit = False
    $ persistent.most_recent_ending = -1
    call screen main_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
