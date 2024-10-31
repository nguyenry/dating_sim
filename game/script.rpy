# The script of the game goes in this file.

# Transforms

transform size_normal:
    ysize 1000
    fit "contain"

transform size_close:
    ysize 1200
    fit "contain"

transform size_far:
    ysize 500
    fit "contain"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Al")
define m = Character("[povname]")

# Movies
image main_menu_mov = Movie(play="gui/main_menu.webm")
image sakura_mov = Movie(play="images/sakura_short.webm")
image puke_mov = Movie(play="images/puke.webm")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene main_menu_mov
    # with fade

    # "\"AI is something that is kind of present in your profile always and makes suggestions to you.\" - CEO of Grindr"

    scene classroom
    with fade

    show ai happy at center, size_normal

    a "Welcome to My Romance Academia!"

    a "I will be your AI assistant as we curate your profile to maximize your chances on the dating scene! First, what is your name?"

    # $ povname = renpy.input("What is your name?", length=15, exclude=" 0123456789+=,.?!<>{}[]").strip() or "Admin"
    python:
        povname = renpy.input("What is your name? Type here.", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Admin"
        

    a "Hi [povname]! Let's start with your physical appearance, which has a 90\% weighting on profile priorities according to data we have collected from users."

    menu:
        "What is your hair color?"

        "Black":
            jump puke
        "Brown":
            jump puke
        "Blonde":
            jump puke
        "Gray":
            jump puke

    label puke:
        # show puke_mov
        $ renpy.movie_cutscene("images/puke.webm")

    a "Cue some explanation of why that is bad."


    menu:
        "What is your body type?"

        "Twink":
            jump hairless
        "Twunk":
            jump hairless
        "Dolphin":
            jump hairless
        "Otter":
            jump hairy
        "Bear":
            jump hairy

    label hairless:
        menu:
            "How often do you shave?"

            "Daily":
                a "Okok, that's a good amount."
                jump young
            "Weekly":
                a "Ew, what the fuck is there shit stringing on your ass hairs?"
                jump young
            "Monthly":
                $ renpy.movie_cutscene("images/puke.webm")
                jump young
            "Never":
                $ renpy.movie_cutscene("images/puke.webm")
                jump young
    
    label hairy:
        menu:
            "How hairy are you?"

            "Very":
                a "Perfect, the twinks are gonna love you."
                jump old
            "Not really":
                a "Oof, you're just a fem twink bottom bitch, then."
                $ renpy.movie_cutscene("images/puke.webm")
                jump old

    label young:
        menu:
            "How old are you?"

            "18-24":
                a "Okok, legal, chill."
                jump size
            "25+":
                a "Get the fuck outta here, hag!"
                $ renpy.movie_cutscene("images/puke.webm")
                jump size

    label old:
        menu:
            "How old are you?"

            "50+":
                a "Those daddy issue twinks are gonna love you..."
                jump size
            "< 50":
                $ renpy.movie_cutscene("images/puke.webm")
                jump size

    label size:
        menu:
            "How big are you?"

            "1 foot":
                a "Get those size queens, daddy!"
            "< 1 foot":
                a "Ooo, sorry, guess you're a bottom. Slay!"
    
    a "Cue contact information input form."

    a "Cue paywall."


    # scene classroom_invert

    # show ai scary at center, size_normal

    # a "What?"

    # m "Fuck, please, just let me leave."

    # a "I really thought you'd be different from the rest, but I guess humans are all the same."

    # This ends the game.

    return
