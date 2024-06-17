init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995


            textbutton _("LOG") action ShowMenu('history')
            if not persistent.try_skipping:
                textbutton _("SKIP") action Show('skip_confirm')

            if auto_enabled_:
                textbutton _("AUTO") action Preference("auto-forward", "toggle")
            else:
                textbutton _("AUTO") action NullAction()
            if quick_load_:
                textbutton _("LOAD") action FileLoad(1, page=1) selected False




            textbutton _("PREFS") action ShowMenu('preferences')




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")












screen navigation():


    on "show" action Function(clack_play_albert)

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            if persistent.most_recent_ending == 2:
                imagebutton:
                    if persistent.lang == "korean":
                        idle "tl/korean/korean-reset-idle.png"
                        hover "tl/korean/korean-reset-hover.png"
                    elif persistent.lang == "spanish":
                        idle "tl/spanish/spanish-reset-idle.png"
                        hover "tl/spanish/spanish-reset-hover.png"
                    elif persistent.lang == "chinese":
                        idle "tl/chinese/chinese-reset-idle.png"
                        hover "tl/chinese/chinese-reset-hover.png"
                    elif persistent.lang == "russian":
                        idle "tl/russian/russian-reset-idle.png"
                        hover "tl/russian/russian-reset-hover.png"
                    elif persistent.lang == "turkish":
                        idle "tl/turkish/turkish-reset-idle.png"
                        hover "tl/turkish/turkish-reset-hover.png"
                    elif persistent.lang == "french":
                        idle "tl/french/french-reset-idle.png"
                        hover "tl/french/french-reset-hover.png"
                    elif persistent.lang == "italian":
                        idle "tl/italian/italian-reset-idle.png"
                        hover "tl/italian/italian-reset-hover.png"
                    else:
                        idle "gui/reset_button_idle.png"
                        hover "gui/reset_button_hover.png"
                    action Show('reset_screen')
            else:

                imagebutton:
                    if persistent.lang == "korean":
                        idle "tl/korean/korean-play-idle.png"
                        hover "tl/korean/korean-play-hover.png"
                    elif persistent.lang == "spanish":
                        idle "tl/spanish/spanish-play-idle.png"
                        hover "tl/spanish/spanish-play-hover.png"
                    elif persistent.lang == "chinese":
                        idle "tl/chinese/chinese-play-idle.png"
                        hover "tl/chinese/chinese-play-hover.png"
                    elif persistent.lang == "russian":
                        idle "tl/russian/russian-play-idle.png"
                        hover "tl/russian/russian-play-hover.png"
                    elif persistent.lang == "turkish":
                        idle "tl/turkish/turkish-play-idle.png"
                        hover "tl/turkish/turkish-play-hover.png"
                    elif persistent.lang == "french":
                        idle "tl/french/french-play-idle.png"
                        hover "tl/french/french-play-hover.png"
                    elif persistent.lang == "italian":
                        idle "tl/italian/italian-play-idle.png"
                        hover "tl/italian/italian-play-hover.png"
                    else:
                        idle "main_title_play_button"
                        hover "gui/play_button_hover.png"
                    action Start()


        else:


            imagebutton:
                if persistent.lang == "korean":
                    idle "tl/korean/korean-log-idle.png"
                    hover "tl/korean/korean-log-hover.png"
                elif persistent.lang == "spanish":
                    idle "tl/spanish/spanish-log-idle.png"
                    hover "tl/spanish/spanish-log-hover.png"
                elif persistent.lang == "chinese":
                    idle "tl/chinese/chinese-log-idle.png"
                    hover "tl/chinese/chinese-log-hover.png"
                elif persistent.lang == "russian":
                    idle "tl/russian/russian-log-idle.png"
                    hover "tl/russian/russian-log-hover.png"
                elif persistent.lang == "turkish":
                    idle "tl/turkish/turkish-log-idle.png"
                    hover "tl/turkish/turkish-log-hover.png"
                elif persistent.lang == "french":
                    idle "tl/french/french-log-idle.png"
                    hover "tl/french/french-log-hover.png"
                else:
                    idle "gui/log_button_idle.png"
                    hover "gui/log_button_hover.png"
                action ShowMenu("history")







            imagebutton:
                if persistent.lang == "korean":
                    idle "tl/korean/korean-pref-idle.png"
                    hover "tl/korean/korean-pref-hover.png"
                elif persistent.lang == "spanish":
                    idle "tl/spanish/spanish-pref-idle.png"
                    hover "tl/spanish/spanish-pref-hover.png"
                elif persistent.lang == "chinese":
                    idle "tl/chinese/chinese-pref-idle.png"
                    hover "tl/chinese/chinese-pref-hover.png"
                elif persistent.lang == "russian":
                    idle "tl/russian/russian-pref-idle.png"
                    hover "tl/russian/russian-pref-hover.png"
                elif persistent.lang == "turkish":
                    idle "tl/turkish/turkish-pref-idle.png"
                    hover "tl/turkish/turkish-pref-hover.png"
                elif persistent.lang == "french":
                    idle "tl/french/french-pref-idle.png"
                    hover "tl/french/french-pref-hover.png"
                else:
                    idle "gui/pref_button_idle.png"
                    hover "gui/pref_button_hover.png"
                action ShowMenu("preferences")










        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:


            imagebutton:
                if persistent.lang == "korean":
                    idle "tl/korean/korean-home-idle.png"
                    hover "tl/korean/korean-home-hover.png"
                elif persistent.lang == "spanish":
                    idle "tl/spanish/spanish-home-idle.png"
                    hover "tl/spanish/spanish-home-hover.png"
                elif persistent.lang == "chinese":
                    idle "tl/chinese/chinese-home-idle.png"
                    hover "tl/chinese/chinese-home-hover.png"
                elif persistent.lang == "russian":
                    idle "tl/russian/russian-home-idle.png"
                    hover "tl/russian/russian-home-hover.png"
                elif persistent.lang == "turkish":
                    idle "tl/turkish/turkish-home-idle.png"
                    hover "tl/turkish/turkish-home-hover.png"
                elif persistent.lang == "french":
                    idle "tl/french/french-home-idle.png"
                    hover "tl/french/french-home-hover.png"
                else:
                    idle "gui/home_button_idle.png"
                    hover "gui/home_button_hover.png"
                action MainMenu()


        imagebutton:
            if persistent.lang == "korean":
                idle "tl/korean/korean-about-idle.png"
                hover "tl/korean/korean-about-hover.png"
            elif persistent.lang == "spanish":
                idle "tl/spanish/spanish-about-idle.png"
                hover "tl/spanish/spanish-about-hover.png"
            elif persistent.lang == "chinese":
                idle "tl/chinese/chinese-about-idle.png"
                hover "tl/chinese/chinese-about-hover.png"
            elif persistent.lang == "russian":
                idle "tl/russian/russian-about-idle.png"
                hover "tl/russian/russian-about-hover.png"
            elif persistent.lang == "turkish":
                idle "tl/turkish/turkish-about-idle.png"
                hover "tl/turkish/turkish-about-hover.png"
            elif persistent.lang == "french":
                idle "tl/french/french-about-idle.png"
                hover "tl/french/french-about-hover.png"
            elif persistent.lang == "portuguese":
                idle "tl/portuguese/portuguese-about-idle.png"
                hover "tl/portuguese/portuguese-about-hover.png"
            else:
                idle "main_title_about_button"
                hover "gui/about_button_hover.png"
            action ShowMenu("about")






        if renpy.variant("pc"):




            imagebutton:
                if persistent.lang == "korean":
                    idle "tl/korean/korean-quit-idle.png"
                    hover "tl/korean/korean-quit-hover.png"
                elif persistent.lang == "spanish":
                    idle "tl/spanish/spanish-quit-idle.png"
                    hover "tl/spanish/spanish-quit-hover.png"
                elif persistent.lang == "chinese":
                    idle "tl/chinese/chinese-quit-idle.png"
                    hover "tl/chinese/chinese-quit-hover.png"
                elif persistent.lang == "russian":
                    idle "tl/russian/russian-quit-idle.png"
                    hover "tl/russian/russian-quit-hover.png"
                elif persistent.lang == "turkish":
                    idle "tl/turkish/turkish-quit-idle.png"
                    hover "tl/turkish/turkish-quit-hover.png"
                elif persistent.lang == "french":
                    idle "tl/french/french-quit-idle.png"
                    hover "tl/french/french-quit-hover.png"
                elif persistent.lang == "portuguese":
                    idle "tl/portuguese/portuguese-quit-idle.png"
                    hover "tl/portuguese/portuguese-quit-hover.png"
                elif persistent.lang == "italian":
                    idle "tl/italian/italian-quit-idle.png"
                    hover "tl/italian/italian-quit-hover.png"
                else:
                    idle "gui/quit_button_idle.png"
                    hover "gui/quit_button_hover.png"
                action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








