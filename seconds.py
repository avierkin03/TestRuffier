from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

# Клас для створення віджета-секундоміра
class Seconds(Label):
    done = BooleanProperty(False)
    
    def __init__(self, total, **kwargs):
        self.done = False
        self.current = 0
        self.total = total
        super().__init__(text = f"Пройшло секунд: {self.current}")

    # метод, який перезапускає наш секундомір
    def restart(self, total):
        self.done = False
        self.current = 0
        self.text = f"Пройшло секунд: {self.current}"
        self.total = total
        self.start()

    # метод, який запускає наш секундомір
    def start(self):
        Clock.schedule_interval(self.change, 1)

    # метод, який буде викликатися щосекунди після запуску секундоміра
    def change(self, dt):
        self.current += 1
        self.text = f"Пройшло секунд: {self.current}"
        if self.current >= self.total:
            self.done = True
            return False


