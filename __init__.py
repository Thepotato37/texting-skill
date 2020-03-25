from mycroft import MycroftSkill, intent_file_handler


class Texting(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('texting.intent')
    def handle_texting(self, message):
        self.speak_dialog('texting')


def create_skill():
    return Texting()

