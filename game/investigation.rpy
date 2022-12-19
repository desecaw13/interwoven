# screens for investigations

screen test_investigation(__is_normal):

    if __is_normal:
        imagebutton:
            xalign 0.25 yalign 0.25
            idle "tmp icon"

            if evidence_dict["pepper"] in evidence:
                action Call("already_done", "investigation")
            else:
                action Call("test_pepper")
    else:
        imagebutton:
            xalign 0.75 yalign 0.75
            idle "tmp alt icon"

            if evidence_dict["alt pepper"] in evidence:
                action Call("already_done", "investigation")
            else:
                action Call("test_alt_pepper")

label test_pepper:
    a "this is some text about peppers"
    $ evidence.add(evidence_dict["pepper"])
    jump investigation

label test_alt_pepper:
    a "why is it purple..."
    $ evidence.add(evidence_dict["alt pepper"])
    jump investigation


label already_done(back):
    a "I looked at this already."
    jump expression back
