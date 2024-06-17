init python:
    import random
    import time

style default:
    antialias False


define math_answers = [0,0,0,0]
define total_num_math_problems = 10
define math_answered_correct = 0

define compliments = [_("Wow! {w=0.5}Amazing!"),
                      _("Excellent job!"),
                      _("I can’t believe it! {w=0.5}Nicely done!"),
                      _("Magnificent!"),
                      _("Impressive!"),
                      _("Tres bien! {w=0.5}Tres bien!")]

define non_compliments = [_("That’s a pity. {w=0.5}You were so close!"),
                          _("You almost got it!"),
                          _("Try a little harder!"),
                          _("Not quite. {w=0.5}But I appreciate the effort!"),
                          _("No that wasn't quite right."),
                          _("You must be talented at something else!"),
                          _("Interesting choice... {w=0.5}Next time possibly."),
                          _("Just try a little harder! {w=0.5}Next time you’ll get it…")]

define feedback = ""


define music_volume = 0.5
define quick_load_ = False

label splashscreen:

    if not persistent.forced_quit:

        if persistent.select_lang is False:
            call screen language_selection_screen


        scene dino game-small
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')
        with Pause(1)
        $ renpy.pause(0.1, hard='True')
        pause 1.8
        $ renpy.pause(0.1, hard='True')
        scene black
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')
        with Pause(1)

        show text _ ("WARNING") as text_1:
            xalign 0.5 ypos warning_title_ypos zoom 3.0
        show text _ ("As required by G2 law we must inform that this therapy \nmay contain aspects that certain patients may find uncomfortable:") as text_2:
            xalign 0.5 ypos 250
        show text _ ("• Jumpscares\n• Loud noises\n• Disturbing and flashing images\n• Implied violence\n• Cartoon gore") as text_3:
            xalign 0.5 ypos 425
        show text _ ("Proceed at your own risk.") as text_4:
            xalign 0.5 ypos 600
        $ renpy.pause(5.0, hard='True')
        $ renpy.pause(0.1, hard='True')
        scene black
        $ renpy.transition(Dissolve(1.0))
        $ renpy.pause(1.0, hard='True')
        with Pause(1)

    return




init:

    $ config.keymap['self_voicing'].remove('v')
    $ config.keymap['self_voicing'].remove('V')
    $ config.keymap['hide_windows'].remove('h')
    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['toggle_skip'].remove('K_TAB')
    $ config.keymap['fast_skip'].remove('>')
    $ config.keymap['clipboard_voicing'].remove('C')
    $ config.keymap['rollforward'].remove('mousedown_5')
    $ config.keymap['rollforward'].remove('K_PAGEDOWN')
    $ config.keymap['rollforward'].remove('repeat_K_PAGEDOWN')
    $ config.keymap['rollback'].remove('K_PAGEUP')
    $ config.keymap['rollback'].remove('repeat_K_PAGEUP')
    $ config.keymap['rollback'].remove('K_AC_BACK')
    $ config.keymap['rollback'].remove('mousedown_4')
    $ config.keymap['game_menu'].remove('K_ESCAPE')
    $ config.keymap['game_menu'].remove('K_MENU')
    $ config.keymap['game_menu'].remove('mouseup_3')
    $ config.keymap['self_voicing'] = []
    $ config.keymap['clipboard_voicing'] = []
    $ config.keymap['toggle_skip'] = []
    $ config.keymap['accessibility'] = ['shift_K_a']



