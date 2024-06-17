image ctc_blink:
    "gui/ctc.png"
    linear 0.5 alpha 1.0
    pause 0.25
    linear 0.5 alpha 0.0
    pause 0.25
    repeat


image albert_office:
    zoom 5 xalign 0.5 yalign 0.5
    contains:
        "images/albert office.png"
        xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("add_office_layer_1 == True", "images/albert office layer 1.png", "add_office_layer_1 == False", "images/empty.png")
        xalign 0.5 yalign 0.5

image albert_office_glitch_1:
    zoom 5
    "images/albert office glitch 1.png"
image albert_office_glitch_2:
    zoom 5
    "images/albert office glitch 2.png"
image albert_office_glitch_3:
    zoom 5
    "images/albert office glitch 3.png"
image glitch_1:
    zoom 5
    "images/glitch 1.png"
image glitch_2:
    zoom 5
    "images/glitch 2.png"

image albert_office_red:
    zoom 5
    "images/albert office red.png"

image albert_office_red_2:
    zoom 5
    "images/albert office red 2.png"

image albert_office_red_3:
    zoom 5
    "images/albert office red 3.png"


image albert_office_lamp:
    zoom 5
    "images/albert office lamp.png"
image albert_office_telephone:
    zoom 5
    "images/albert office telephone.png"

image telephone_ring:
    zoom 5 xalign 0.5 yalign 0.5
    block:
        "images/telephone ring 1.png"
        0.3
        "images/telephone ring 2.png"
        0.3
        repeat




image albert_sitting:
    zoom 5 xalign 0.5 yalign 0.5
    contains:
        "images/characters/albert_sitting.png"
        xalign 0.5 yalign 0.5
    contains:
        "albert_sitting_eyes"
        xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("albert_is_talking == True and albert_is_sitting == True", "albert_sitting_mouth_talk",
                                   "albert_is_talking == False or albert_is_sitting == False", "albert_sitting_mouth_normal")
        xalign 0.5 yalign 0.5

image albert_sitting_glitchy:

    "albert_sitting"
    1.0
    "albert_sitting_glitch_1"
    0.2
    "albert_sitting"
    0.8
    "albert_sitting_glitch_2"
    0.2
    "albert_sitting"
    1.0
    "albert_sitting_glitch_2"
    0.05
    "albert_sitting"
    0.1
    "albert_sitting_glitch_1"
    0.4
    repeat


image albert_sitting_phone:
    zoom 5 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("albert_is_calling == True", "albert_body_pick_up_phone_animation",
                                   "albert_is_calling == False", "albert_body_put_down_phone_animation")
        xalign 0.5 yalign 0.5
    contains:
        "albert_sitting_eyes"
        xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("albert_is_talking == True and albert_is_sitting == True", "albert_sitting_mouth_talk",
                                   "albert_is_talking == False or albert_is_sitting == False", "albert_sitting_mouth_normal")
        xalign 0.5 yalign 0.5

image albert_body_pick_up_phone_animation:
    xalign 0.5 yalign 0.5
    "images/characters/albert_sitting_pick_up_phone_1.png"
    0.2
    "images/characters/albert_sitting_pick_up_phone_2.png"

image albert_body_put_down_phone_animation:
    xalign 0.5 yalign 0.5
    "images/characters/albert_sitting_pick_up_phone_2.png"
    0.2
    "images/characters/albert_sitting_pick_up_phone_1.png"

image albert_sitting_glitch_1:
    "images/characters/albert_sitting_glitch_1.png"
    zoom 5.0

image albert_sitting_glitch_2:
    "images/characters/albert_sitting_glitch_2.png"
    zoom 5.0

image albert_sitting_glitch_3:
    "images/characters/albert_sitting_glitch_3.png"
    zoom 5.0

image albert_sitting_eyes:
    "images/characters/albert_eye_1.png"
    4.0
    "images/characters/albert_eye_2.png"
    0.3
    "images/characters/albert_eye_3.png"
    0.3
    "images/characters/albert_eye_2.png"
    0.3
    "images/characters/albert_eye_1.png"
    repeat

image albert_sitting_mouth_talk:
    "images/characters/albert_mouth_2.png"
    0.1
    "images/characters/albert_mouth_3.png"
    0.3
    "images/characters/albert_mouth_4.png"
    0.3
    "images/characters/albert_mouth_2.png"
    0.1
    "images/characters/albert_mouth_3.png"
    0.05
    "images/characters/albert_mouth_2.png"
    0.2
    "images/characters/albert_mouth_4.png"
    0.3
    "images/characters/albert_mouth_3.png"
    0.3
    "images/characters/albert_mouth_2.png"
    0.2
    "images/characters/albert_mouth_4.png"
    0.1
    repeat

image albert_sitting_mouth_normal:
    "images/characters/albert_mouth_1.png"

