
define num_rorschach = 6
define num_total_rorschach = 11
define num_rorschach_round = 10
define rorschach_set = set()
define rorschach_list = []
define rorschach_num = 1
define picture_num = 0
define num_flipping = 0

define num_horror_rorschach = 4
define horror_rorschach_set = set()
define horror_rorschach_list = []
define horror_rorschach_num = 1

define word_list = [_("HUMAN"), _("BUTTERFLY"), _("MOTH"), _("FACE"), _("ELEPHANT"), _("RUG"), _("BAT"), _("CRAB"), _("LOBSTER"), _("ROBOT"), _("LEAF"), _("BEAR"), _("RABBIT")]
define word_set = set()
define selected_word_list = [_("HUMAN"), _("BUTTERFLY"), _("MOTH"), _("FACE"), _("ELEPHANT"), _("RUG")]
define num_word = 6
define word_color = "#291E26"


define actual_word_list = [_("CORPSE"), _("DEATH"), _("MURDER"), _("BLOODSHED"), _("DISMEMBERMENT"), _("PSYCHO"), _("SUFFER"), _("REGRET"), _("BUTCHERY"), _("SLAUGHTER")]
define actual_word_set = set()
define selected_actual_word_list = [_("CORPSE"), _("DEATH"), _("MURDER"), _("BLOODSHED"), _("DISMEMBERMENT"), _("PSYCHO")]

define rorschach_feedback = [_("Interesting choice!"),
                             _("Quite the imagination!"),
                             _("Really cool!"),
                             _("Fascinating choice..."),
                             _("Is that what you see?"),
                             _("Hmm... {w=0.5}Okay."),
                             _("Interesting. {w=0.5}Very, {w=0.5}very interesting.")]

define flip_rorschach_feedback = [_("...I would kindly ask you not to do that, {w=0.5}Taylor."),
                                  _("...Why did you flip the paper, {w=0.5}Taylor?"),
                                  _("...Is there anything wrong, {w=0.5}Taylor? {w=0.5}Why did you flip the paper?")]

define flip_rorschach_feedback_index = 0

default persistent.forced_quit = False

label main_menu:


    if persistent.forced_quit:
        return
    else:
        if persistent.unlock_true_end and persistent.most_recent_ending != 2:

            $ renpy.music.play('audio/REVERSE_takeADeepBreath_piano_v2.mp3', channel='music', loop=True)
        else:


            $ renpy.music.play('audio/takeADeepBreath_piano_v2.mp3', channel='music', loop=True)

        call screen main_menu


label rorschach_start:

    a "This section is going to be a lot more fun than the previous ones."

    a "Have you by any chance heard of The Rorschach Test, {w=0.5}Taylor?"

    t "The Rorschach Test?"

    t "Isn’t that the thing where they show you a picture and ask you what you see?"

    a "That is correct!"

    a "It is a psychological test developed in 1921 to measure underlying thought disorder..."

    a "and examine a person’s personality characteristics and emotional functioning."

    a "So for this section, {w=0.5}I will be showing you a series of inkblots..."

    a "and you will tell me what you see in them."

    a "Is that clear?"

    if persistent.unlock_bad_end and persistent.unlock_true_end:

        t_think "(......)"

        t_think "(I always wonder what’s on the back of those inkblots.)"

    t "Yea. {w=0.5}Crystal clear."

    if persistent.num_finish > 0:

        $ renpy.screenshot("scr1")
        $ renpy.save("1-1")
        $ quick_load_ = True
        with Dissolve(0.2)

    $ albert_is_sitting = False

    show black behind taylor_face:
        alpha 0.0
        ease 0.5 alpha 0.5

    show albert_face:
        xpos 1100 ypos 600 rotate_pad 1 rotate 0 zoom 0.01
        parallel:
            ease_circ 1.0 zoom 1.0
        parallel:
            ease 1.0 rotate 1440

    $ renpy.pause(0.5, hard='True')

    a "Alright! {w=0.5}Here we go."

    $ preferences.afm_enable = False
    $ auto_enabled_ = False

    $ picture_num = 0
    $ rorschach_round_num = 1
    $ taylor_see_horror_rorschach = False

    python:

        while len(rorschach_set) != num_rorschach:
            rorschach_set.add(random.randint(1, num_total_rorschach))

        rorschach_list = list(rorschach_set)
        random.shuffle(rorschach_list)


        while len(horror_rorschach_set) != num_horror_rorschach:
            horror_rorschach_set.add(random.randint(1, num_horror_rorschach))

        horror_rorschach_list = list(horror_rorschach_set)
        random.shuffle(horror_rorschach_list)

