from kivy.uix.label import Label
from kivy.clock import Clock

# Клас для створення віджета, який показуватиме к-ть присідань які залишилося зробити
class Sits(Label):
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        super().__init__(text = f"Залишилося присідань: {self.total}")

    # Метод, який буде спрацьовувати після кожного виконання анімації бігунком
    def next(self, *args):
        self.current += 1
        self.text = f"Залишилося присідань: {self.total - self.current}"
