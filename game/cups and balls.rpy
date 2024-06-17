
define cup_positions = [335, 625, 916]
define cup_positions_real = [335, 625, 916]
define cup_index_real = [0, 1, 2]
define has_ball_index = 1
define add_office_layer_1 = False


define total_num_cups_and_balls_problems = 6
define chose_cup_answer = -1
define cup_answered_correct = 0
define cup_speed = 0.5


label cups_and_balls_start:

    a "For this section we’re gonna play a game."

    a "A very classic one."

    a "It is called the shell game."

    a "Have you heard of that?"

    if persistent.num_finish > 1:

        t "...The shell game? {w=0.5}You mean Cups and Balls?"

        a "Yes! {w=0.5}That is correct!"
    else:


        t "...The shell game? {w=0.5}No not really."

        a "It is more commonly known as Cups and Balls."

        t "Oh! {w=0.5}That."

        t "I suck at that game."

    a "Why don’t we give it a try? {w=0.5}What do you think?"

    t "Umm... {w=0.5}Whatever you say."

    $ albert_is_sitting = False

    show black behind taylor_face:
        alpha 0.0
        ease 0.5 alpha 0.5

    show albert_face:
        xpos 1150 ypos -600 rotate_pad 1 rotate 0
        parallel:
            easein_bounce 1.0 xpos 1100 ypos 600
        parallel:
            ease 1.0 rotate 1440

    $ renpy.pause(0.5, hard='True')

    a "Love the enthusiasm!"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/audioblocks-game-low-health-hurt-sound-12.mp3"

    show cup as cup_1:
        xpos cup_positions[0] ypos -400
        easein_bounce 0.5 ypos 250

    show cup as cup_2:
        xpos cup_positions[1] ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250

    show cup as cup_3:
        xpos cup_positions[2] ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    $ renpy.pause(1.0, hard='True')

    a "As you can see, {w=0.5}I have three cups over here."


    hide albert_sitting

    a "And in one of them, {w=0.5}I will be placing a..."

    a_think "......"

    a "Hmmm. {w=0.5}Pardon me, {w=0.5}but it seems that we don’t have any balls here."

    a "Let me go get one."

    window hide

    stop music fadeout 3.0

    show black behind taylor_face:
        alpha 0.5
        ease 0.5 alpha 0.0

    show albert_face:
        xpos 1100 ypos 600 rotate_pad 1 rotate 0
        linear 2.0 xpos 1450 ypos 600

    show cup as cup_1:
        linear 2.0 ypos -400
    show cup as cup_2:
        linear 2.0 ypos -400
    show cup as cup_3:
        linear 2.0 ypos -400

    $ renpy.pause(2.0, hard='True')

    hide albert_face
    hide black
    hide cup_1
    hide cup_2
    hide cup_3

    $ renpy.pause(2.0, hard='True')

    window auto

    t_think "......"

    window hide

    $ renpy.pause(2.0, hard='True')

    window show

    t "Just what in the hell is going on...?"

    if persistent.num_finish > 1:

        t "Why do I feel like I’ve been through this so many times?"

    window hide

    $ renpy.pause(4.0, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/terrified-scream-cartoonish.mp3"

    show taylor_face_panic:
        xpos 190 ypos 600
    hide taylor_face

    $ renpy.pause(2.0, hard='True')

    t "What, {w=0.5}what the f**k was that !?"

    $ add_office_layer_1 = True

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/system-glitch-2.ogg"

    $ renpy.music.set_volume(music_volume, delay=0, channel='music')
    play music "audio/takeADeepBreath_v2.mp3"

    show albert_office_glitch_1 behind taylor_face_panic
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    hide albert_office_glitch_1
    show albert_office_glitch_2 behind taylor_face_panic
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    show glitch_1
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    hide albert_office_glitch_2
    show albert_office_glitch_3 behind taylor_face_panic
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    show albert_sitting_glitch_1
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    hide glitch_1
    show glitch_2
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    hide glitch_2
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    hide albert_office_glitch_3
    hide albert_sitting_glitch_1
    show albert_office behind taylor_face_panic
    show albert_sitting
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)

    $ albert_is_sitting = True

    $ renpy.pause(1.0, hard='True')

    window auto

    a "Thank you for your patience, {w=0.5}Taylor."

    a "I appreciate it very much."

    t "What the hell happened out there???"

    t "Did you hear that???"

    a "Hear what?"

    t "The scream!!!"

    a "What scream?"

    show taylor_face_speechless:
        xpos 190 ypos 600
    hide taylor_face_panic

    t_think "......"

    t_think "(This is a waste of time.)"

    a "Shall we proceed with the therapy?"

    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_speechless

    t_think "......"

    $ albert_is_sitting = False

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/audioblocks-game-low-health-hurt-sound-12.mp3"

    show black behind taylor_face:
        alpha 0.0
        ease 0.5 alpha 0.5

    show albert_face:
        xpos 1150 ypos -600 rotate_pad 1 rotate 0
        parallel:
            easein_bounce 1.0 xpos 1100 ypos 600
        parallel:
            ease 1.0 rotate 1440

    show cup as cup_1:
        xpos cup_positions[0] ypos -400
        easein_bounce 0.5 ypos 250

    show cup as cup_2:
        xpos cup_positions[1] ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250

    show cup as cup_3:
        xpos cup_positions[2] ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    $ renpy.pause(1.0, hard='True')

    a "As you can see, {w=0.5}I have three cups over here."

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/squish.ogg"

    show eyeball behind cup_2:
        xpos cup_positions[1] ypos 330

    show cup as cup_2:
        linear 0.5 ypos 80

    $ renpy.pause(0.5, hard='True')

    show taylor_face_panic:
        xpos 190 ypos 600
    hide taylor_face

    a "And in one of them, {w=0.5}I will be placing a ball under it."

    t "WTF man??? {w=0.5}That’s NOT a ball."

    t "That’s a frickin’ EYEBALL."

    a "An eyeball is a ball. {w=0.5}It is a sphere."

    t "You know that’s NOT what I meant."

    t "WHERE THE HELL DID YOU GET IT???"

    a "It was donated by a former patient."

    if persistent.num_finish > 0:

        t "BULLSHIT. {w=0.5}This was what the scream was about, {w=0.5}wasn’t it?"

        a_think "......"
    else:


        t "WHY WOULD YOU USE THAT FOR CUPS AND BALLS???"

        t "THIS IS MESSED UP."

        a "Actually, {w=0.5}according to the contract, {w=0.5}we are free to use it however we want."

        t "Jesus f**kin’ christ."

        a "Any other inquiries?"

        a "You know, {w=0.5}the faster we finish this section, {w=0.5}the sooner I can put it back."

        t "Okay, {w=0.5}okay! {w=0.5}Jesus christ."

    a "Anyways, {w=0.5}I will be shifting those three cups around."

    a "And you will tell me which one you think has the ball."

    a "Is that clear?"

    if persistent.num_finish > 0:

        t "ANSWER MY QUES - "

        $ renpy.screenshot("scr1")
        $ renpy.save("1-1")
    else:


        t "Yes. {w=0.5}I know how the game works."

    show cup as cup_2:
        linear 0.5 ypos 250

    a "Perfect! {w=0.5}Here we go."

    if persistent.num_finish > 0:

        show taylor_face_speechless:
            xpos 190 ypos 600
        hide taylor_face_panic

        t_think "......"

        $ quick_load_ = True
        with Dissolve(0.2)

    $ preferences.afm_enable = False
    $ auto_enabled_ = False

    hide eyeball

    show cup as cup_1:
        xpos cup_positions[0] ypos 250

    show cup as cup_2:
        xpos cup_positions[1] ypos 250

    show cup as cup_3:
        xpos cup_positions[2] ypos 250

    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_panic
    hide taylor_face_speechless

    $ cup_shift_turn = 0
    $ cup_positions_real[0] = 335
    $ cup_positions_real[1] = 625
    $ cup_positions_real[2] = 916

    $ cup_index_real[0] = 0
    $ cup_index_real[1] = 1
    $ cup_index_real[2] = 2

    $ has_ball_index = 1
    $ current_cups_and_balls_round = 0

