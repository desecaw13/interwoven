# inventory system

init python:
    class Evidence:
        def __init__(self, name, pic):
            self.name = name
            self.pic = pic

default evidence = set()
default evidence_dict = {
        "pepper": Evidence("Pepper", "tmp icon"),
        "alt pepper": Evidence("Pepper", "tmp alt icon"),
    }