label rorschach_round:

    python:



        if picture_num == num_rorschach - 1:
            picture_num = 0
            word_color = "E2146B"

        if rorschach_round_num < num_rorschach:
            rorschach_num = rorschach_list[picture_num]
        else:
            horror_rorschach_num = horror_rorschach_list[picture_num]

        word_set = set()
        actual_word_set = set()


        while len(word_set) != num_word:
            word_set.add(word_list[random.randint(0, len(word_list)-1)])
            
            selected_word_list = list(word_set)

        if rorschach_round_num < num_rorschach:
            
            selected_actual_word_list = selected_word_list

        else:
            
            while len(actual_word_set) != num_word:
                actual_word_set.add(actual_word_list[random.randint(0, len(actual_word_list)-1)])
            selected_actual_word_list = list(actual_word_set)



    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/audioblocks-game-low-health-hurt-sound-12.mp3"

    show paper:
        xalign 0.5 ypos -400
        easein_bounce 0.5 ypos 250

    if rorschach_round_num < num_rorschach:

        show rorschach_image as current_rorschach_image:
            xalign 0.5 ypos -400
            easein_bounce 0.5 ypos 250
    else:


        show horror_rorschach_image as current_rorschach_image:
            xalign 0.5 ypos -400
            easein_bounce 0.5 ypos 250

    $ renpy.pause(0.5, hard='True')

    if rorschach_round_num == num_rorschach and not taylor_see_horror_rorschach:

        $ taylor_see_horror_rorschach = True

        show taylor_face_panic:
            xpos 190 ypos 600
        hide taylor_face

    $ renpy.pause(0.01, hard='True')

    show screen empty_screen
    show screen rorschach_problem
    $ renpy.transition(Dissolve(0.3))
    $ renpy.pause(0.3, hard='True')

    ""

label rorschach_round_end:

    a "[feedback!t]"

    $ picture_num += 1
    $ rorschach_round_num += 1

    hide paper
    hide current_rorschach_image
    $ renpy.transition(Dissolve(0.2))
    $ renpy.pause(0.2, hard='True')

    if rorschach_round_num != num_rorschach_round:
        jump rorschach_round

    hide taylor_face_panic
    show taylor_face:
        xpos 190 ypos 600

    a "Good job, {w=0.5}Taylor! {w=0.5}That was incredibly fascinating."

    show black behind taylor_face:
        alpha 0.5
        ease 0.5 alpha 0.0

    show albert_face:
        xpos 1100 ypos 600 rotate_pad 1 rotate 0 zoom 1.0
        parallel:
            ease_circ 1.0 zoom 0.01
        parallel:
            ease 1.0 rotate 1440

    $ renpy.pause(1.0, hard='True')

    hide albert_face
    hide black

    $ albert_is_sitting = True

    jump end

label flip_rorschach:

    $ num_flipping += 1

    hide screen empty_screen
    hide screen rorschach_problem

    $ renpy.music.set_volume(0.3, delay=0, channel='sound')
    play sound "audio/flip page.ogg"

    if rorschach_round_num < num_rorschach:

        show rorschach_image as current_rorschach_image:
            linear 0.2 xzoom 0.001
            alpha 0
    else:


        show taylor_face:
            xpos 190 ypos 600
        hide taylor_face_panic

        show horror_rorschach_image as current_rorschach_image:
            linear 0.2 xzoom 0.001
            alpha 0

    show paper:
        linear 0.2 xzoom 0.001
        linear 0.2 xzoom 1

    if rorschach_round_num == num_rorschach_round - 1 and math_answered_correct == 0 and cup_answered_correct == 0 and num_open_eyes == 4:



        stop music fadeout 3.0

        show vincent:
            xalign 0.5 ypos 250 alpha 0 xzoom 0.001
            pause 0.2
            alpha 1
            linear 0.2 xzoom 1

        $ renpy.pause(4.0, hard='True')

        jump rorschach_vincent_glitch
    else:


        $ renpy.pause(1.0, hard='True')

        $ flip_rorschach_feedback_index = random.randint(0,len(flip_rorschach_feedback)-1)
        $ feedback = flip_rorschach_feedback[flip_rorschach_feedback_index]

        a "[feedback!t]"

        $ renpy.music.set_volume(0.3, delay=0, channel='sound')
        play sound "audio/flip page.ogg"

        if rorschach_round_num < num_rorschach:

            show rorschach_image as current_rorschach_image:
                pause 0.2
                alpha 1
                linear 0.2 xzoom 1
        else:


            show taylor_face_panic:
                xpos 190 ypos 600
            hide taylor_face

            show horror_rorschach_image as current_rorschach_image:
                pause 0.2
                alpha 1
                linear 0.2 xzoom 1

        show paper:
            linear 0.2 xzoom 0.001
            linear 0.2 xzoom 1

        $ renpy.pause(0.4, hard='True')

        show screen empty_screen
        show screen rorschach_problem
        $ renpy.transition(Dissolve(0.3))
        $ renpy.pause(0.3, hard='True')

        ""