label shift_cup:

    show screen empty_screen

    python:

        cup_index_1 = random.randint(0,2)
        cup_index_2 = random.randint(0,2)
        while cup_index_2 == cup_index_1:
            cup_index_2 = random.randint(0,2)

        temp_store_cup_position = cup_positions_real[cup_index_2]
        cup_positions_real[cup_index_2] = cup_positions_real[cup_index_1]
        cup_positions_real[cup_index_1] = temp_store_cup_position

        temp_store_cup_index = cup_index_real[cup_index_2]
        cup_index_real[cup_index_2] = cup_index_real[cup_index_1]
        cup_index_real[cup_index_1] = temp_store_cup_index

        if cup_index_real[cup_index_1] == has_ball_index:
            has_ball_index = cup_index_real[cup_index_2]
        elif cup_index_real[cup_index_2] == has_ball_index:
            has_ball_index = cup_index_real[cup_index_1]

    $ renpy.pause(cup_speed, hard='True')

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/audioblocks-arcade-fast-metallic-boost.mp3"

    show cup as cup_1:
        ease cup_speed xpos cup_positions_real[0]

    show cup as cup_2:
        ease cup_speed xpos cup_positions_real[1]

    show cup as cup_3:
        ease cup_speed xpos cup_positions_real[2]




    if cup_shift_turn != 3:

        $ cup_shift_turn += 1
        jump shift_cup

    $ renpy.pause(0.5, hard='True')

    show screen empty_screen
    show screen cups_and_balls_problem

    n2 "Select the correct cup:"

