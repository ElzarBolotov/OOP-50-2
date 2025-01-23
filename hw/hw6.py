class ElectronicDevice:
    def turn_on(self):
        print("Девайс включён")

    def turn_off(self):
        print("Девайс выключен")


class SmartDevice:
    def connect_to_network(self):
        print("Девайс подключен к сети")

    def update_software(self):
        print("Обновление завершено")


class AudioDevice:
    def play_sound(self):
        print("Звук включён")

    def stop_sound(self):
        print("Звук выключен")



class SmartSpeaker(ElectronicDevice, SmartDevice, AudioDevice):
    def __init__(self, model):
        self.model = model

    def play_music(self):
        print(f"Музыка играет в {self.model}")

    def stop_music(self):
        print(f"Музыка в {self.model} остановилась")



smart_speaker = SmartSpeaker("Yamaha")


smart_speaker.turn_on()
smart_speaker.connect_to_network()
smart_speaker.play_sound()


smart_speaker.play_music()
smart_speaker.stop_music()


smart_speaker.turn_off()