label rorschach_vincent_glitch:

    $ auto_enabled_ = True

    t "Damn, {w=0.5}cool drawing you got there."

    t "Didn’t know that you were an artist as well."

    t "Who is that?"

    window hide

    $ renpy.pause(2.0, hard='True')

    window auto

    a_think "......"

    window hide

    $ renpy.pause(2.0, hard='True')

    window auto

    $ renpy.music.set_volume(music_volume, delay=0, channel='music')
    play music ["<silence 1.0>", "audio/skipABeat_v1.mp3"]
    queue music "audio/skipABeat_v1.mp3"

    show albert_office_red behind black:
        alpha 0
        linear 3.0 alpha 1

    a "Why did you do that, {w=0.5}Taylor?"

    a "That wasn’t very nice."

    t "Huh?"

    t "Do what?"

    a "I am quite confident that you know exactly what I’m referring to."

    show taylor_face_awkward:
        xpos 190 ypos 600
    hide taylor_face

    t "Umm... {w=0.5}Why did the background music suddenly change?"

    stop music fadeout 4.0

    window hide

    show albert_face:

        ease_expo 1.0 xpos 190

    $ renpy.pause(0.5, hard='True')

    hide paper
    hide vincent
    hide taylor_face_awkward
    hide albert_face

    $ persistent.forced_quit = True

    stop music
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/monster angry moan.ogg"

    show albert_giant_face
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    show glitch_1
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushup"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    show glitch_2
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
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)
    $ renpy.transition(PushMove(0.1, "pushdown"))
    $ renpy.pause(0.01, hard=True)

    $ renpy.quit()

label recover_force_quit:

    $ persistent.forced_quit = False
    $ quick_menu = True
    $ navigation = True
    $ auto_enabled_ = True
    $ quick_load_ = False


    $ albert_is_talking = False
    $ taylor_is_talking = False
    $ albert_is_sitting = True
    $ add_office_layer_1 = True

    scene albert_office
    show albert_sitting
    show albert_office_lamp
    show albert_office_telephone
    show taylor_face_panic:
        xpos 190 ypos 600

    $ renpy.pause(2.0, hard='True')

    window auto

    t "What, {w=0.5}what the hell just happened!?"

    a "I apologize for my sudden outburst, {w=0.5}Taylor."

    a "That was very rude of me."

    t "Umm... {w=0.5}Don’t worry about it."

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "audio/takeADeepBreath_v1.mp3"

    a "As an apology, {w=0.5}I will answer your question."

    a "That was a classmate of mine from college."

    hide taylor_face_panic
    show taylor_face:
        xpos 190 ypos 600

    t_think "......"

    t "Oh. {w=0.5}Were you guys friends? {w=0.5}Is that why you were drawing him?"

    t "You guys look kinda similar as well."

    a "In fact, {w=0.5}it is quite the opposite."

    a "We were arch-enemies."

    hide taylor_face
    show taylor_face_panic:
        xpos 190 ypos 600

    t "Arch-enemies? {w=0.5}Why’s that?"

    a "No specific reason."

    a "Probably because we looked similar and were both very competent people."

    a "So people loved to compare us to each other."

    a "I was the best student in the class. {w=0.5}He was the second."

    a "He always tried very hard to beat me in school. {w=0.5}But he never succeeded."

    hide taylor_face_panic
    show taylor_face:
        xpos 190 ypos 600

    t_think "......"

    t "Did you like him?"

    a "I guess you could say I admired and despised him at the same time."

    a "He had a lot of potential to be better than me, {w=0.5}yet I witnessed him let them go to waste."

    t "...You enjoyed feeling superior to him, {w=0.5}didn’t you?"

    a_think "......"

    a "...I wouldn’t put it that way."

    t "Then let me put it this way, {w=0.5}you enjoyed the fact that he always saw you as his goal."

    t "And you felt amazing because of that."

    t "You miss him, {w=0.5}don’t you? {w=0.5}And all your friends from G4."

    a_think "......"

    a "That is absurd, {w=0.5}Taylor."

    t "Bullshit. {w=0.5}Or why else would you draw him?"

    t "I know artists only draw things they like."

    t "It must be hard, {w=0.5}going to a foreign district by yourself to pursue education."

    t "But what’s even harder is, {w=0.5}you have to say goodbye to all your friends after graduation."

    t "Why don’t you give them a call sometime?"

    a_think "......"

    a "I’ll think about it."

    window hide

    $ renpy.pause(2.0, hard='True')

    window auto

    jump good_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
