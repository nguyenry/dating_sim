screen character_choose:
    add "images/characters/character_select_screen.png"

    imagebutton:
        auto "images/characters/char_bear_%s.png"
        focus_mask True
        action [SetVariable("choosed_char", "bear"), Jump("init")]

    imagebutton:
        auto "images/characters/char_dolphin_%s.png"
        focus_mask True
        action [SetVariable("choosed_char", "dolphin"), Jump("init")]

    imagebutton:
        auto "images/characters/char_twunk_%s.png"
        focus_mask True
        action [SetVariable("choosed_char", "twunk"), Jump("init")]

    imagebutton:
        auto "images/characters/char_twink_%s.png"
        focus_mask True
        action [SetVariable("choosed_char", "twink"), Jump("init")]

    imagebutton:
        auto "images/characters/char_twinkie_%s.png"
        focus_mask True
        action [SetVariable("choosed_char", "ai happy"), Jump("init")]

image sakura_mov = Movie(play="images/sakura_short.webm")

screen contact_info:
    add "sakura_mov"

    default mcfirst_value = ""
    default mclast_value = ""
    default active_input = 1

    vbox:
        ypos 100
        xalign 0.5
        spacing 10
        xsize 400
        label "First Name"
        frame:
            xalign 0.5
            xfill True
            padding (10,10)
            if active_input == 1:
                input value ScreenVariableInputValue('mcfirst_value') pixel_width 200 length 30
            else:
                textbutton "[mcfirst_value]" action SetScreenVariable("active_input", 1)
    vbox:
        ypos 300
        xalign 0.5
        spacing 10
        xsize 400
        label "Last Name"
        frame:
            xalign 0.5
            xfill True
            padding (10,10)
            if active_input == 2:
                input value ScreenVariableInputValue("mclast_value") pixel_width 200 length 30
            else:
                textbutton "[mclast_value]" action SetScreenVariable("active_input", 2)