from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout

# Клас для створення віджета-бігунка
class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)

    def __init__(self, total, steptime, auterepeat=True, bcolor=(0.73, 0.15, 0.96, 1), btext_inprogress="Присідання", **kwargs): 
        super().__init__(**kwargs)
        self.total = total
        self.autorepeat = auterepeat
        # анімація складається з двох частин: спочатку позиція поміняється на "top": 0.1, а потім знову поміняється на "top": 1.0
        # сумарно це має відбутися за 1.5 секунди
        self.anim = Animation(pos_hint = {"top": 0.1}, duration = steptime/2) + Animation(pos_hint = {"top": 1.0}, duration = steptime/2)
        self.anim.on_progress = self.next
        self.button = Button(text = btext_inprogress, background_color = bcolor, pos_hint = {"top": 1.0}, size_hint = (1, 0.1))
        self.add_widget(self.button)

    # метод для запуску бігунка
    def start(self):
        self.value = 0
        self.finished = False
        #запускаємо автоповтор анімації
        if self.autorepeat:
            self.anim.repeat = True
        #включаємо анімацію для кнопки
        self.anim.start(self.button)

    # метод, який спрацьовує під час анімації
    def next(self, widget, step):
        if step == 1:
            self.value += 1
            # якщо зроблено достатньо переміщень 
            if self.value >= self.total:
                #зупиняємо повтор анімації
                self.anim.repeat = False
                self.finished = True
