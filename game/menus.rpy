# screens for menus

screen inventory():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xpadding 20 ypadding 20

        hbox spacing 100:
            label "Inventory"
            use item('Pepper') # todo: make conditional
            imagebutton:
                idle "close button"
                action Hide("inventory")

screen notebook():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xpadding 20 ypadding 20

        hbox spacing 100:
            label "Notebook"
            imagebutton:
                idle "close button"
                action Hide("notebook")

screen item(name):
    frame:
        xpadding 20 ypadding 20

        vbox spacing 20:
            label name
            imagebutton idle "tmp icon"
