screen character_choose:
    add "images/characters/character_select_screen.png"

    imagebutton:
        auto "images/characters/char_bear_%s.png"
        focus_mask True
        # action [SetVariable("choosed_char", "bear"), Jump("bear")]
        action [SetVariable("choosed_char", "bear"), Jump("init")]

    imagebutton:
        auto "images/characters/char_dolphin_%s.png"
        focus_mask True
        # action [SetVariable("choosed_char", "dolphin"), Jump("dolphin")]
        action [SetVariable("choosed_char", "dolphin"), Jump("init")]

    imagebutton:
        auto "images/characters/char_twunk_%s.png"
        focus_mask True
        # action [SetVariable("choosed_char", "twunk"), Jump("twunk")]
        action [SetVariable("choosed_char", "twunk"), Jump("init")]

    imagebutton:
        auto "images/characters/char_twink_%s.png"
        focus_mask True
        # action [SetVariable("choosed_char", "twink"), Jump("twink")]
        action [SetVariable("choosed_char", "twink"), Jump("init")]

    imagebutton:
        auto "images/characters/char_twinkie_%s.png"
        focus_mask True
        # action [SetVariable("choosed_char", "ai happy"), Jump("twinkie")]
        action [SetVariable("choosed_char", "ai happy"), Jump("init")]
