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

define a = Character("AI")
define m = Character("Me")

# Movies

image sakura_mov = Movie(play="images/sakura_short.webm")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bedroom

    "You wake up in bed, ready for the first day of school."

    m "Whaaaaaa"

    scene sakura_mov
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ai happy at center, size_normal

    # These display lines of dialogue.

    a "You've created a new Ren'Py game."

    a "Once you add a story, pictures, and music, you can release it to the world!"

    m "Woahhhh, that's so cool!"

    # This ends the game.

    return