image albert_face_complete:
    "images/characters/albert_face_complete.png"
    zoom 5.0

image albert_face:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/albert_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        "albert_face_eyes"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("albert_is_talking == True", "albert_face_mouth_talk",
                                   "albert_is_talking == False", "albert_face_mouth_normal")
        zoom 5.0 xalign 0.5 yalign 0.5

image albert_face_eyes:
    "images/characters/albert_face_eye_1.png"
    8.0
    "images/characters/albert_face_eye_2.png"
    0.3
    "images/characters/albert_face_eye_3.png"
    0.3
    "images/characters/albert_face_eye_2.png"
    0.3
    "images/characters/albert_face_eye_1.png"
    repeat

image albert_face_mouth_normal:
    "images/characters/albert_face_mouth_1.png"

image albert_face_mouth_talk:
    "images/characters/albert_face_mouth_2.png"
    0.3
    "images/characters/albert_face_mouth_1.png"
    0.1
    "images/characters/albert_face_mouth_2.png"
    0.1
    "images/characters/albert_face_mouth_1.png"
    0.05
    repeat

image albert_giant_face:
    xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5
    contains:
        "images/characters/albert_giant_face_eye_2.png"
        zoom 5.0 xpos 500 ypos 250 xanchor 0.5 yanchor 0.5
        rotate 0
        linear 0.2 rotate 360
        repeat
    contains:
        "images/characters/albert_giant_face_eye_1.png"
        zoom 5.0 xpos 763 ypos 300 xanchor 0.5 yanchor 0.5
        rotate 0
        linear 0.2 rotate 360
        repeat
    contains:
        "images/characters/albert_giant_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    block:
        zoom 1.0
        ease 1.5 zoom 5.0

image albert_face_outline:
    zoom 5.0
    "images/characters/krueger_face_outline.png"



image taylor_face:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/taylor_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        "taylor_face_eyes"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("taylor_is_talking == True", "taylor_face_mouth_talk",
                                   "taylor_is_talking == False", "taylor_face_mouth_normal")
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_face_close_eye:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/taylor_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        "taylor_face_close_eyes_animation"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("taylor_is_talking == True", "taylor_face_mouth_talk",
                                   "taylor_is_talking == False", "taylor_face_mouth_normal")
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_face_open_eye:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/taylor_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        "taylor_face_open_eyes_animation"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("taylor_is_talking == True", "taylor_face_mouth_talk",
                                   "taylor_is_talking == False", "taylor_face_mouth_normal")
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_face_panic:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/taylor_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        "taylor_face_eyes_panic"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("taylor_is_talking == True", "taylor_face_mouth_talk",
                                   "taylor_is_talking == False", "taylor_face_mouth_normal")
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_face_awkward:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/taylor_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        "taylor_face_eyes_awkward"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("taylor_is_talking == True", "taylor_face_mouth_talk",
                                   "taylor_is_talking == False", "taylor_face_mouth_normal")
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_face_distracted:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/taylor_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        "images/characters/taylor_eye_awkward.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("taylor_is_talking == True", "taylor_face_mouth_talk",
                                   "taylor_is_talking == False", "taylor_face_mouth_normal")
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_face_speechless:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/taylor_face.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        "images/characters/taylor_eye_2.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        ConditionSwitch("taylor_is_talking == True", "taylor_face_mouth_talk",
                                   "taylor_is_talking == False", "taylor_face_mouth_normal")
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_face_bleed:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/characters/taylor face bleeding/taylor bleed 1.png"
        zoom 5.0 xalign 0.5 yalign 0.5
        0.5
        "images/characters/taylor face bleeding/taylor bleed 2.png"
        zoom 5.0 xalign 0.5 yalign 0.5
        0.5
        "images/characters/taylor face bleeding/taylor bleed 3.png"
        zoom 5.0 xalign 0.5 yalign 0.5
        0.5
        "images/characters/taylor face bleeding/taylor bleed 4.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_face_eyes:
    "images/characters/taylor_eye_1.png"
    8.0
    "images/characters/taylor_eye_2.png"
    0.3
    "images/characters/taylor_eye_3.png"
    0.3
    "images/characters/taylor_eye_4.png"
    0.3
    "images/characters/taylor_eye_2.png"
    0.3
    "images/characters/taylor_eye_1.png"
    repeat

image taylor_face_close_eyes_animation:
    "images/characters/taylor_eye_2.png"
    0.2
    "images/characters/taylor_eye_3.png"
    0.2
    "images/characters/taylor_eye_4.png"

image taylor_face_open_eyes_animation:
    "images/characters/taylor_eye_3.png"
    0.2
    "images/characters/taylor_eye_2.png"
    0.2
    "images/characters/taylor_eye_1.png"

image taylor_face_eyes_panic:
    "images/characters/taylor_eye_panic.png"

