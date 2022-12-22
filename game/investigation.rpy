# screens for investigations

init python:
    def say_this(text):
        renpy.show_screen("hud")
        renpy.say(a, text)

screen test_investigation(__is_normal):

    if __is_normal:
        imagebutton:
            align (0.25, 0.25)
            idle "tmp icon"

            if evidence_dict["pepper"] in evidence:
                action Function(renpy.invoke_in_new_context, say_this, "I looked at this already.")
                #action Call("already_done", from_current=True)
            else:
                action Call("test_pepper")
    else:
        imagebutton:
            align (0.75, 0.75)
            idle "tmp alt icon"

            if evidence_dict["alt pepper"] in evidence:
                action Call("already_done", from_current=True)
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


label already_done:
    a "I looked at this already."
    return
