# screens for menus

screen inventory():
    modal True
    frame:
        align (0.5, 0.5)
        padding (20, 20)

        hbox spacing 100:
            label "Inventory"
            
            for x in evidence:
                use item(x.name, x.pic)

            imagebutton:
                idle "close button"
                action Hide("inventory")

screen notebook():
    modal True
    frame:
        align (0.5, 0.5)
        padding (20, 20)

        hbox spacing 100:
            label "Notebook"
            imagebutton:
                idle "close button"
                action Hide("notebook")

screen item(name, pic):
    frame:
        padding (20, 20)

        vbox spacing 20:
            label name
            imagebutton idle pic
