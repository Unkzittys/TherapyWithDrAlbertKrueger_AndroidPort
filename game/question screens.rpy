
init 1 python:
    class checkAnswer(Action):
        
        def __init__(self, index, correct_index, end_label):
            self.index = index
            self.correct_index = correct_index
            self.end_label = end_label
        
        def __call__(self):
            renpy.hide_screen("empty_screen")
            renpy.hide_screen("math_problem")
            renpy.hide_screen("cups_and_balls_problem")
            if self.end_label == "end_of_cups_and_balls_question":
                global chose_cup_answer
                chose_cup_answer = self.index
            if self.index == self.correct_index:
                global feedback
                feedback = compliments[random.randint(0,len(compliments)-1)]
                if self.end_label == "end_of_math_problem":
                    global math_answered_correct
                    math_answered_correct += 1
                elif self.end_label == "end_of_cups_and_balls_question":
                    global cup_answered_correct
                    cup_answered_correct += 1
                renpy.jump(self.end_label)
            else:
                global feedback
                feedback = non_compliments[random.randint(0,len(non_compliments)-1)]
                renpy.jump(self.end_label)

    class pickRandomFeedback(Action):
        
        def __init__(self, list_, end_label):
            self.list_ = list_
            self.end_label = end_label
        
        def __call__(self):
            renpy.hide_screen("empty_screen")
            renpy.hide_screen("rorschach_problem")
            global feedback
            feedback = self.list_[random.randint(0,len(self.list_)-1)]
            renpy.jump(self.end_label)


screen math_countdown(timer_range):
    default end_time = time.time() + timer_range
    default current_time = time.time()
    timer 0.05 repeat True action If(
        current_time < end_time,
        true=SetScreenVariable('current_time', time.time()),
        false=[Hide('math_countdown'), Show('math_problem')]
    )

screen empty_screen:

    key "K_SPACE" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "mouseup_1" action NullAction()

    imagebutton:
        idle "images/empty.png"
        hover "images/empty.png"
        action NullAction()

screen math_problem:

    imagebutton:
        idle "images/empty.png"
        hover "images/empty.png"
        action NullAction()

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos 285
        ypos 250
        idle "card_idle_zoom"
        hover "card_hover_zoom"
        focus_mask "card_hover_zoom"
        action checkAnswer(1, correct_answer_num, "end_of_math_problem")

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos 525
        ypos 250
        idle "card_idle_zoom"
        hover "card_hover_zoom"
        focus_mask "card_hover_zoom"
        action checkAnswer(2, correct_answer_num, "end_of_math_problem")

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos 765
        ypos 250
        idle "card_idle_zoom"
        hover "card_hover_zoom"
        focus_mask "card_hover_zoom"
        action checkAnswer(3, correct_answer_num, "end_of_math_problem")

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos 1005
        ypos 250
        idle "card_idle_zoom"
        hover "card_hover_zoom"
        focus_mask "card_hover_zoom"
        action checkAnswer(4, correct_answer_num, "end_of_math_problem")

screen cups_and_balls_problem:

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos cup_positions[0]
        ypos 250
        idle "cup_idle_zoom"
        hover "cup_hover_zoom"
        focus_mask "cup_hover_zoom"
        action checkAnswer(0, has_ball_index, "end_of_cups_and_balls_question")

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos cup_positions[1]
        ypos 250
        idle "cup_idle_zoom"
        hover "cup_hover_zoom"
        focus_mask "cup_hover_zoom"
        action checkAnswer(1, has_ball_index, "end_of_cups_and_balls_question")

    imagebutton:
        xanchor 0.5 yanchor 0.5
        xpos cup_positions[2]
        ypos 250
        idle "cup_idle_zoom"
        hover "cup_hover_zoom"
        focus_mask "cup_hover_zoom"
        action checkAnswer(2, has_ball_index, "end_of_cups_and_balls_question")

image shaky_word_1:
    Text(selected_word_list[0])
    yoffset -5.0 xoffset 5.0
    pause .2
    yoffset 5.0 xoffset -5.0
    pause .2
    yoffset 5.0 xoffset 5.0
    pause .2
    yoffset -5.0 xoffset -5.0
    pause .2
    repeat

