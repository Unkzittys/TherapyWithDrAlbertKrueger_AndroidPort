
define answered_survey = [False, False, False]
define persistent.most_recent_ending = -1
define persistent.num_finish = 0

define dead_taylor_eyes = 2
define persistent.try_skipping = False
define persistent.save_tut = False
define persistent.unlock_bad_end = False
define persistent.unlock_true_end = False

label end:

    if persistent.num_finish > 0:

        $ quick_load_ = False
        with Dissolve(0.2)

    stop music fadeout 5.0

    $ renpy.pause(3.0, hard='True')

    $ auto_enabled_ = True

    a "Well done, {w=0.5}Taylor. {w=0.5}Well done."

    a "I am so proud of you."

    a "I hate to say this, {w=0.5}but we’re getting close to the end of our therapy."

    a "I just want to say, {w=0.5}I really enjoyed speaking to you."

    a "And I really appreciate that you chose Krueger Corporation."

    t "Umm... {w=0.5}I actually didn’t, {w=0.5}but no worries."

    t "It was also a very... {w=0.5}interesting session for me."

    a "I’m glad you enjoyed it as well. {w=0.5}That means a lot to me."

    a "May I ask what was your favorite section of the therapy?"

    t "Favorite section? {w=0.5}Uh... {w=0.5}They were all pretty cool I guess."

    a "You’re too kind, {w=0.5}Taylor."

    a "I’m so glad to hear that."

    a "Would you mind filling out this post-therapy survey for me? "

    a "That would mean a lot to me."

    t "...Sure."

    $ preferences.afm_enable = False
    $ auto_enabled_ = False

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "audio/weird-detuned-guitar-sounds.mp3"

    $ answered_survey[0] = False
    $ answered_survey[1] = False
    $ answered_survey[2] = False

    window hide

    show black:
        alpha 0.6
    show survey_paper
    show text _ ("How did you like the overall\nexperience of the therapy?") as text_1:
        ypos 70
    show text _ ("How would you rate\nyour therapist?") as text_2:
        ypos 300
    show text _ ("Would you recommend Krueger\nCorporation to your friends?") as text_3:
        ypos 520
    show sad_face as sad_face_1:
        xpos 565 ypos 180
    show smiley_face as smiley_face_1:
        xpos 705 ypos 180
    show sad_face as sad_face_2:
        xpos 565 ypos 405
    show smiley_face as smiley_face_2:
        xpos 705 ypos 405
    show sad_face as sad_face_3:
        xpos 565 ypos 630
    show smiley_face as smiley_face_3:
        xpos 705 ypos 630
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    call screen survey_screen

label finish_survey:

    $ renpy.pause(1.0, hard='True')

    hide survey_paper
    hide text_1
    hide text_2
    hide text_3
    hide sad_face_1
    hide sad_face_2
    hide sad_face_3
    hide smiley_face_1
    hide smiley_face_2
    hide smiley_face_3
    hide smiley_face_hover_1
    hide smiley_face_hover_2
    hide smiley_face_hover_3
    hide black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    stop music fadeout 2.0

    $ auto_enabled_ = True

    a "Thanks a lot. {w=0.5}That was a big help."

    a "Before I let you go..."

    a "Can I have one last request?"

    t "...Sure. {w=0.5}What is it?"

    if math_answered_correct == total_num_math_problems and cup_answered_correct == total_num_cups_and_balls_problems and num_open_eyes == 0 and num_flipping == 0:

        jump true_end
    else:

        jump bad_end

label true_end:

    $ renpy.music.set_volume(music_volume, delay=0, channel='music')
    play music ["<silence 1.0>", "audio/skipABeat_v1.mp3"]
    queue music "audio/skipABeat_v1.mp3"

    show albert_office_red_3 behind albert_sitting:
        alpha 0
        linear 3.0 alpha 1
    show albert_office_telephone:
        alpha 1
        linear 3.0 alpha 0
    show albert_office_lamp:
        alpha 1
        linear 3.0 alpha 0
    show bad_tv behind taylor_face:
        alpha 0
        linear 3.0 alpha 1

    a "Will you... {w=0.5}become a dream eater?"

    show taylor_face_panic:
        xpos 190 ypos 600
    hide taylor_face

    t "Hu-{w=0.5}huh!?"

    t "What is a dream eater?"

    a "They are... {w=0.5}my servants. "

    a "Very, {w=0.5}very loyal servants."

    a "They all used to be good kids. {w=0.5}Just like you."

    a "Congratulations, {w=0.5}Taylor."

    a "You should feel proud."

    t "But - {w=0.5}but I don’t want to -"

    a "It is only because of the Dream Therapy, {w=0.5}that I get to know wonderful people like you."

    a "We need you - {w=0.5}to build a better future of G2 district."

    a "We need you - {w=0.5}to join the army."

    window hide

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "audio/mrthenoronha__destruction-8-bit.ogg"

    stop music fadeout 3.0

    show taylor_face_bleed:
        xpos 190 ypos 600
    hide taylor_face_panic
    show blood_drip

    $ renpy.pause(2.0, hard='True')

    window hide

    scene black

    $ renpy.pause(5.0, hard='True')

    window auto

    a "Thank you... {w=0.5}for your contribution to G2 district."

    window hide

    $ persistent.most_recent_ending = 1
    $ persistent.unlock_true_end = True

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "audio/takeADeepBreath_v1.mp3"

    $ renpy.pause(2.0, hard='True')

    show text _ ("BAD{size=-30} (TRUE?) {/size}END") as text_1:
        zoom 5.0 yoffset -60
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(2.0, hard='True')

    show text _ ("ENDING 2/3"):
        zoom 2.0 yoffset 70
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(4.0, hard='True')

    hide text_1
    hide text
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    jump credit_scene

