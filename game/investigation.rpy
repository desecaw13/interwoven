# screens for investigations

init python:

    # handles Amaya saying things during picking up evidence
    def a_say(text="I looked at this already."):
        renpy.show_screen("disabled_hud")
        # IDEA: could show a disabled investigation here
        a(text)
        #evidence.add(evidence_dict["alt pepper"])


screen test_investigation(__is_normal):

    if __is_normal:
        imagebutton:
            align (0.25, 0.25)
            idle "tmp icon"

            if evidence_dict["pepper"] in evidence:
                action Function(renpy.invoke_in_new_context, a_say)
            else:
                action Function(renpy.invoke_in_new_context, a_say, "Wow, I sure do love peppers."), AddToSet(evidence, evidence_dict["pepper"])
    else:
        imagebutton:
            align (0.75, 0.75)
            idle "tmp alt icon"

            if evidence_dict["alt pepper"] in evidence:
                action Function(renpy.invoke_in_new_context, a_say)
            else:
                action Function(renpy.invoke_in_new_context, a_say, "Why is it purple..."), AddToSet(evidence, evidence_dict["alt pepper"])