label start:

    if persistent.forced_quit:
        jump recover_force_quit


    $ albert_is_talking = False
    $ taylor_is_talking = False
    $ albert_is_sitting = True
    $ add_office_layer_1 = False
    $ auto_enabled_ = True
    $ quick_load_ = False


    stop music fadeout 5.0
    scene black
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(2.0, hard='True')

    window hide

    o "L-E-E? {w=0.5}Taylor Lee?"

    o "Dr. Krueger is waiting for you at Room 1015."

    if persistent.num_finish > 0:

        t "...I’ll be right there."
    else:


        t "Huh? {w=0.5}Wait a second -"

    $ renpy.music.set_volume(0.6, delay=0, channel='sound')
    play sound "audio/camera.ogg"

    show taylor_medical_card:
        xalign -5.0 yalign -1.0 rotate_pad 1 rotate 0
        parallel:
            ease_circ 0.8 xalign 0.5 yalign 0.5
        parallel:
            ease 0.8 rotate 1440

    show white:
        alpha 1
        0.3
        linear 1.8 alpha 0

    $ renpy.pause(2.0, hard='True')

    show medical_card_speech_bubble
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')

    $ renpy.pause(2.0, hard='True')

    scene black
    $ renpy.transition(Dissolve(1.0))
    $ renpy.pause(2.0, hard='True')

    if persistent.unlock_bad_end and persistent.unlock_true_end:

        a_think "I close my eyes, {w=0.5}then I drift away~"

        a_think "Into the magic night, {w=0.5}I softly say~"

        a_think "A silent prayer like dreamers do~"

        a_think "Then I fall asleep to dreams, {w=0.5}my dreams of you~"

        a_think "In dreams I walk with you~ {w=0.5}in dreams I talk to you~"

        a_think "In dreams you’re mine~ {w=0.5}all of the time~"

        a_think "In dreams you’re mine~ {w=0.5}all of the time~"

        a_think "We’re together in dreams~ {w=0.5}in dreams~"

        window hide

        $ renpy.pause(4.0, hard='True')

    window auto

    $ renpy.music.set_volume(music_volume, delay=0, channel='music')
    play music "audio/takeADeepBreath_v2.mp3"

    scene albert_office
    show albert_sitting



    $ renpy.pause(4.0, hard='True')



    show taylor_face:
        xpos 190 ypos 600
    $ renpy.transition(Dissolve(0.5))
    $ renpy.pause(0.5, hard='True')

    if persistent.num_finish > 0:

        $ variation_1 = variation_1_all[random.randint(0, len(variation_1_all)-1)]

        t_think "[variation_1!t]"

    t "Where... {w=0.5}where the hell am I?"

    a "Welcome to Krueger Health Solutions Corporation."

    a "We are the largest leading multi-specialty medical groups in G2 District... "

    a "delivering more than one million patient visits each year."

    a "I am Dr. Albert Gerald Krueger. {w=0.5}And I will be in charge of your dream therapy today."

    t "...What? {w=0.5}I am not sick."

    t "And what the hell is a dream therapy? "

    t "That sounds like such a scam."

    a "Do not be afraid, {w=0.5}my child."

    a "I’ll have you know that I am a professional and I have a PhD in Marine Biology."

    t "…Do I look like a dolphin to you???"

    if persistent.num_finish > 0:

        $ variation_2 = variation_2_all[random.randint(0, len(variation_2_all)-1)]

        a "[variation_2!t]"

    a "Before we start our session, {w=0.5}I’d like to go over your basic information."

    a "What is your name, {w=0.5}my child?"

    t "...Taylor Lee."

    a "Age?"

    t "19."

    a "Pronouns?"

    t "They/Them."

    a "What brings you here today and what are your symptoms?"

    t "??? {w=0.5}I said I am not sick."

    a "Very well."

    a "Why don't we start with a sanity check?"

    a "Do you enjoy Math, {w=0.5}Taylor?"

    t "...Not particularly."

    a "Perfect! {w=0.5}Then let's start with some simple Math."

    a "The rule is very simple."

    a "I’ll show you a question, {w=0.5}and you’ll need to choose the correct answer..."

    a "from the four cards I provide you."

    a "Does that sound good?"

    t_think "......"

    if persistent.num_finish > 0:

        if not persistent.save_tut:

            t "I do have one request."

            t "I’d like to save right now, {w=0.5}just in case I mess up."

            a "No Taylor, {w=0.5}I would count that as cheating."

            t "Well people mess up, {w=0.5}you know?"

            t "Sometime I get a little bit too nervous that I get the question wrong."

            t "But that way it wouldn’t be a true reflection of my ability, {w=0.5}don’t you think?"

            a_think "......"

            a "Hmm... {w=0.5}You do have a point."

            a "Then how about this; {w=0.5}I will save for you once before each section starts."

            a "But you will only be able to load before the section finishes."

            a "Once it’s beyond that point, {w=0.5}you can no longer come back and redo the questions."

            a "You will see the load button under the text box."

            a "Does that sound good?"

            $ renpy.screenshot("scr1")
            $ renpy.save("1-1")

            t "...Fair enough."

            $ persistent.save_tut = True
        else:


            t "...Whatever."

            $ renpy.screenshot("scr1")
            $ renpy.save("1-1")
    else:



        t "...Whatever."

    $ albert_is_sitting = False

    show black behind taylor_face:
        alpha 0.0
        ease 0.5 alpha 0.5

    show albert_face:
        xpos 1450 ypos 600 rotate_pad 1 rotate 0
        parallel:
            ease_circ 1.0 xpos 1100 ypos 600
        parallel:
            ease 1.0 rotate 1440

    $ renpy.pause(0.5, hard='True')

    a "Alright! {w=0.5}Let’s get started."

    if persistent.num_finish > 0:
        $ quick_load_ = True

    $ auto_enabled_ = False
    $ preferences.afm_enable = False


    python:
        num_1 = 0
        num_2 = 0
        math_symbols = ['+', '-', '*', '/']

        correct_answer = 0
        correct_answer_num = 0;

        current_question = 1;

