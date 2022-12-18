# main script and where the game starts

# sets `current_label` to the name of the current label unless it is a renpy internal or in the alternate dimensions
init python:
    def label_callback(name, abnormal):
        if name.startswith("_") or name.startswith("alt_"): return
        store.current_label = name

    config.label_callback = label_callback


# bool definitions
define is_normal = True # tells which dimensions the player is in
define is_investigation = False

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

label investigation:
    $ is_investigation = True

    if is_normal:
        scene bg sitroom
    else:
        scene bg alt sitroom

    show screen hud

    call screen test_investigation

    $ is_investigation = False # move ?
    return
