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
        if is_normal:
            action Jump("alt_" + current_label)
        else:
            action Jump(current_label)