screen main_menu():




    style_prefix "main_menu" tag menu


    if persistent.most_recent_ending == 2:
        add "desktop_main_menu"
        add Text(_("Dear Taylor,\nHow are you doing?\nI called my arch-enemy today;\nhe seems to be doing fine.\nWould you like to meet up sometime?\nI have a cool therapy idea to show you.\n\nAll the best,\nDr. Krueger")) xpos 460 ypos 228 zoom 0.8
    elif persistent.unlock_true_end:
        add "main_title_background_2"
    else:
        add "main_title_background"

    if persistent.most_recent_ending == 2:
        imagebutton:
            if persistent.lang == "korean":
                idle "tl/korean/korean-reset-idle.png"
                hover "tl/korean/korean-reset-hover.png"
            elif persistent.lang == "spanish":
                idle "tl/spanish/spanish-reset-idle.png"
                hover "tl/spanish/spanish-reset-hover.png"
            elif persistent.lang == "chinese":
                idle "tl/chinese/chinese-reset-idle.png"
                hover "tl/chinese/chinese-reset-hover.png"
            elif persistent.lang == "russian":
                idle "tl/russian/russian-reset-idle.png"
                hover "tl/russian/russian-reset-hover.png"
            elif persistent.lang == "turkish":
                idle "tl/turkish/turkish-reset-idle.png"
                hover "tl/turkish/turkish-reset-hover.png"
            elif persistent.lang == "french":
                idle "tl/french/french-reset-idle.png"
                hover "tl/french/french-reset-hover.png"
            elif persistent.lang == "italian":
                idle "tl/italian/italian-reset-idle.png"
                hover "tl/italian/italian-reset-hover.png"
            else:
                idle "gui/reset_button_idle.png"
                hover "gui/reset_button_hover.png"
            xpos 40
            ypos 640
            action Show('reset_screen')
    else:
        imagebutton:
            if persistent.lang == "korean":
                idle "tl/korean/korean-play-idle.png"
                hover "tl/korean/korean-play-hover.png"
            elif persistent.lang == "spanish":
                idle "tl/spanish/spanish-play-idle.png"
                hover "tl/spanish/spanish-play-hover.png"
            elif persistent.lang == "chinese":
                idle "tl/chinese/chinese-play-idle.png"
                hover "tl/chinese/chinese-play-hover.png"
            elif persistent.lang == "russian":
                idle "tl/russian/russian-play-idle.png"
                hover "tl/russian/russian-play-hover.png"
            elif persistent.lang == "turkish":
                idle "tl/turkish/turkish-play-idle.png"
                hover "tl/turkish/turkish-play-hover.png"
            elif persistent.lang == "french":
                idle "tl/french/french-play-idle.png"
                hover "tl/french/french-play-hover.png"
            elif persistent.lang == "italian":
                idle "tl/italian/italian-play-idle.png"
                hover "tl/italian/italian-play-hover.png"
            else:
                idle "main_title_play_button"
                hover "gui/play_button_hover.png"
            xpos 40
            ypos 640
            action Start()








    imagebutton:
        if persistent.lang == "korean":
            idle "tl/korean/korean-about-idle.png"
            hover "tl/korean/korean-about-hover.png"
        elif persistent.lang == "spanish":
            idle "tl/spanish/spanish-about-idle.png"
            hover "tl/spanish/spanish-about-hover.png"
        elif persistent.lang == "chinese":
            idle "tl/chinese/chinese-about-idle.png"
            hover "tl/chinese/chinese-about-hover.png"
        elif persistent.lang == "russian":
            idle "tl/russian/russian-about-idle.png"
            hover "tl/russian/russian-about-hover.png"
        elif persistent.lang == "turkish":
            idle "tl/turkish/turkish-about-idle.png"
            hover "tl/turkish/turkish-about-hover.png"
        elif persistent.lang == "french":
            idle "tl/french/french-about-idle.png"
            hover "tl/french/french-about-hover.png"
        elif persistent.lang == "portuguese":
            idle "tl/portuguese/portuguese-about-idle.png"
            hover "tl/portuguese/portuguese-about-hover.png"
        else:
            idle "main_title_about_button"
            hover "gui/about_button_hover.png"
        xpos 310
        ypos 640
        action ShowMenu("about")

    imagebutton:
        if persistent.lang == "korean":
            idle "tl/korean/korean-quit-idle.png"
            hover "tl/korean/korean-quit-hover.png"
        elif persistent.lang == "spanish":
            idle "tl/spanish/spanish-quit-idle.png"
            hover "tl/spanish/spanish-quit-hover.png"
        elif persistent.lang == "chinese":
            idle "tl/chinese/chinese-quit-idle.png"
            hover "tl/chinese/chinese-quit-hover.png"
        elif persistent.lang == "russian":
            idle "tl/russian/russian-quit-idle.png"
            hover "tl/russian/russian-quit-hover.png"
        elif persistent.lang == "turkish":
            idle "tl/turkish/turkish-quit-idle.png"
            hover "tl/turkish/turkish-quit-hover.png"
        elif persistent.lang == "french":
            idle "tl/french/french-quit-idle.png"
            hover "tl/french/french-quit-hover.png"
        elif persistent.lang == "portuguese":
            idle "tl/portuguese/portuguese-quit-idle.png"
            hover "tl/portuguese/portuguese-quit-hover.png"
        elif persistent.lang == "italian":
            idle "tl/italian/italian-quit-idle.png"
            hover "tl/italian/italian-quit-hover.png"
        else:
            idle "gui/quit_button_idle.png"
            hover "gui/quit_button_hover.png"
        xpos 580
        ypos 640
        action Quit(confirm=not main_menu)

    text _("Copyright 2021 dino999z"):

        ypos 680
        xpos 1250

    add "tite_drop_shadow"
    if persistent.lang is None:
        add "title" xpos 400 ypos 80
    elif persistent.lang == "korean":
        add "title_korean" xpos 400 ypos 80
    elif persistent.lang == "spanish":
        add "title_spanish" xpos 400 ypos 80
    elif persistent.lang == "chinese":
        add "title_chinese" xpos 400 ypos 80
    elif persistent.lang == "russian":
        add "title_russian" xpos 400 ypos 80
    elif persistent.lang == "turkish":
        add "title_turkish" xpos 400 ypos 80
    elif persistent.lang == "french":
        add "title_french" xpos 400 ypos 80
    elif persistent.lang == "portuguese":
        add "title_portuguese" xpos 400 ypos 80
    elif persistent.lang == "japanese":
        add "title_japanese" xpos 400 ypos 80
    elif persistent.lang == "italian":
        add "title_italian" xpos 400 ypos 80
    add "main_title_bad_tv"
    add "dust" zoom 1.0



    frame




