label end_of_cups_and_balls_question:


    $ current_cups_and_balls_round += 1

    $ cup_speed -= 0.09

    hide screen empty_screen
    hide screen cups_and_balls_problem

    show cup as cup_1:
        xpos cup_positions[0] ypos 250

    show cup as cup_2:
        xpos cup_positions[1] ypos 250

    show cup as cup_3:
        xpos cup_positions[2] ypos 250

    $ cup_positions_real[0] = 335
    $ cup_positions_real[1] = 625
    $ cup_positions_real[2] = 916

    if chose_cup_answer == 0:

        show cup as cup_1:
            linear 0.5 ypos 80

        if chose_cup_answer == has_ball_index:
            show eyeball behind cup_1:
                xpos cup_positions[0] ypos 330

    elif chose_cup_answer == 1:

        show cup as cup_2:
            linear 0.5 ypos 80

        if chose_cup_answer == has_ball_index:
            show eyeball behind cup_2:
                xpos cup_positions[1] ypos 330

    elif chose_cup_answer == 2:

        show cup as cup_3:
            linear 0.5 ypos 80

        if chose_cup_answer == has_ball_index:
            show eyeball behind cup_3:
                xpos cup_positions[2] ypos 330




    a "[feedback!t]"


    if chose_cup_answer != has_ball_index:

        a "The correct answer is - "

        if has_ball_index == 0:

            show cup as cup_1:
                linear 0.5 ypos 80

            show eyeball behind cup_1:
                xpos cup_positions[0] ypos 330

        elif has_ball_index == 1:

            show cup as cup_2:
                linear 0.5 ypos 80

            show eyeball behind cup_2:
                xpos cup_positions[1] ypos 330

        elif has_ball_index == 2:

            show cup as cup_3:
                linear 0.5 ypos 80

            show eyeball behind cup_3:
                xpos cup_positions[2] ypos 330

        a "Ta da!"


        if current_cups_and_balls_round != total_num_cups_and_balls_problems:

            a "Let’s try again."

    show cup as cup_1:
        linear 0.5 xpos cup_positions[0] ypos 250

    show cup as cup_2:
        linear 0.5 xpos cup_positions[1] ypos 250

    show cup as cup_3:
        linear 0.5 xpos cup_positions[2] ypos 250

    $ renpy.pause(0.5, hard='True')

    hide eyeball

    if current_cups_and_balls_round == total_num_cups_and_balls_problems - 2:

        hide albert_sitting
        hide albert_sitting_glitch_3
        show albert_sitting_glitch_2 behind black

    elif current_cups_and_balls_round == total_num_cups_and_balls_problems -3:

        hide albert_sitting
        hide albert_sitting_glitch_2
        show albert_sitting_glitch_3 behind black
    else:


        hide albert_sitting_glitch_2
        hide albert_sitting_glitch_3
        show albert_sitting behind black


    if current_cups_and_balls_round != total_num_cups_and_balls_problems:

        $ cup_shift_turn = 0

        jump shift_cup





    show albert_office_lamp behind black:
        xoffset 100

    show albert_office_telephone behind black:
        xoffset 160

    if cup_answered_correct == total_num_cups_and_balls_problems:

        a "Impressive job, {w=0.5}Taylor! {w=0.5}You spotted all of them!"

    elif cup_answered_correct > total_num_cups_and_balls_problems/2:

        a "Good job, {w=0.5}Taylor! {w=0.5}You managed to spot most of them."

    elif cup_answered_correct > 0 and cup_answered_correct <= total_num_cups_and_balls_problems/2:

        a "Good effort, {w=0.5}Taylor!"

        a "Your performance wasn’t the best but I know you will do better next time!"

    elif cup_answered_correct == 0:

        a_think "......"

        a "I see that it was a bit too difficult for you. "

        a "But no need to worry, {w=0.5}it’s not a big deal."

    show black:
        linear 1.0 alpha 0

    show cup as cup_1:
        linear 3.0 xpos cup_positions[0]-1200 ypos 250

    show cup as cup_2:
        linear 3.0 xpos cup_positions[1]-1200 ypos 250

    show cup as cup_3:
        linear 3.0 xpos cup_positions[2]-1200 ypos 250

    show albert_office_lamp:
        linear 0.3 xoffset 0

    show albert_office_telephone:
        linear 0.4 xoffset 0

    show albert_face:
        xpos 1100 ypos 600 rotate_pad 1 rotate 0
        linear 2.0 xpos 1450 ypos 600

    $ renpy.pause(3.0, hard='True')

    hide cup_1
    hide cup_2
    hide cup_3
    hide black
    hide albert_face

    if persistent.num_finish > 0:
        $ quick_load_ = False
        with Dissolve(0.2)

    jump break_2_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
