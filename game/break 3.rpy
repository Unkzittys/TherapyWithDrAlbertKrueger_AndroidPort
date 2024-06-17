

label break_3_start:

    window auto

    $ auto_enabled_ = True

    if num_open_eyes == 4:

        $ renpy.music.set_volume(music_volume, delay=0, channel='music')
        play music "audio/takeADeepBreath_v2.mp3"

        scene albert_office
        show albert_sitting
        show albert_office_lamp
        show albert_office_telephone
        show taylor_face_panic:
            xpos 190 ypos 600
        $ renpy.transition(PushMove(0.1, "pushup"))
        $ renpy.pause(0.01, hard=True)
        $ renpy.transition(PushMove(0.1, "pushup"))
        $ renpy.pause(0.01, hard=True)
        $ renpy.transition(PushMove(0.1, "pushup"))
        $ renpy.pause(0.01, hard=True)

        $ renpy.pause(1.0, hard='True')

        a "My apologies, {w=0.5}Taylor."

        a "I was getting too excited to hear your answers, {w=0.5}that I came a bit too close."

        t "I wouldn’t call that \"a bit\" too close, {w=0.5}but whatever."
    else:


        stop music fadeout 1.0

        hide screen empty_screen
        hide screen open_eyes_decision_screen

        $ renpy.pause(1.0, hard='True')

        a "Thank you for your cooperation, {w=0.5}Taylor."

        a "You are now free to re-open your eyes."

        if persistent.num_finish > 0:
            $ quick_load_ = False
            with Dissolve(0.2)

        $ renpy.music.set_volume(music_volume, delay=0, channel='music')
        play music "audio/takeADeepBreath_v2.mp3"

        hide close_eye_animation
        show open_eye_animation behind taylor_face_close_eye
        show taylor_face_open_eye:
            xpos 190 ypos 600
        pause 0.5
        hide taylor_face_open_eye
        show taylor_face:
            xpos 190 ypos 600
        hide taylor_face_outline with Dissolve(0.3)

        $ renpy.pause(1.0, hard='True')

    a "Shall we take another short break?"

    a "Let me make the music louder."

    window hide

    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_panic

    python:

        for x in range(0, 6):
            music_volume += 0.1
            renpy.music.set_volume(music_volume, delay=0, channel='music')
            renpy.pause(0.1)

    $ renpy.pause(2.0, hard='True')


    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/drunken-single-singing-male-long.mp3" loop

    $ renpy.pause(4.0, hard='True')

    window auto

    t_think "......"

    window hide

    $ renpy.pause(2.0, hard='True')

    window auto

    t "Umm... {w=0.5}Do you hear that?"

    window hide

    python:

        for x in range(0, 6):
            music_volume -= 0.1
            renpy.music.set_volume(music_volume, delay=0, channel='music')
            renpy.pause(0.3)

    stop music fadeout 6.0

    $ renpy.pause(2.0, hard='True')

    window auto

    a_think "......"

    a "*sigh* {w=0.5}My apologies for such unpleasant experience, {w=0.5}Taylor."

    a "Now if you would excuse me, {w=0.5}I will go handle that."

    a "Why don’t you watch some videos at the mean time?"

    t "Umm... {w=0.5}Okay."

    a "I’ll put on some videos."

    t "...Albert."

    a "Yes?"

    t "...Please don’t kill him."

    a "*laugh* {w=0.5}Of course I won’t. {w=0.5}Who do you think I am?"

    if persistent.num_finish > 1:

        a "Some kind of mad sadistic doctor?"

    a "I’ll be back soon."

    $ renpy.predict('cat_mouse_animation')

    stop sound
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/system-glitch-2.ogg"

    scene black
    show cat_mouse_animation
    show text _ ("We'll be \nright back"):
        zoom 5.0
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)

    $ renpy.pause(4.0, hard='True')

    show screen empty_screen
    if persistent.num_finish == 1:
        $ renpy.movie_cutscene("HORROR.webm")
    else:
        if persistent.unlock_bad_end and persistent.unlock_true_end:
            $ renpy.movie_cutscene("SKELETONS.webm")
        else:
            $ renpy.movie_cutscene("_FAKEAD.webm")

    $ renpy.pause(4.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/sfx-censored-bleep--long.ogg"

    if persistent.num_finish > 0:
        if persistent.num_finish % 2 == 0:
            scene albert_office_glitch_1
            show albert_sitting_glitch_1
        else:
            scene albert_office_red
            show albert_sitting_glitch_3
    else:
        scene albert_office_red_2
    show bad_tv
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)

    $ renpy.pause(2.0, hard='True')

    $ renpy.music.set_volume(music_volume, delay=0, channel='music')
    play music "audio/takeADeepBreath_v2.mp3"

    scene albert_office
    show albert_sitting
    show albert_office_lamp
    show albert_office_telephone
    if persistent.num_finish == 1:
        show taylor_face_panic:
            xpos 190 ypos 600
    else:
        show taylor_face:
            xpos 190 ypos 600
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)

    $ renpy.pause(2.0, hard='True')

    hide screen empty_screen

    a "Hello again, {w=0.5}Taylor."

    a "I hope you enjoyed the video."

    if persistent.num_finish == 1:

        t "What, {w=0.5}what the hell was that video?"

        a "It was a commercial of our company."

        t "No it was not."

        t "It was something way f**ked up than that."

        a "Hmm..."

        a "My apologies. {w=0.5}I might have put on the wrong video."

        a "Anyways, {w=0.5}are we ready for the next round of therapy?"

        hide taylor_face_panic
        show taylor_face:
            xpos 190 ypos 600

        t_think "......"
    else:


        if persistent.unlock_bad_end and persistent.unlock_true_end:

            t "What was that video all about?"

            a "Dancing skeletons. {w=0.5}Did you not enjoy it?"

            t "...Eh, {w=0.5}I guess it was cute."

            t "Did things get resolved with... {w=0.5}that dude?"

            a "Yes. {w=0.5}Resolved. {w=0.5}Peacefully."

            t "That’s, {w=0.5}that’s good."

            a "Are we ready for the next round of therapy?"

            t "...Yes, {w=0.5}sure."
        else:


            t "That was... {w=0.5}Uh... {w=0.5}A pretty cool commercial."

            a "Thank you."

            a "In fact, {w=0.5}it is a bit out of date."

            a "I plan to update it soon."

            t "Umm... {w=0.5}I see."

            t "Did things get resolved with... {w=0.5}that dude?"

            a "Yes. {w=0.5}Resolved. {w=0.5}Peacefully."

            t "That’s, {w=0.5}that’s good."

            a "Are we ready for the next round of therapy?"

            t "...Yes, {w=0.5}sure."

    jump rorschach_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