label bad_end:

    $ renpy.music.set_volume(music_volume, delay=0, channel='music')
    play music ["<silence 1.0>", "audio/skipABeat_v1.mp3"]
    queue music "audio/skipABeat_v1.mp3"

    show albert_office_red behind albert_sitting:
        alpha 0
        linear 3.0 alpha 1
    show albert_office_telephone:
        alpha 1
        linear 3.0 alpha 0
    show albert_office_lamp:
        alpha 1
        linear 3.0 alpha 0
    show albert_sitting_glitchy behind taylor_face
    hide albert_sitting
    show bad_tv behind taylor_face:
        alpha 0
        linear 3.0 alpha 1

    a "Will you...{w=0.5} sacrifice yourself for the G2 district?"

    show taylor_face_panic:
        xpos 190 ypos 600
    hide taylor_face

    t "Hu-{w=0.5}huh!?"

    a "We need you - {w=0.5}for building a better future of G2 district."

    a "We need you - {w=0.5}to feed the hungry people of G2 district."

    a "G2... {w=0.5}is our hometown."

    a "We need to... {w=0.5}make G2 better."

    t "What do you mean “feed the hungry people” ???"

    a "My children... {w=0.5}have been starving."

    a "They will be grateful to you... {w=0.5}forever."

    stop music fadeout 1.5

    window hide

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/repairedgnome__jumpscare1.mp3"

    show creepy_face_1 behind bad_tv:
        zoom 0.8
        ease_expo 2.0 zoom 3
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    hide creepy_face_1
    show creepy_face_1:
        zoom 3
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    scene black
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)

    $ renpy.pause(5.0, hard='True')

    window auto

    a "Thank you... {w=0.5}for your contribution to G2 district."

    window hide

    $ persistent.most_recent_ending = 0
    $ persistent.unlock_bad_end = True

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "audio/takeADeepBreath_v1.mp3"

    $ renpy.pause(2.0, hard='True')

    show text _ ("BAD END") as text_1:
        zoom 5.0 yoffset -60
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(2.0, hard='True')

    show text _ ("ENDING 1/3"):
        zoom 2.0 yoffset 70
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(4.0, hard='True')

    hide text_1
    hide text
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    jump credit_scene

label good_end:

    a "Sorry to say this, {w=0.5}but it looks like I’ll have to end our therapy early, {w=0.5}Taylor."

    t "...Oh. {w=0.5}That’s fine."

    a "I just want to say, {w=0.5}I really enjoyed speaking to you."

    a "And it’s been a while since I met someone like you, {w=0.5}Taylor."

    t "Someone like me?"

    a "Yes. {w=0.5}Rebellious, {w=0.5}full of energy, {w=0.5}no fear in your heart."

    a "But most importantly, {w=0.5}you try very hard to give me a hard time."

    t "Umm... {w=0.5}I guess I’m flattered."

    a "I hope we can become friends. {w=0.5}Maybe we can write letters to each other?"

    t_think "......"

    t "People don’t write letters anymore."

    a_think "......"

    a "That’s a shame."

    a "I guess I’ll just figure out some other way."

    a "Before I let you go, {w=0.5}can I have one last request?"

    t "...Sure. {w=0.5}What is it?"

    a "Would you mind filling out this post-therapy..."

    a "Forget about it."

    a "Goodbye, {w=0.5}Taylor."

    a "I hope we can stay in touch."

    window hide

    stop music

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/system-glitch-2.ogg"

    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)

    scene desktop
    show taylor_face_panic:
        xpos 190 ypos 600

    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)

    $ renpy.pause(2.0, hard=True)

    window show

    t "...Huh?"

    t "This is my desktop."

    t "Was that... {w=0.5}just a dream?"

    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(1.0, hard='True')

    t_think "......"

    t "What’s this txt file on my desktop?"

    window hide

    $ persistent.most_recent_ending = 2

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "audio/takeADeepBreath_v1.mp3"

    $ renpy.pause(2.0, hard='True')

    show text _ ("GOOD{size=-30} (TRUE) {/size}END") as text_1:
        zoom 5.0 yoffset -60
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(2.0, hard='True')

    show text _ ("ENDING 3/3"):
        zoom 2.0 yoffset 70
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(4.0, hard='True')

    hide text_1
    hide text
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    jump credit_scene

    return