image shaky_word_2:
    Text(selected_word_list[1])
    yoffset 5.0 xoffset 5.0
    pause .2
    yoffset 5.0 xoffset -5.0
    pause .2
    yoffset -5.0 xoffset 5.0
    pause .2
    yoffset -5.0 xoffset -5.0
    pause .2
    repeat

image shaky_word_3:
    Text(selected_word_list[2])
    yoffset 5.0 xoffset -5.0
    pause .2
    yoffset 5.0 xoffset 5.0
    pause .2
    yoffset -5.0 xoffset 5.0
    pause .2
    yoffset -5.0 xoffset -5.0
    pause .2
    repeat

image shaky_word_4:
    Text(selected_word_list[3])
    yoffset 5.0 xoffset -5.0
    pause .2
    yoffset -5.0 xoffset -5.0
    pause .2
    yoffset -5.0 xoffset 5.0
    pause .2
    yoffset 5.0 xoffset 5.0
    pause .2
    repeat

image shaky_word_5:
    Text(selected_word_list[4])
    yoffset 5.0 xoffset -5.0
    pause .2
    yoffset -5.0 xoffset -5.0
    pause .2
    yoffset -5.0 xoffset 5.0
    pause .2
    yoffset 5.0 xoffset 5.0
    pause .2
    repeat

image shaky_word_6:
    Text(selected_word_list[5])
    yoffset -5.0 xoffset 5.0
    pause .2
    yoffset -5.0 xoffset -5.0
    pause .2
    yoffset 5.0 xoffset -5.0
    pause .2
    yoffset 5.0 xoffset 5.0
    pause .2
    repeat

screen rorschach_problem:

    zorder 3

    imagebutton:
        xpos 0
        ypos -110
        idle "rorschach_paper_idle_zoom"
        hover "rorschach_paper_hover_zoom"
        focus_mask "rorschach_paper_hover_zoom"
        action Jump("flip_rorschach")

    imagebutton:
        xpos 440
        ypos 573
        idle "shaky_word_1"
        hover Text(selected_actual_word_list[0], size=70, color=word_color) xoffset 0 yoffset 0 xalign 0.5 yalign 0.5
        action pickRandomFeedback(rorschach_feedback, "rorschach_round_end")

    imagebutton:
        xpos 440
        ypos 631
        idle "shaky_word_2"
        hover Text(selected_actual_word_list[1], size=70, color=word_color) xoffset 0 yoffset 0 xalign 0.5 yalign 0.5
        action pickRandomFeedback(rorschach_feedback, "rorschach_round_end")

    imagebutton:
        xpos 640
        ypos 573
        idle "shaky_word_3"
        hover Text(selected_actual_word_list[2], size=70, color=word_color) xoffset 0 yoffset 0 xalign 0.5 yalign 0.5
        action pickRandomFeedback(rorschach_feedback, "rorschach_round_end")

    imagebutton:
        xpos 640
        ypos 631
        idle "shaky_word_4"
        hover Text(selected_actual_word_list[3], size=70, color=word_color) xoffset 0 yoffset 0 xalign 0.5 yalign 0.5
        action pickRandomFeedback(rorschach_feedback, "rorschach_round_end")

    imagebutton:
        xpos 840
        ypos 573
        idle "shaky_word_5"
        hover Text(selected_actual_word_list[4], size=70, color=word_color) xoffset 0 yoffset 0 xalign 0.5 yalign 0.5
        action pickRandomFeedback(rorschach_feedback, "rorschach_round_end")

    imagebutton:
        xpos 840
        ypos 631
        idle "shaky_word_6"
        hover Text(selected_actual_word_list[5], size=70, color=word_color) xoffset 0 yoffset 0 xalign 0.5 yalign 0.5
        action pickRandomFeedback(rorschach_feedback, "rorschach_round_end")




