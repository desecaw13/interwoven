# heads up display

screen hud:
    imagebutton:
        xalign 0.0
        idle "tmp inventory button"
        action Show("inventory")
    imagebutton:
        xalign 1.0
        idle "tmp notebook button"
        action Show("notebook")
    imagebutton:
        xalign 0.5
        idle "tmp weave button"
        if isNormal:
            action Jump("alt_start")
        else:
            action Jump("start")
