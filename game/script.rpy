# main script and where the game starts

# sets `current_label` to the name of the current label unless it is a renpy internal or in the alternate dimensions
init python:
    def label_callback(name, abnormal):
        if name.startswith("_") or name.startswith("alt_"): return
        store.current_label = name

    config.label_callback = label_callback

# tells which dimensions the player is in
define is_normal = True

# character definitions
define a = Character("Amaya")

label start:
    $ is_normal = True

    scene bg normal room

    show screen hud
    
    "A body has been discovered"

    show amaya suprised

    a "This is so sad frfr"

    return

label alt_start:
    $ is_normal = False

    scene bg alt room

    show screen hud

    "A body was discovered"

    show alt amaya suprised

    a "I am not actually Amaya"

    return

label test:
    "test"