label repeat_math:

    python:

        for x in range(0,4):
            math_answers[x] = 0

        while True:
            num_1 = random.randint(1,9)
            num_2 = random.randint(1,9)
            math_symbol_index = random.randint(0,3)
            math_symbol = math_symbols[math_symbol_index]
            
            if math_symbol == '+':
                correct_answer = num_1 + num_2
                break
            elif math_symbol == '-':
                correct_answer = num_1 - num_2
                if correct_answer >= 0:
                    break
            elif math_symbol == '*':
                correct_answer = num_1 * num_2
                if correct_answer < 20:
                    break
            elif math_symbol == '/':
                correct_answer = num_1 / num_2
                if num_1 % num_2 == 0:
                    break

        correct_answer_num = random.randint(1,4)

        math_answers[correct_answer_num - 1] = correct_answer

        for x in range(0,4):
            if x != (correct_answer_num - 1):
                math_answers[x] = random.randint(1,9)
                y = 0
                while y != 4:
                    if y != x:
                        if math_answers[x] != math_answers[y]:
                            y += 1
                        else:
                            math_answers[x] = random.randint(1,9)
                            y = 0
                    else:
                        y += 1


    image math_answer_1:
        xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5
        contains:
            Text(str(math_answers[0]), font="GenericMobileSystem.ttf", size=40)
            xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 zoom 5.0

    image math_answer_2:
        xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5
        contains:
            Text(str(math_answers[1]), font="GenericMobileSystem.ttf", size=40)
            xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 zoom 5.0

    image math_answer_3:
        xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5
        contains:
            Text(str(math_answers[2]), font="GenericMobileSystem.ttf", size=40)
            xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 zoom 5.0

    image math_answer_4:
        xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5
        contains:
            Text(str(math_answers[3]), font="GenericMobileSystem.ttf", size=40)
            xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5 zoom 5.0

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/arcade-game-over-2.mp3"

    show card as card_1:
        xpos 285 ypos -400
        easein_bounce 0.5 ypos 250

    show math_answer_1:
        xpos 285 ypos -400
        easein_bounce 0.5 ypos 250

    show card as card_2:
        xpos 525 ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250

    show math_answer_2:
        xpos 525 ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250

    if current_question == total_num_math_problems:
        show bloody_card as card_3:
            xpos 765 ypos -400
            pause 0.2
            easein_bounce 0.5 ypos 250
    else:
        show card as card_3:
            xpos 765 ypos -400
            pause 0.2
            easein_bounce 0.5 ypos 250

    show math_answer_3:
        xpos 765 ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    show card as card_4:
        xpos 1005 ypos -400
        pause 0.3
        easein_bounce 0.5 ypos 250

    show math_answer_4:
        xpos 1005 ypos -400
        pause 0.3
        easein_bounce 0.5 ypos 250

    with Dissolve(0.5)

    if current_question == total_num_math_problems:


        $ renpy.pause(0.1, hard='True')

        n "[num_1][math_symbol][num_2]=?{nw}" with Dissolve(1.0)
        jump bloody_card_convo

label finish_bloody_card_convo:


    $ renpy.pause(0.1, hard='True')

    show screen math_countdown(0.8)
    show screen empty_screen

    n "[num_1][math_symbol][num_2]=?" with Dissolve(1.0)

label end_of_math_problem:

    a "[feedback!t]"

    hide card_1
    hide card_2
    hide card_3
    hide card_4
    hide math_answer_1
    hide math_answer_2
    hide math_answer_3
    hide math_answer_4
    $ renpy.transition(Dissolve(0.1))
    $ renpy.pause(0.1, hard='True')

    if current_question != total_num_math_problems:
        $ current_question += 1
        jump repeat_math
    else:
        jump finish_math

label bloody_card_convo:


    $ renpy.pause(0.5, hard='True')

    show taylor_face_panic:
        xpos 190 ypos 600
    hide taylor_face

    show bloody_card as card_3:
        xpos 765 ypos 250
        easein_bounce 0.5 ypos -400
    show math_answer_3:
        xpos 765 ypos 250
        easein_bounce 0.5 ypos -400


    $ renpy.pause(0.5, hard='True')

    show card as card_3:
        xpos 765 ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    show math_answer_3:
        xpos 765 ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    $ renpy.pause(1.0, hard='True')

    $ auto_enabled_ = True

    a "Oops. {w=0.5}My apologies."

    t "What the hell??? {w=0.5}Was that blood???"

    a "No it wasn’t."

    t "That most definitely was!"

    a "No it wasn’t. "

    a "Now Taylor, {w=0.5}time is ticking."

    a "Focus on your question first."

    $ preferences.afm_enable = False
    $ auto_enabled_ = False

    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_panic

    t_think "......"

    jump finish_bloody_card_convo

label finish_math:

    if math_answered_correct == total_num_math_problems:

        a "Wonderful job, {w=0.5}Taylor! {w=0.5}You got all of them correct!"

    elif math_answered_correct > total_num_math_problems/2:

        a "You got most of them right! {w=0.5}Good job!"

    elif math_answered_correct > 0 and math_answered_correct <= total_num_math_problems/2:

        a "You got a few of them right! {w=0.5}Could be a lot better but I know you tried your best."

    elif math_answered_correct == 0:

        a_think "......"

        a "This isn’t your strong suit, {w=0.5}is it?"

    show black behind taylor_face:
        alpha 0.5
        ease 0.5 alpha 0.0

    show albert_face:
        xpos 1100 ypos 600 rotate_pad 1 rotate 0
        parallel:
            ease_circ 1.0 xpos 1450 ypos 600
        parallel:
            ease 1.0 rotate 1440

    $ renpy.pause(1.0, hard='True')

    hide albert_face
    hide black

    $ albert_is_sitting = True

    if persistent.num_finish > 0:
        $ quick_load_ = False
        with Dissolve(0.2)

    jump break_1_start



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
