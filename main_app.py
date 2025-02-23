from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits  
from ruffier import test         
from seconds import Seconds                                                    

p1 = 0
p2 = 0 
p3 = 0
age = 7
name = ""

# Функція, яка повертає число або False, якщо рядок не конвертується
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

# Клас для створення першого екрану (з інструкцією)
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instructions = Label(text = txt_instruction)
        self.lbl_name = Label(text = "Введіть ім'я")
        self.lbl_age = Label(text = "Введіть вік")
        self.input_name = TextInput(multiline = False)
        self.input_age = TextInput(multiline = False)
        self.button = Button(text = "Почати", size_hint = (0.3, 0.2), pos_hint = {"center_x": 0.5})
        self.button.on_press = self.next

        self.name_layout = BoxLayout(size_hint = (0.8, 0.15))
        self.name_layout.add_widget(self.lbl_name)
        self.name_layout.add_widget(self.input_name)

        self.age_layout = BoxLayout(size_hint = (0.8, 0.15))
        self.age_layout.add_widget(self.lbl_age)
        self.age_layout.add_widget(self.input_age)

        self.main_layout = BoxLayout(orientation = "vertical", spacing = 8, padding = 8)
        self.main_layout.add_widget(self.instructions)
        self.main_layout.add_widget(self.name_layout)
        self.main_layout.add_widget(self.age_layout)
        self.main_layout.add_widget(self.button)

        self.add_widget(self.main_layout)

    # метод, що спрацьовує при натисканні на кнопку "Почати"
    def next(self):
        global name, age
        name = self.input_name.text
        age = check_int(self.input_age.text)

        if age == False:
            self.input_age.text = "Введіть ціле число"
        elif age < 7:
            self.input_age.text = "Введіть число більше 7"
        elif not name.strip():
            self.input_name.text = "Введіть ваше ім'я"
        else:
            self.manager.current = "pulse"



# Клас для створення другого екрану (з першим вимірюванням пульсу)         
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instructions = Label(text = txt_test1)
        self.lbl_result = Label(text = "Введіть результат")
        self.input_result = TextInput(multiline = False)
        self.input_result.set_disabled(True)        # блокуємо поле для введення результату
        self.button = Button(text = "Продовжити", size_hint = (0.3, 0.2), pos_hint = {"center_x": 0.5})
        self.button.on_press = self.next
        self.lbl_seconds = Seconds(15)  # створюємо віджет-секундомір
        self.next_screen = False        # властивість, яка "пропускатиме" нас на наступний екран

        self.result_layout = BoxLayout(size_hint = (0.8, 0.1))
        self.result_layout.add_widget(self.lbl_result)
        self.result_layout.add_widget(self.input_result)

        self.main_layout = BoxLayout(orientation = "vertical", spacing = 8, padding = 8)
        self.main_layout.add_widget(self.instructions)
        self.main_layout.add_widget(self.lbl_seconds)     # додаємо віджет-секундомір у вертикальний лейаут (під інструкцією)
        self.main_layout.add_widget(self.result_layout)
        self.main_layout.add_widget(self.button)

        self.add_widget(self.main_layout)

    # метод, що спрацьовує при натисканні на кнопку "Продовжити"
    def next(self):
        # якщо нам ще не можна на наступний екран 
        if not self.next_screen:
            self.button.set_disabled(True) 
            self.lbl_seconds.start()
        # якщо нам вже можна на наступний екран 
        else:
            global p1
            p1 = check_int(self.input_result.text)
            if p1 == False:
                self.input_result.text = "Введіть ціле число"
            elif p1 <= 0 or p1 >= 50:
                self.input_result.text = "Виміряйте пульс ще раз"
            else:
                self.manager.current = "sits"
    


# Клас для створення третього екрану (з присіданнями)     
class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instructions = Label(text = txt_test2)
        self.button = Button(text = 'Продовжити', size_hint = (0.3, 0.2), pos_hint = {'center_x': 0.5})
        self.button.on_press = self.next

        main_line = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        main_line.add_widget(instructions)
        main_line.add_widget(self.button)
        self.add_widget(main_line)

    # метод, що спрацьовує при натисканні на кнопку "Продовжити"
    def next(self):
        self.manager.current = 'pulse2'
    
  

# Клас для створення четвертого екрану (з останніми двома вимірюваннями пульсу)   
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instructions = Label(text = txt_test3)
        lbl_result1 = Label(text = 'Результат:')
        self.enter_result1 = TextInput(text = '0', multiline = False)
        lbl_result2 = Label(text = 'Результат після відпочинку:')
        self.enter_result2 = TextInput(text = '0', multiline = False)
        self.button = Button(text = 'Завершити', size_hint = (0.3, 0.2), pos_hint = {'center_x': 0.5})
        self.button.on_press = self.next

        line1 = BoxLayout(size_hint = (0.8, 0.1))
        line1.add_widget(lbl_result1)
        line1.add_widget(self.enter_result1)

        line2 = BoxLayout(size_hint = (0.8, 0.1))
        line2.add_widget(lbl_result2)
        line2.add_widget(self.enter_result2)

        main_line = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        main_line.add_widget(instructions)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.button)
        self.add_widget(main_line)
    
    # метод, що спрацьовує при натисканні на кнопку "Завершити"
    def next(self):
        global p2, p3
        p2 = check_int(self.enter_result1.text)
        p3 = check_int(self.enter_result2.text)

        if p2 == False:
            self.enter_result1.text = "Введіть ціле число"
        elif p2 <= 0 or p2 >= 50:
            self.enter_result1.text = "Виміряйте пульс ще раз"
        elif p3 == False:
             self.enter_result2.text = "Введіть ціле число"
        elif p3 <= 0 or p3 >= 50:
            self.enter_result2.text = "Виміряйте пульс ще раз"
        else:
            self.manager.current = 'result'
        


# Клас для створення п'ятого екрану (з результатом)   
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instructions = Label(text = '')

        self.main_layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.main_layout.add_widget(self.instructions)

        self.add_widget(self.main_layout)
        self.on_enter = self.before

    def before(self):
        global name
        self.instructions.text = name + '\n' + test(p1, p2, p3, age)



# Клас для створення додатку
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name = "instructions"))
        sm.add_widget(PulseScr(name = "pulse"))
        sm.add_widget(CheckSits(name = "sits"))
        sm.add_widget(PulseScr2(name = "pulse2"))
        sm.add_widget(Result(name = "result"))
        return sm


app = HeartCheck()
app.run()