screen yes_no_countdown(timer_range):
    default end_time = time.time() + timer_range
    default current_time = time.time()
    timer 0.05 repeat True action If(
        current_time < end_time,
        true=SetScreenVariable('current_time', time.time()),
        false=[Hide('yes_no_countdown'), Show('open_eyes_decision_screen')]
    )

image shaky_yes:
    Text(_("YES"))
    zoom 5
    yoffset -5.0 xoffset 5.0
    pause .2
    yoffset 5.0 xoffset -5.0
    pause .2
    yoffset 5.0 xoffset 5.0
    pause .2
    yoffset -5.0 xoffset -5.0
    pause .2
    repeat

image shaky_yes_red:
    Text(_("YES"), color="#FF0000")
    zoom 5

image shaky_no:
    Text(_("NO"))
    zoom 5
    yoffset 5.0 xoffset 5.0
    pause .2
    yoffset -5.0 xoffset 5.0
    pause .2
    yoffset 5.0 xoffset -5.0
    pause .2
    yoffset -5.0 xoffset -5.0
    pause .2
    repeat

image shaky_no_red:
    Text(_("NO"), color="#FF0000")
    zoom 5

screen open_eyes_decision_screen:

    imagebutton:
        xpos gateway_yes_xpos
        ypos 200
        xalign 0.5
        idle "shaky_yes"
        hover "shaky_yes_red"
        action Jump("Open_eyes")

    imagebutton:
        xpos gateway_no_xpos
        ypos 200
        xalign 0.5
        idle "shaky_no"
        hover "shaky_no_red"
        action Jump(next_label)

screen survey_screen:

    if not answered_survey[0]:

        imagebutton:
            xpos -80
            ypos -180
            idle "smiley_face_empty"
            hover "smiley_face_hover"
            focus_mask "smiley_face_focus_mask"
            action Jump("show_smiley_face_1_circle")

        imagebutton:
            xpos 70
            ypos -180
            idle "smiley_face_empty"
            hover "smiley_face_hover"
            focus_mask "smiley_face_focus_mask"
            action Jump("show_smiley_face_1_circle")

    if not answered_survey[1]:

        imagebutton:
            xpos -80
            ypos 45
            idle "smiley_face_empty"
            hover "smiley_face_hover"
            focus_mask "smiley_face_focus_mask"
            action Jump("show_smiley_face_2_circle")

        imagebutton:
            xpos 70
            ypos 45
            idle "smiley_face_empty"
            hover "smiley_face_hover"
            focus_mask "smiley_face_focus_mask"
            action Jump("show_smiley_face_2_circle")

    if not answered_survey[2]:

        imagebutton:
            xpos -80
            ypos 270
            idle "smiley_face_empty"
            hover "smiley_face_hover"
            focus_mask "smiley_face_focus_mask"
            action Jump("show_smiley_face_3_circle")

        imagebutton:
            xpos 70
            ypos 270
            idle "smiley_face_empty"
            hover "smiley_face_hover"
            focus_mask "smiley_face_focus_mask"
            action Jump("show_smiley_face_3_circle")

label show_smiley_face_1_circle:

    $ answered_survey[0] = True

    show smiley_face_hover as smiley_face_hover_1:
        xpos 705 ypos 180
    with Dissolve(0.3)

    python:

        for x in range(0, len(answered_survey)):
            if answered_survey[x] == False:
                renpy.call_screen("survey_screen")

        renpy.jump("finish_survey")

label show_smiley_face_2_circle:

    $ answered_survey[1] = True

    show smiley_face_hover as smiley_face_hover_2:
        xpos 705 ypos 405
    with Dissolve(0.3)

    python:

        for x in range(0, len(answered_survey)):
            if answered_survey[x] == False:
                renpy.call_screen("survey_screen")

        renpy.jump("finish_survey")

label show_smiley_face_3_circle:

    $ answered_survey[2] = True

    show smiley_face_hover as smiley_face_hover_3:
        xpos 705 ypos 630
    with Dissolve(0.3)

    python:

        for x in range(0, len(answered_survey)):
            if answered_survey[x] == False:
                renpy.call_screen("survey_screen")

        renpy.jump("finish_survey")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
