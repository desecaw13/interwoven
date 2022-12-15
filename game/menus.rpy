# screens for menus

screen inventory:
    modal True
    hbox xalign 0.5 yalign 0.5 spacing 100:
        text "inv"
        imagebutton:
            idle "tmp close button"
            action Hide("inventory")

screen notebook:
    modal True
    hbox xalign 0.5 yalign 0.5 spacing 100:
        text "nb"
        imagebutton:
            idle "tmp close button"
            action Hide("notebook")
