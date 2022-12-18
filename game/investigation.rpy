# screens for investigation

screen test_investigation(__is_normal):

    imagebutton:
        if __is_normal:
            xalign 0.25 yalign 0.25
            idle "tmp icon"
        else:
            xalign 0.75 yalign 0.75
            idle "tmp alt icon"
        action Return()
