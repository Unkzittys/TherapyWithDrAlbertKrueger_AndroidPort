define a = Character(_("Albert"), callback=beep_albert, what_color = "#CE0892",ctc="ctc_blink", ctc_position="nestled")
define a_think = Character(_("Albert"), what_color = "#CE0892",ctc="ctc_blink", ctc_position="nestled")
define t = Character(_("Taylor"), callback=beep_taylor, what_color = "#291E26",ctc="ctc_blink", ctc_position="nestled")
define t_think = Character(_("Taylor"), what_color = "#291E26",ctc="ctc_blink", ctc_position="nestled")
define n = Character("", what_slow_cps=5, callback=beep_question, what_color = "#000000", what_size=100, advance=False, what_font="GenericMobileSystem.ttf")
define n2 = Character("", what_slow_cps=0, what_color = "#000000", advance=False)
define o = Character(_("Nurse"), callback=beep_nurse, what_color = "#64535A",ctc="ctc_blink", ctc_position="nestled")
define v = Character(_("???"), callback=beep_vincent, what_color = "#260756",ctc="ctc_blink", ctc_position="nestled")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
