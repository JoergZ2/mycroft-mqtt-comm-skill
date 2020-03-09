from mycroft import MycroftSkill, intent_file_handler


class MycroftMqttComm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('comm.mqtt.mycroft.intent')
    def handle_comm_mqtt_mycroft(self, message):
        self.speak_dialog('comm.mqtt.mycroft')


def create_skill():
    return MycroftMqttComm()

