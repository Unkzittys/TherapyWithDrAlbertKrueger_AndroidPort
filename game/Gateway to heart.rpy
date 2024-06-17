define num_open_eyes = 0
define next_label = "gateway_to_heart_q_2"

label gateway_to_heart_start:

    a "This section is a bit different."

    a "It is not a game or a test, {w=0.5}but a way for me to get to know you better."

    a "Or as how I usually like to call it... {w=0.5}the gateway to your heart."

    t "The gateway to my heart?"

    a "Yes. {w=0.5}I will be asking you a series of questions, {w=0.5}and I’d like you to answer them honestly."

    t "Huh? {w=0.5}What kind of questions?"

    a "All kinds of questions. {w=0.5}Questions that are... {w=0.5}about you."

    t_think "......"

    t "Nah. {w=0.5}I’ll pass."

    a "It is an integral part of the therapy. {w=0.5}Abstaining is not an option."

    t "...This ain’t fair, {w=0.5}you know?"

    t "I didn’t sign up for any of this. "

    t "Why do I have to tell you anything about me?"

    a "Hmm... {w=0.5}Well, {w=0.5}I guess I can modify this part a little bit."

    a "How about each time you tell me something about you, {w=0.5}I’ll tell you something about me in return?"

    t "Hmm... {w=0.5}That’s tempting."

    t "But how do I know if you’re lying or not?"

    a "Trust is extremely important between a patient and their therapist."

    a "It is essential for the work to go as far as it needs to."

    show taylor_face_speechless:
        xpos 190 ypos 600
    hide taylor_face

    t_think "......"

    t "Ok fine, {w=0.5}whatever."

    a "Excellent! {w=0.5}However, {w=0.5}I do have one request:"

    a "You’ll have to close your eyes for this section."

    a "And no matter what happens - {w=0.5}you can’t open your eyes till I tell you to do so."

    a "Can I trust you on that?"

    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_speechless

    t_think "......"

    stop music fadeout 3.0

    show taylor_face_close_eye:
        xpos 190 ypos 600
    hide taylor_face

    show close_eye_animation behind taylor_face_close_eye

    $ renpy.pause(0.01, hard='True')

    show taylor_face_outline with Dissolve(0.3):
        xpos 190 ypos 600

    $ renpy.pause(3.0, hard='True')

    t "Like this?"

    a "Yes! {w=0.5}Perfect."

    if persistent.num_finish > 0:

        $ renpy.screenshot("scr1")
        $ renpy.save("1-1")
        $ quick_load_ = True
        with Dissolve(0.2)

    a "My first question is -"

    a "What was it like growing up in your family?"

    t "Hmm... {w=0.5}Nothing extra-ordinary."

    t "My parents were immigrants who came to G2 to seek opportunities."

    t "I had two siblings, {w=0.5}and we used to all live under the same roof with our parents."

    t "Sometimes it gets a little bit annoying, {w=0.5}but as a whole it was a pretty happy experience."

    t "What about you? {w=0.5}What was your family like?"

    a "It was also quite ordinary."

    a "Both of my parents were well-known figures in the medical field."

    a "They were very busy people."

    a "However, {w=0.5}what’s different from you is, {w=0.5}I was the only child."

    if persistent.num_finish > 0:

        t "Damn. {w=0.5}That must be nice. {w=0.5}Getting all the love and attention."

        a_think "......"

        a "I guess you could say so."

        if persistent.unlock_bad_end and persistent.unlock_true_end:

            a "But sometimes it gets a little lonely."

            t_think "......"

            t "...I see."
    else:


        t "I, {w=0.5}I see."

    $ next_label = "gateway_to_heart_q_2"

    $ preferences.afm_enable = False
    $ auto_enabled_ = False


    if persistent.lang == "korean":
        $ gateway_yes_xpos = 270
        $ gateway_no_xpos = 820
    else:
        $ gateway_yes_xpos = 410
        $ gateway_no_xpos = 860

    show screen empty_screen

    show screen yes_no_countdown(0.5)

    t_think "(Should I open my eyes?)" with Dissolve(1.0)

