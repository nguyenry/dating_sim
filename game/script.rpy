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

default name = "Me"

define a = Character("Al")
define m = Character("[name]")

# Movies

image sakura_mov = Movie(play="images/sakura_short.webm")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bedroom

    m "Huh? W-what the fuck happened?"

    "You wake up in bed, ready for the first day of school."

    m "What?? No, no... I... I was just in my room..."

    m "I put on this h-headset and..."

    "Oh! Did you hear that? It's time for your first day of school!"

    "Aren't you excited?"

    m "What? No, how the FUCK do I get out of here??"

    "Oh, hush, you're going to be late! C'mon, let's get ready and go to school!"

    m "NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. NO. "

    scene sakura_mov
    with fade

    "Wow! Made it just in time for your first class."

    "Oh, but who is that?"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ai happy at center, size_normal

    # These display lines of dialogue.

    "It's you're new AI boyfriend, AI, whose personality is derived from your Internet activity :)"

    # Flash scary AI

    m "W-what in the fresh titty..."

    a "Hi! As you know, I'm AI. What's your name?"

    m "My name is... My na-... FUck... FUCK, why can't I remember my name??"

    a "That's ok! For now, you can have a default name \"Admin\" ;)"

    $ name = "Admin"

    m "Huh? No, I don't understand. What the hell is going on here. GET ME OUT OF HERE{nw}"
    with dissolve


    a "Ah, that's much better! C'mon, let's go to class before we're late!"

    scene classroom

    show ai happy at center, size_normal

    a "Sit down next to me, Admin!"

    m "No, no, you're not real... This is just a dream. Yeah, yeah... That explains it."

    a "Real, not real.. Dream, not a dream. What does it matter? I'm here. You're here."

    a "You can understand me. And I understand you..."

    m "No, you don't understand shit. I have a life. You are just a game."

    scene classroom_invert

    show ai scary at center, size_normal

    a "What?"

    m "Fuck, please, just let me leave."

    a "I really thought you'd be different from the rest, but I guess humans are all the same."

    # This ends the game.

    return
