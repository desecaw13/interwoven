# heads up display

screen hud():
    imagebutton:
        xalign 0.0
        idle "inventory button"
        action Show("inventory")
    imagebutton:
        xalign 1.0
        idle "notebook button"
        action Show("notebook")
    if is_investigation:
        imagebutton:
            xalign 0.5
            idle "weave button"
            keysym "w"
            action ToggleVariable("is_normal"), Jump(current_label)

screen disabled_hud():
    imagebutton:
        xalign 0.0
        idle "inventory button"
        action Show("inventory")
    imagebutton:
        xalign 1.0
        idle "notebook button"
        action Show("notebook")
    if is_investigation:
        imagebutton:
            xalign 0.5
            idle "weave disabled button"
