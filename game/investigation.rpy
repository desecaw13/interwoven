# screens for investigation

screen test_investigation(__is_normal):

    if __is_normal:
        imagebutton:
            xalign 0.25 yalign 0.25
            idle "tmp icon"

            if evidence_dict["pepper"] in evidence:
                action Jump("already_done")
            else:
                action Jump("test_pepper")
    else:
        imagebutton:
            xalign 0.75 yalign 0.75
            idle "tmp alt icon"
            action If(evidence_dict["alt pepper"] in evidence, Jump("already_done"), Jump("test_alt_pepper"))

label test_pepper:
    a "this is some text about peppers"
    $ evidence.add(evidence_dict["pepper"])
    return
label test_alt_pepper:
    a "why is it purple..."
    $ evidence.add(evidence_dict["alt pepper"])
    return

label already_done:
    # chage random, individually, or not at all?
    a "I looked at this already."
    jump investigation