style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True



style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

                if persistent.lang == "korean":

                    text _("Korean Translation: SHADE TV - {font=neodgm.ttf}공포게임 쉐이드{/font}TV, Bridget - {font=neodgm.ttf}정연{/font}\n")

                elif persistent.lang == "spanish":

                    text _("Spanish Translation: Gambas\n")

                elif persistent.lang == "chinese":

                    text _("Chinese Translation: {font=pixel.ttf}林尧 & 丞珞{/front}\n")

                elif persistent.lang == "japanese":

                    text _("Japanese Translation: obatatsu\n")

                elif persistent.lang == "russian":

                    text _("Russian Translation: he2wobuun\n")

                elif persistent.lang == "french":

                    text _("French Translation: Maïlys, Ella and Aymeric\n")

                elif persistent.lang == "turkish":

                    text _("Turkish Translation: Phymos (Yumeshi Novel)\n")

                elif persistent.lang == "portuguese":

                    text _("Portuguese Translation: Rance Guertena\n")

                elif persistent.lang == "italian":

                    text _("Italian Translation: Domtastick & Keyli Yuy")

                text _("Thank you for playing this game!")





define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")









screen preferences():
    tag menu


    use game_menu(_("Pref."), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Language")

                    hbox:
                        textbutton "English" text_font "GenericMobileSystem.ttf" action Language(None)
                        textbutton "한국어" text_font "neodgm.ttf" action Language("korean")
                        textbutton "Español" text_font "GenericMobileSystem.ttf" action Language("spanish")
                        textbutton "Français" text_font "GenericMobileSystem.ttf" action Language("french")
                    hbox:
                        textbutton "中文" text_font "pixel.ttf" action Language("chinese")
                        textbutton "Русский" text_font "Euxoi.ttf" action Language("russian")
                        textbutton "Türkçe" text_font "SHPinscher-Regular.otf" action Language("turkish")
                        textbutton "Português" text_font "GenericMobileSystem.ttf" action Language("portuguese")
                    hbox:
                        textbutton "日本語" text_font "PixelMplus10-Regular.ttf" action Language("japanese")
                        textbutton "Italiano" text_font "GenericMobileSystem.ttf" action Language("italian")


















            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:





                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"



style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450










screen history():




    predict False tag menu

    use game_menu(_("Log"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    on "show" action Function(clack_play_albert)


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 450



screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