image taylor_face_eyes_awkward:
    "images/characters/taylor_eye_awkward.png"
    0.3
    "images/characters/taylor_eye_1.png"
    3.0
    "images/characters/taylor_eye_awkward.png"
    1.0
    "images/characters/taylor_eye_1.png"
    5.0
    repeat

image taylor_face_mouth_normal:
    "images/characters/taylor_mouth_1.png"

image taylor_face_mouth_talk:
    "images/characters/taylor_mouth_2.png"
    0.3
    "images/characters/taylor_mouth_1.png"
    0.1
    "images/characters/taylor_mouth_2.png"
    0.1
    "images/characters/taylor_mouth_1.png"
    0.05
    repeat

image taylor_face_outline:
    zoom 5.0 xanchor 0.5 yanchor 0.5
    "images/characters/taylor_face_outline.png"

image dead_taylor_eyes_animation:
    "images/characters/dead_taylor_eyes/dead taylor eyes 1.png"
    8.0
    "images/characters/dead_taylor_eyes/dead taylor eyes 2.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 3.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 4.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 5.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 4.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 3.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 2.png"
    0.3
    repeat

image dead_taylor_open_eyes_animation:
    "images/characters/dead_taylor_eyes/dead taylor eyes 5.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 4.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 3.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 2.png"
    0.3
    "images/characters/dead_taylor_eyes/dead taylor eyes 1.png"

image dead_taylor:
    xalign 0.5 yalign 0.5
    contains:
        "images/characters/dead_taylor_body.png"
        zoom 5.0
    contains:
        "dead_taylor_eyes_animation"
        ConditionSwitch("dead_taylor_eyes == 0", "images/characters/dead_taylor_eyes/dead taylor eyes look down.png",
                                   "dead_taylor_eyes == 1", "dead_taylor_eyes_animation", "dead_taylor_eyes == 2", "dead_taylor_open_eyes_animation")
        zoom 5.0

image dream_taylor:
    xalign 0.5 yalign 0.5
    contains:
        zoom 5.0
        "images/characters/taylor_dream_eater.png"



image card:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/card.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image card_hover_zoom:
    contains:
        "images/card_hover.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image card_idle_zoom:
    contains:
        "images/card_idle.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image bloody_card:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/bloody_card.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image cup:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/cup.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image cup_hover_zoom:
    contains:
        "images/cup_hover.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image cup_idle_zoom:
    contains:
        "images/cup_idle.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image eyeball:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/eyeball.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image paper:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/rorschach/rorschach paper.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image rorschach_image:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/rorschach/rorschach " + str(rorschach_num) + ".png"
        zoom 5.0 xalign 0.5 yalign 0.5

image horror_rorschach_image:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/rorschach/horror rorschach " + str(horror_rorschach_num) + ".png"
        zoom 5.0 xalign 0.5 yalign 0.5

image rorschach_paper_hover_zoom:
    contains:
        "images/rorschach/rorschach paper hover.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image rorschach_paper_idle_zoom:
    contains:
        "images/rorschach/rorschach paper idle.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image vincent:
    xanchor 0.5 yanchor 0.5
    contains:
        "images/rorschach/vincent.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image survey_paper:
    xalign 0.5 yalign 0.5
    contains:
        "images/survey paper.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image smiley_face:
    xalign 0.5 yalign 0.5
    contains:
        "images/smiley face.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image sad_face:
    xalign 0.5 yalign 0.5
    contains:
        "images/sad face.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image smiley_face_focus_mask:
    xalign 0.5 yalign 0.5
    contains:
        "images/smiley face focus mask.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image smiley_face_empty:
    xalign 0.5 yalign 0.5
    contains:
        "images/smiley face empty.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image smiley_face_hover:
    xalign 0.5 yalign 0.5
    contains:
        "images/smiley face hover.png"
        zoom 5.0 xalign 0.5 yalign 0.5

image taylor_medical_card:
    zoom 5.0 xalign 0.5 yalign 0.5
    "images/taylor medical card.png"

image medical_card_speech_bubble:
    xalign 0.5 yalign 0.5
    contains:
        "images/speech bubble animation/speech bubble.png"
        zoom 5.0 xalign 0.5 yalign 0.5
    contains:
        zoom 5.0 xalign 0.5 yalign 0.5
        0.3
        "images/speech bubble animation/speech bubble dot 1.png"
        0.3
        "images/speech bubble animation/speech bubble dot 2.png"
        0.3
        "images/speech bubble animation/speech bubble dot 3.png"


image close_eye_animation:
    zoom 5.0
    "images/close eyes animation/close eye 1.png"
    0.1
    "images/close eyes animation/close eye 2.png"
    0.1
    "images/close eyes animation/close eye 3.png"
    0.1
    "images/close eyes animation/close eye 4.png"
    0.1
    "images/close eyes animation/close eye 5.png"
    0.1
    "images/close eyes animation/close eye 6.png"
    0.1
    "black"

