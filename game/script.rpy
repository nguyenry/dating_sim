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
define choosed_char = "None"

# Images
image char_select = "images/characters/character_select_screen.png"

# Movies
image main_menu_mov = Movie(play="gui/main_menu.webm")
image sakura_mov = Movie(play="images/sakura_short.webm")
image sakura_scary = Movie(play="images/sakura_scary.webm")
image quote = Movie(play="")

# Audio

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ renpy.movie_cutscene("images/ai_quote_wsound.webm")

    play sound "audio/anime-wow-sound-effect_3sfDUWt.ogg"

    init python:
        renpy.music.register_channel("background", "music")
    play background "audio/romantic - yu yu hakusho.ogg"

    scene char_select
    with fade
    
    "Select an AI assistant to help you create the perfect you by clicking on them.{p=2.0}{nw}"

    call screen character_choose

    label init:
        play sound "audio/bubble click.ogg"
        scene classroom
        with fade

        play sound "audio/japanese school bell sound.ogg"
        image char = "images/[choosed_char].png"
        show char at center, size_normal

    a "Welcome to My Romance Academia!{w=1.0} Click anywhere to continue."

    a "I will be your AI assistant as we curate your profile to maximize your chances on the dating scene!"

    python:
        povname = renpy.input("First, what is your name? Start typing and then press Enter/Return.", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Admin"
        

    a "Hi [povname]! Let's start with your physical appearance, which has a 90\% weighting on profile priorities according to data we have collected from users."

    menu:
        "What is your hair color?"

        "Black":
            $ renpy.movie_cutscene("images/puke.webm")
            a "Ew, what are we? A 2000's emo goth baddie?"
        "Brown":
            $ renpy.movie_cutscene("images/puke.webm")
            a "Boringggg..."
        "Blonde":
            a "Ok, conventional, period. Blondes got a 90\% successful match rating on our apps, so you are in good hands."
        "Gray":
            $ renpy.movie_cutscene("images/puke.webm")
            a "Wow, this a dating app, not a funeral."

    menu:
        "How about your eye color?"

        "Black":
            $ renpy.movie_cutscene("images/eva-asuka.webm")
            a "Our data analytics show users with black eyes have a successful match rate of 1\%. Try harder."
        "Brown":
            $ renpy.movie_cutscene("images/eva-asuka.webm")
            a "Our data analytics show users with brown eyes have a successful match rate of 3\%. Try harder."
        "Green":
            $ renpy.movie_cutscene("images/eva-eye.webm")
            a "Our data analytics show users with green eyes have a successful match rate of 10\%. Try harder."
        "Blue":
            a "Our data analytics show users with blue eyes have a successful match rate of 99\%. Slay!"

    menu:
        "What is your race?"

        "Hispanic or Latino":
            a "Something"
        "White":
            a "Something"
        "Black or African American":
            $ renpy.movie_cutscene("images/chris-voodoo.webm")
            a "Our data shows that Black or African Americans frequently report being fetishized on our apps. Try something else."
        "Native Hawaiian or Other Pacific Islander":
            $ renpy.movie_cutscene("images/moana-pee.webm")
            a "Exotic..."
        "Asian":
            $ renpy.movie_cutscene("images/eeaao-snot.webm")
            a "Oof, sorry, Asians have the lowest rate of matches."
        "Two or More Races":
            a "Something"

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
                $ renpy.movie_cutscene("images/katy perry - roar.webm")
                a "Ew, what the fuck? Is there shit stringing along your ass hairs?"
                jump young
            "Monthly":
                $ renpy.movie_cutscene("images/katy perry - roar.webm")
                a "Ew, what the fuck? Is there shit stringing along your ass hairs?"
                jump young
            "Never":
                $ renpy.movie_cutscene("images/bart baker - 22.webm")
                a "Ew, am I supposed to braid your shit-stained ass hairs?"
                jump young
    
    label hairy:
        menu:
            "How hairy are you?"

            "Very":
                a "Perfect, the twinks are gonna love you."
                jump old
            "Not really":
                a "Oof, you're just a fem twink bottom bitch, then."
                $ renpy.movie_cutscene("images/knives out - gag.webm")
                jump old

    label young:
        menu:
            "How old are you?"

            "18-24":
                a "Okok, legal, chill."
                jump size
            "25+":
                a "Get the fuck outta here, hag!"
                $ renpy.movie_cutscene("images/knives out - puke.webm")
                jump size

    label old:
        menu:
            "How old are you?"

            "50+":
                a "Those daddy-issue twinks are gonna love you..."
                jump size
            "< 50":
                $ renpy.movie_cutscene("images/knives out - puke.webm")
                jump size

    label size:
        menu:
            "How big are you?"

            "1 foot":
                a "Get those size queens, daddy!"
            "< 1 foot":
                $ renpy.movie_cutscene("images/knives out - confession.webm")
                a "Ooo, sorry, guess you're a bottom. Slay!"
    
    scene sakura_scary
    with pixellate
    show char at center, size_normal

    a "Thank you for participating in our survey!"

    a "We now have enough data to create the perfect you! But first, we need you to provide the following information:"

    python:
        legalName = renpy.input("Full Legal Name (First MI Last):", length=64)
        legalName = legalName.strip()

        if not legalName:
            legalName = "Admin"

    python:
        email = renpy.input("Email:", length=256)
        email = email.strip()

        if not email:
            email = "disgusting@loser.com"

    python:
        address = renpy.input("Residential Address:", length=256)
        address = address.strip()

        if not address:
            address = "6666 Stupidbitch Rd., Dumbville, JK 69420"

    python:
        phoneNum = renpy.input("Phone Number:", length=32)
        phoneNum = phoneNum.strip()

        if not phoneNum:
            phoneNum = "(555) 666-6666"

    python:
        ssn = renpy.input("Social Security Number:", length=32)
        ssn = phoneNum.strip()

        if not ssn:
            ssn = "123 45 6789"

    menu:
        "Perfect! Are you ready for your avatar?"

        "Yes":
            a "That'll be $15, then. Please click on the following {a=https://forms.gle/PGtNg7xcqv5uNH4SA}link{/a} to complete your transaction."
        "No":
            a "That's too bad. That'll be $15 either way. Please click on the following {a=https://forms.gle/PGtNg7xcqv5uNH4SA}link{/a} to complete your transaction."

    a "Did you follow the {a=https://forms.gle/PGtNg7xcqv5uNH4SA}link{/a}? You won't become the perfect you if you don't fill out the link!"

    $ renpy.movie_cutscene("images/ending.webm")

    # This ends the game.

    return