label gateway_to_heart_q_2:

    hide screen empty_screen
    hide screen open_eyes_decision_screen

    $ renpy.pause(1.0, hard='True')

    $ auto_enabled_ = True

    a "My second question is -"

    a "How connected do you feel to the people around you?"

    t "Hmm..."

    t "Well, {w=0.5}I’m not very popular in schools."

    t "But I do have a few good friends that I feel deeply connected to."

    t "And my family as well."

    t "We understand and respect each other very well."

    a "That’s good. "

    a "It is important to have friends and families that support you."

    t "Well, {w=0.5}what about you? {w=0.5}Do you feel connected to the people around you?"

    a_think "......"

    a "Of course. "

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound ["<silence 0.5>", "audio/fighting.ogg"]

    a "I feel deeply connected to all my patients. {w=0.5}They all mean a lot to me."

    t "...I guess that’s very professional of you."

    if persistent.num_finish > 0:

        t "But what about your family? {w=0.5}Or your friends?"

        a_think "......"

        t "Is there really no one else that you feel connected to besides your patients?"

        a_think "......"

    t_think "(What the hell were all these noises?)" with Dissolve(1.0)

    $ next_label = "gateway_to_heart_q_3"

    $ preferences.afm_enable = False
    $ auto_enabled_ = False


    if persistent.lang == "korean":
        $ gateway_yes_xpos = 270
        $ gateway_no_xpos = 820
    else:
        $ gateway_yes_xpos = 410
        $ gateway_no_xpos = 860

    show screen empty_screen

    show screen yes_no_countdown(0.5)

    t_think "(Should I open my eyes?)" with Dissolve(1.0)

label gateway_to_heart_q_3:

    hide screen empty_screen
    hide screen open_eyes_decision_screen

    $ renpy.pause(1.0, hard='True')

    $ auto_enabled_ = True

    a "Next question -"

    a "If you could wave a magic wand, {w=0.5}what positive changes would you make happen in your life?"

    t "Hmm... {w=0.5}That’s a tough one."

    t "There’s really nothing I’d like to change."

    t "I like everything the way it is right now."

    a "Interesting response."

    a "It is always important to appreciate what you have at hand."

    t "Well, {w=0.5}let’s hear yours. {w=0.5}What would you change?"

    a "Hmm..."

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music ["<silence 0.5>", "audio/weird-detuned-guitar-sounds.mp3"]
    queue music "audio/weird-detuned-guitar-sounds.mp3"

    a "I guess the world could have less mediocre people."

    t_think "......"

    t "Excuse me?"

    a "I’m just joking. "

    a "I love my life and everything about it."

    a "There’s nothing that needs to be changed."

    t_think "......"

    t_think "(Something feels off.)" with Dissolve(1.0)

    t_think "(And what is this weird guitar sound?)" with Dissolve(1.0)

    $ next_label = "gateway_to_heart_q_4"

    $ preferences.afm_enable = False
    $ auto_enabled_ = False


    if persistent.lang == "korean":
        $ gateway_yes_xpos = 270
        $ gateway_no_xpos = 820
    else:
        $ gateway_yes_xpos = 410
        $ gateway_no_xpos = 860

    show screen empty_screen

    show screen yes_no_countdown(0.5)

    t_think "(Should I open my eyes?)" with Dissolve(1.0)

label gateway_to_heart_q_4:

    stop music fadeout 1.0

    hide screen empty_screen
    hide screen open_eyes_decision_screen

    $ renpy.pause(1.0, hard='True')

    $ auto_enabled_ = True

    a "Last question - "

    a "Have you ever had the urge..."

    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    play music "audio/killer-scene-with-breath-and-scream_.ogg"

    a "To murder someone in your life?"

    a "Or maybe dismember them, {w=0.5}chop them into pieces..."

    a "And make them into a hamburger?"

    t "Ex... {w=0.5}excuse me?"

    t "Of course not! {w=0.5}This is messed up."

    t "Have... {w=0.5}have you???"

    a "I personally take a dislike to hamburgers, {w=0.5}so no."

    t "That’s - {w=0.5}that’s not -"

    t_think "......"

    t_think "(I’m feeling really uneasy.)" with Dissolve(1.0)

    $ next_label = "break_3_start"

    $ preferences.afm_enable = False
    $ auto_enabled_ = False


    if persistent.lang == "korean":
        $ gateway_yes_xpos = 270
        $ gateway_no_xpos = 820
    else:
        $ gateway_yes_xpos = 410
        $ gateway_no_xpos = 860

    show screen empty_screen

    show screen yes_no_countdown(0.5)

    t_think "(Should I open my eyes?)" with Dissolve(1.0)