label credit_scene:

    $ persistent.num_finish += 1

    $ renpy.pause(1.0, hard='True')

    show text _ ("A GAME BY") as text_1:
        zoom 2.0 yoffset -80 xalign 0.5
    show text _ ("DINO999Z"):
        zoom 3.0 xalign 0.5 yoffset 10
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(4.0, hard='True')

    hide text_1
    hide text
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    show text _ ("OTHER CONTRIBUTERS:") as text_1:
        zoom 1.0 yoffset -80 xalign 0.5
    show text _ ("HARMLESS (MUSIC)") as text_2:
        zoom 1.5 xalign 0.5 yoffset -30
    show text _ ("MICHAEL BRAZEAU (AD NARRATION)"):
        zoom 1.5 xalign 0.5 yoffset 20
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(4.0, hard='True')

    hide text_1
    hide text_2
    hide text
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    show text _ ("USED LIBRARIES:") as text_1:
        zoom 1.0 yoffset -80 xalign 0.5
    show text _ ("AUDIOBLOCKS") as text_2:
        zoom 1.5 xalign 0.5 yoffset -30
    show text _ ("FREESOUND.ORG"):
        zoom 1.5 xalign 0.5 yoffset 20
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(4.0, hard='True')

    hide text_1
    hide text_2
    hide text
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    show text _ ("SOUND EFFECTS:") as text_1:
        zoom 1.0 yoffset -80 xalign 0.5
    show text _ ("XTRGAMR  FELLUR  MRTHENORONHA") as text_2:
        zoom 1.5 yoffset -30
    show text _ ("SAPISVR  REPAIREDGNOME  SYNA-MAX") as text_3:
        zoom 1.5 yoffset 20
    show text _ ("BOBBY COLE"):
        zoom 1.5 yoffset 70
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(4.0, hard='True')

    hide text_1
    hide text_2
    hide text_3
    hide text
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')


    if persistent.lang != None:
        $ renpy.pause(1.0, hard='True')

        show text _ ("TRANSLATION:") as text_1:
            zoom 1.0 yoffset -80 xalign 0.5
        show text _ ("TRANSLATOR") as text_2:
            zoom 1.5 xalign 0.5 yoffset -30
        show text _ ("TRANSLATOR2"):
            zoom 1.5 xalign 0.5 yoffset 20
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

        $ renpy.pause(4.0, hard='True')

        hide text_1
        hide text_2
        hide text
        $ renpy.transition(Dissolve(0.5))
        $ renpy.pause(0.5, hard='True')

    $ renpy.pause(1.0, hard='True')

    show text _ ("THANK YOU FOR") as text_1:
        zoom 2.0 yoffset -50
    show text _ ("PLAYING THIS GAME") as text_2:
        zoom 2.0 yoffset 40
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    $ renpy.pause(4.0, hard='True')

    hide text_1
    hide text_2
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    stop music fadeout 5.0

    $ renpy.pause(5.0, hard='True')

    if persistent.most_recent_ending == 0:

        jump hint_bad_end

    elif persistent.most_recent_ending == 1:

        jump hint_true_end
    else:


        jump hint_good_end

label hint_bad_end:

    show dead_taylor
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if persistent.num_finish == 1:

        t "...Yo."

        t "Good to see that you’re doing fine."

        t "As you can see... "

        t "I’m very f**ked."

        $ dead_taylor_eyes = 0

        t "*sigh* {w=0.5}What a waste."

        t "They didn’t even finish my intestines."

        $ dead_taylor_eyes = 1

        t "But it’s okay - {w=0.5}this does not need to happen to you."

        t "The thing is... {w=0.5}Albert seems to be using dream therapy as a way to find a certain type of people."

        t "So maybe... {w=0.5}get all the questions right?"

        t "Be as obedient as possible, {w=0.5}don’t question him."

        t "Maybe that way you can save yourself from getting the same fate as I do."

        t "Why don’t you go ahead and find out?"
    else:


        t "...Sup."

        $ dead_taylor_eyes = 1

        t "It looks like we’ve failed again."

        t "But it’s okay, {w=0.5}I know you can do it next time."

        if persistent.unlock_true_end:

            t "It looks like you’ve already unlocked the second bad end."

            t "Then why don’t you try something... {w=0.5}new?"

            t "Try to piss him off as much as possible."

            t "I’m sure that would be fun."
        else:


            t "Why don’t try you getting all the questions right?"

            t "And don’t do anything sneaky."

            t "If he tells you to do something, {w=0.5}you listen to him."

            t "Maybe that way you can save yourself from getting the same fate as I do."

            t "Why don’t you go ahead and find out?"

    return

label hint_true_end:

    show dream_taylor

    $ renpy.pause(8.0, hard='True')

    return

label hint_good_end:

    scene albert_office
    show albert_sitting_phone
    show albert_office_lamp
    show black

    $ albert_is_calling = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/telephone-line-connector.mp3"

    $ renpy.pause(4.0, hard='True')

    v "Hello?"

    hide black

    a_think "......"

    a "It’s been a while, {w=0.5}Vincent."
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