image open_eye_animation:
    zoom 5.0
    "images/close eyes animation/close eye 6.png"
    0.1
    "images/close eyes animation/close eye 5.png"
    0.1
    "images/close eyes animation/close eye 4.png"
    0.1
    "images/close eyes animation/close eye 3.png"
    0.1
    "images/close eyes animation/close eye 2.png"
    0.1
    "images/close eyes animation/close eye 1.png"
    0.1
    "images/empty.png"

image desktop:
    zoom 5.0
    "images/desktop.png"


image creepy_face_1:
    zoom 5.0 xanchor 0.5 yanchor 0.5 xalign 0.5 yalign 0.5
    "images/creepy_face_1.png"


image cat_mouse_animation:
    "images/cat mouse animation/frame_00_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_01_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_02_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_03_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_04_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_05_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_06_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_07_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_08_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_09_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_10_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_11_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_12_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_13_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_14_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_15_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_16_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_17_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_18_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_19_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_20_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_21_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_22_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_23_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_24_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_25_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_26_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_27_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_28_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_29_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_30_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_31_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_32_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_33_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_34_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_35_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_36_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_37_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_38_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_39_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_40_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_41_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_42_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_43_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_44_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_45_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_46_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_47_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_48_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_49_delay-0.03s.gif"
    0.02
    "images/cat mouse animation/frame_50_delay-0.03s.gif"
    0.02
    repeat


image bad_tv:
    contains:
        alpha 0.3
        "images/bad tv/tv-static-1.png"
        0.1
        "images/bad tv/tv-static-2.png"
        0.1
        "images/bad tv/tv-static-3.png"
        0.
        "images/bad tv/tv-static-4.png"
        repeat
    contains:
        "images/bad tv/bad_signal_layer_1.png"
    contains:
        "images/bad tv/bad_signal_layer_2.png"
        yoffset -1000 alpha 1.0
        linear 9.0 yoffset 0 alpha 1.0
        repeat
    contains:
        "black"
        alpha 0
        pause 3.0
        alpha 0.15
        pause 0.2
        alpha 0.3
        pause 0.05
        alpha 0.3
        pause 0.5
        alpha 0.15
        pause 0.35
        alpha 0.1
        pause 0.05
        alpha 0.2
        pause 1.0
        repeat
    contains:
        "images/bad tv/bad_signal_layer_3.png"
        alpha 0.3


image tite_drop_shadow = "images/main title/title_drop_shadow.png"
image title:
    "images/main title/title.png"
    zoom 1.0 xalign 0.5 yalign 0.5
    block:
        ease 1.5 zoom 1.05 xalign 0.5 yalign 0.5
        ease 1.5 zoom 1.0 xalign 0.5 yalign 0.5
        repeat
image main_title_background:
    "gui/main_menu.png"
image main_title_background_2:
    "gui/main_menu_2.png"

image main_title_bad_tv:
    "bad_tv"
    alpha 0
    block:
        5.0
        ease 2.0 alpha 0.2
        5.0
        ease 2.0 alpha 0
        repeat

image main_title_play_button:
    "gui/play_button_idle.png"
    zoom 1

image main_title_load_button:
    "gui/load_button_idle.png"
    zoom 1

image main_title_pref_button:
    "gui/pref_button_idle.png"
    zoom 1

image main_title_about_button:
    "gui/about_button_idle.png"
    zoom 1

image desktop_main_menu:
    "images/desktop_main_menu.png"
    zoom 5.0


image quick_menu_idle:
    "gui/quick menu button idle.png"
    zoom 2.5


image dust = Fixed(SnowBlossom(At("images/particles/dust-1.png", withAdd), count=2, border=50, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=False), SnowBlossom(At("images/particles/dust-2.png", withAdd), count=2, border=50, xspeed=(-20, 20), yspeed=(20, 50), start=0, fast=False, horizontal=False))

transform withAdd:
    additive 1.0

image lighting:
    "images/lighting-pixelated.png"
    alpha 0.3
    block:
        linear 1.0 alpha 0
        pause 5.0
        alpha 0.2
        linear 0.5 alpha 0.5
        repeat

image blood_drip:
    zoom 5.0
    "images/blood dripping/blood drip 1.png"
    0.2
    "images/blood dripping/blood drip 2.png"
    0.2
    "images/blood dripping/blood drip 3.png"
    0.2
    "images/blood dripping/blood drip 4.png"
    0.2
    "images/blood dripping/blood drip 5.png"
    0.2
    "images/blood dripping/blood drip 6.png"
    0.2
    "images/blood dripping/blood drip 7.png"
    0.2
    "images/blood dripping/blood drip 8.png"
    0.2
    "images/blood dripping/blood drip 9.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