label Open_eyes:

    stop music fadeout 1.0

    hide screen empty_screen
    hide screen open_eyes_decision_screen


    $ num_open_eyes += 1

    $ renpy.pause(0.2, hard='True')

    if num_open_eyes == 3:

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "audio/horror-metallic-screeches.mp3"

        show creepy_face_1 behind close_eye_animation:
            xpos 600 zoom 1.0
            linear 0.7 xpos 1600 zoom 1.0

    if num_open_eyes == 4:

        window hide

        $ renpy.music.set_volume(0.8, delay=0, channel='sound')
        play sound "audio/sapisvr__squeaky-jumpscare-2.wav"

        show albert_giant_face behind close_eye_animation:

            parallel:

                zoom 0.1

                linear 0.5 zoom 1
            parallel:


                linear 0.01 yoffset -100

                linear 0.01 yoffset 100

                repeat

    hide close_eye_animation
    show open_eye_animation behind taylor_face_close_eye
    show taylor_face_open_eye:
        xpos 190 ypos 600
    $ renpy.pause(0.5, hard='True')
    hide taylor_face_open_eye
    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_outline with Dissolve(0.3)

    if num_open_eyes == 1:

        $ renpy.pause(1.0, hard='True')

        $ auto_enabled_ = True

        a "Why did you open your eyes, {w=0.5}Taylor?"

        t_think "......"

        hide open_eye_animation
        show taylor_face_close_eye:
            xpos 190 ypos 600
        hide taylor_face

        show close_eye_animation behind taylor_face_close_eye

        $ renpy.pause(0.01, hard='True')

        show taylor_face_outline with Dissolve(0.3):
            xpos 190 ypos 600

    elif num_open_eyes == 2:

        $ renpy.pause(1.0, hard='True')

        $ auto_enabled_ = True

        a "...Is there anything wrong, {w=0.5}Taylor?"

        t_think "......"

        t "...No, {w=0.5}nothing."

        hide open_eye_animation
        show taylor_face_close_eye:
            xpos 190 ypos 600
        hide taylor_face

        show close_eye_animation behind taylor_face_close_eye

        $ renpy.pause(0.01, hard='True')

        show taylor_face_outline with Dissolve(0.3):
            xpos 190 ypos 600

    elif num_open_eyes == 3:

        show taylor_face_panic:
            xpos 190 ypos 600
        hide taylor_face

        $ renpy.pause(4.0, hard='True')

        $ auto_enabled_ = True

        t "What the f**k was that!?"

        a "Taylor, {w=0.5}I would kindly ask you to refrain from using such words."

        t "NO BUT WHAT THE ACTUAL F**K.{w=0.5} WHAT WAS THAT THING???"

        a "I unfortunately have no clue what you’re referring to."

        a "It seems to me that you could be over-stressed, {w=0.5}and thus had some form of hallucination."

        t "NO I SWEAR TO GOD -"

        a "Do me a favor, {w=0.5}will you, {w=0.5}Taylor?"

        a "Close your eyes, {w=0.5}and take a few deep breaths."

        show taylor_face_speechless:
            xpos 190 ypos 600
        hide taylor_face_panic

        t_think "......"

        t_think "(You just can’t with this dude huh?)"

        show taylor_face:
            xpos 190 ypos 600
        hide taylor_face_speechless

        hide open_eye_animation
        show taylor_face_close_eye:
            xpos 190 ypos 600
        hide taylor_face

        show close_eye_animation behind taylor_face_close_eye

        $ renpy.pause(0.01, hard='True')

        show taylor_face_outline with Dissolve(0.3):
            xpos 190 ypos 600

    elif num_open_eyes == 4:

        if persistent.num_finish > 0:
            $ quick_load_ = False

        show taylor_face_panic:
            xpos 190 ypos 600
        hide taylor_face

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
        $ renpy.transition(PushMove(0.1, "pushup"))
        $ renpy.pause(0.01, hard=True)
        $ renpy.transition(PushMove(0.1, "pushdown"))
        $ renpy.pause(0.01, hard=True)
        $ renpy.transition(PushMove(0.1, "pushup"))
        $ renpy.pause(0.01, hard=True)

        hide albert_giant_face
        scene black
        show cat_mouse_animation
        show text _ ("We'll be \nright back"):
            zoom 5.0

        stop sound
        $ renpy.pause(0.01, hard=True)

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "audio/sfx-censored-bleep--long.ogg"

        $ renpy.pause(5.0, hard='True')

        $ renpy.music.set_volume(1.0, delay=0, channel='sound')
        play sound "audio/system-glitch-2.ogg"

        $ renpy.transition(PushMove(0.1, "pushup"))
        $ renpy.pause(0.01, hard=True)
        $ renpy.transition(PushMove(0.1, "pushup"))
        $ renpy.pause(0.01, hard=True)
        $ renpy.transition(PushMove(0.1, "pushup"))
        $ renpy.pause(0.01, hard=True)

        jump break_3_start

    $ renpy.jump(next_label)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
