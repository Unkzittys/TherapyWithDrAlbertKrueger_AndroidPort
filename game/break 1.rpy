
label break_1_start:

    $ auto_enabled_ = True

    a "You must have used a lot of brain cells for those Math questions."

    a "Why don’t we take a little short break?"

    t "Ummm... {w=0.5}Sure."

    a "Let me turn up the music."

    window hide

    python:

        for x in range(0, 6):
            music_volume += 0.1
            renpy.music.set_volume(music_volume, delay=0, channel='music')
            renpy.pause(0.1)

    $ renpy.pause(2.0, hard='True')

    window auto

    a "Much better."

    window hide

    $ renpy.pause(3.0, hard='True')

    show taylor_face_awkward:
        xpos 190 ypos 600
    hide taylor_face

    $ renpy.pause(1.0, hard='True')

    window auto

    t_think "......"

    window hide

    $ renpy.pause(2.0, hard='True')

    show taylor_face_distracted:
        xpos 190 ypos 600
    hide taylor_face_awkward

    window auto

    a "So how’s it going?"

    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_distracted

    t "Huh?"

    a "How are you feeling? {w=0.5}Everything alright?"

    t "Eh... {w=0.5}I’m a bit confused. {w=0.5}But otherwise all good."

    a "How’s school?"

    t "...Pretty much the same."

    a "You a college student?"

    t "Ya."

    a "Sweet! {w=0.5}Are you from G2?"

    t "Yeah. {w=0.5}Been living here my whole life."

    if persistent.num_finish > 0:

        t "You’re from G2 as well, {w=0.5}right?"

        t "I could kinda tell."

        a "Yes indeed I am."
    else:


        t "What about you? {w=0.5}You from around here as well?"

        a "Yes. {w=0.5}I was born in G2."

    a "However, {w=0.5}I did not attend college here."

    a "I went to G4 for my post-secondary education."

    t "Oh! {w=0.5}RMU?"

    a "Yes."

    t "That’s a pretty dope school."

    a "Thank you."

    if persistent.num_finish > 0:

        t_think "(...How did I know he was from G2?)"

    window hide

    $ renpy.pause(3.0, hard='True')

    show taylor_face_awkward:
        xpos 190 ypos 600
    hide taylor_face

    $ renpy.pause(1.0, hard='True')

    window auto

    t_think "......"

    window hide

    $ renpy.pause(2.0, hard='True')

    show taylor_face_distracted:
        xpos 190 ypos 600
    hide taylor_face_awkward

    window auto

    python:

        for x in range(0, 6):
            music_volume -= 0.1
            renpy.music.set_volume(music_volume, delay=0, channel='music')
            renpy.pause(0.3)

    show taylor_face:
        xpos 190 ypos 600
    hide taylor_face_distracted

    a "Alright, {w=0.5}break’s over."

    a "Let’s move on to the next section of our therapy, {w=0.5}shall we?"

    t "Umm okay."

    jump cups_and_balls_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
