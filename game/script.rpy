# main script and where the game starts

# sets `current_label` to the name of the current label unless it is a renpy internal or in the alternate dimensions
init python:
    def label_callback(name, abnormal):
        if name.startswith("_") or name.startswith("alt_"): return
        store.current_label = name

    config.label_callback = label_callback


# bool definitions
default is_normal = True # tells which dimensions the player is in
default is_investigation = False

# image definitions
image bg sitroom = "backgrounds/sittingroom.png"
image bg alt sitroom = "backgrounds/sittingroomalt.png"

# character definitions
define a = Character("Amaya")


# label definitions
label main_menu:
    jump start # tmp

label start:
    jump investigation # tmp

    scene bg room

    show screen hud

    "A body has been discovered"

    show amaya suprised

    a "This is so sad frfr"

    return

label investigation:
    $ is_investigation = True

    $ music_time = renpy.music.get_pos()

    if is_normal:
        if music_time == None:
            play music "audio/invest/invest1.wav" fadein 0.4
        else:
            play music "<from " + str(music_time) + " loop 0>audio/invest/invest1.wav" fadein 0.4

        scene bg sitroom
    else:
        if music_time == None:
            play music "audio/invest/invest2.wav" fadein 0.4
        else:
            play music "<from " + str(music_time) + " loop 0>audio/invest/invest2.wav" fadein 0.4

        scene bg alt sitroom

    show screen hud

    call screen test_investigation(is_normal) with Pixellate(0.75, 5)

    $ is_investigation = False # move ?
    return
