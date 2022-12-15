
define isNormal = True

define a = Character("Amaya")

label start:
    $ isNormal = True

    scene bg normal room

    show screen hud
    
    "A body has been discovered"

    show amaya suprised

    a "This is so sad frfr"

    return

label alt_start:
    $ isNormal = False

    scene bg alt room

    show screen hud

    "A body was discovered"

    show alt amaya suprised

    a "I am not actually Amaya"

    return

label test:
    "test"
