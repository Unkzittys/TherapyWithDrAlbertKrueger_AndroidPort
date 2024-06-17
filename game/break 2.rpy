
define albert_is_calling = False

label break_2_start:

    $ albert_is_sitting = True

    $ auto_enabled_ = True

    a "Let’s take another break, {w=0.5}shall we?"

    t "...Sure."

    a "Awesome. {w=0.5}Let me turn up the music."

    python:

        for x in range(0, 6):
            music_volume += 0.1
            renpy.music.set_volume(music_volume, delay=0, channel='music')
            renpy.pause(0.1)

    $ renpy.pause(1.0, hard='True')

    hide albert_office_telephone
    show telephone_ring

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    $ renpy.music.play("audio/1920PhoneRingTone.ogg", channel="sound", loop=True)

    stop music fadeout 3.0

    $ renpy.pause(4.0, hard='True')

    a "Pardon me."

    $ albert_is_calling = True

    hide telephone_ring
    hide albert_sitting
    show albert_sitting_phone

    python:

        for x in range(0, 6):
            music_volume -= 0.1
            renpy.music.set_volume(music_volume, delay=0, channel='music')

    stop sound
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/phone-picked-up.mp3"

    $ renpy.pause(1.0, hard='True')

    a "Albert Krueger speaking. {w=0.5}How may I help you?"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/xtrgamr__gibberish-chipmunk.wav"

    $ renpy.pause(4.0, hard='True')

    if persistent.num_finish > 0:

        a "Hmm. {w=0.5}Another problem?"
    else:


        a "Hmm. {w=0.5}Is that so?"

    a "Well I’m sure you’re competent enough to come up with a plan, {w=0.5}am I correct?"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/xtrgamr__gibberish.wav"

    $ renpy.pause(3.0, hard='True')

    show taylor_face_panic:
        xpos 190 ypos 600
    hide taylor_face

    if persistent.num_finish > 0:

        $ variation_3 = variation_3_all[random.randint(0, len(variation_3_all)-1)]

        a "[variation_3!t]"
    else:


        a "No William. {w=0.5}We’re not killing it."

    a "I’d prefer that we come up with a better plan before resolving into that."

    a "Now please excuse me, {w=0.5}I’m with a patient at the moment."

    $ renpy.music.set_volume(music_volume, delay=0, channel='music')
    play music "audio/takeADeepBreath_v2.mp3"

    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    play sound "audio/phone-put-down.mp3"

    $ albert_is_calling = False

    $ renpy.pause(0.2, hard='True')

    hide albert_sitting_phone
    show albert_sitting
    show albert_office_telephone

    $ renpy.pause(0.7, hard='True')

    a "Sorry about that."

    t "Umm... {w=0.5}Is everything okay?"

    t "That sounds pretty serious."

    a "Thank you for your concern, {w=0.5}Taylor."

    a "I appreciate it very much."

    a "However, {w=0.5}there’s no need to be worried."

    a "I’ll have you know that our team is extremely well-trained."

    t "Umm, {w=0.5}okay. {w=0.5}That’s good to know."

    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_panic

    $ renpy.pause(0.5, hard='True')

    t "Btw, {w=0.5}your last name is Krueger, {w=0.5}right?"

    a "That is correct."

    t "Just kinda curious... {w=0.5}Does that mean... {w=0.5}You’re the CEO?"

    a "Good catch, {w=0.5}Taylor."

    a "Yes, {w=0.5}I am indeed the CEO of Krueger Corporation."

    a "In fact, {w=0.5}my father was the one who created this company."

    a "All I did was simply take over after his death."

    t "...Is that why you came back from G4? "

    t "To take over your family’s business?"

    a "Yes. {w=0.5}It is part of my destiny."

    if persistent.num_finish > 0:

        t "...Do you miss G4?"

        a_think "......"

        a "Maybe. {w=0.5}Maybe not."

        a "G4 was a nice place."

        if persistent.num_finish > 1:

            a "I would totally visit there again at some point."
    else:


        t "I, {w=0.5}I see."

        t "But damn, {w=0.5}I gotta say, {w=0.5}I’m pretty honored to receive therapy from the CEO himself."

        a "You’re too kind, {w=0.5}Taylor."

        a "I’m just simply doing what I enjoy doing."

        a "And not to mention, {w=0.5}I enjoy talking to you very much."

        t "Umm... {w=0.5}I’m glad."

    a "I say that’s enough time for a short break."

    a "Shall we move on to the next section?"

    t "Eh... {w=0.5}Sure."

    jump gateway_to_heart_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
