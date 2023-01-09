from ui_calculator import Ui_main_window
from PySide6.QtWidgets import QMainWindow

class Calculator(Ui_main_window, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #connecting num buttons
        self.zero_button.clicked.connect(self.add_digit)
        self.one_button.clicked.connect(self.add_digit)
        self.two_button.clicked.connect(self.add_digit)
        self.three_button.clicked.connect(self.add_digit)
        self.four_button.clicked.connect(self.add_digit)
        self.five_button.clicked.connect(self.add_digit)
        self.six_button.clicked.connect(self.add_digit)
        self.seven_button.clicked.connect(self.add_digit)
        self.eight_button.clicked.connect(self.add_digit)
        self.nine_button.clicked.connect(self.add_digit)

        #connecting backspace button
        self.esc_button.clicked.connect(self.delete_one_digit)

        #connecting dot and change sign buttons
        self.dot_button.clicked.connect(self.add_dot)
        self.ch_sign_button.clicked.connect(self.change_sign)

        #connecting remove buttons
        self.c_button.clicked.connect(self.remove)
        self.ce_button.clicked.connect(self.remove)

        #connecting math operations
        self.plus_button.clicked.connect(self.action)
        self.divide_button.clicked.connect(self.action)
        self.minus_button.clicked.connect(self.action)
        self.multip_button.clicked.connect(self.action)

        #connecting equals button
        self.equal_button.clicked.connect(self.calculate_answer)
    
    def add_digit(self):
        button = self.sender()
        if self.answer_line.text() == '0':
            self.answer_line.setText(button.text())
        else:
            self.answer_line.setText(self.answer_line.text() + button.text())
    
    def delete_one_digit(self):
        if self.answer_line.text():
            self.answer_line.setText(self.answer_line.text()[:-1])
    
    def add_dot(self):
        if self.answer_line.text():
            self.answer_line.setText(self.answer_line.text() + '.')
    
    def change_sign(self):
        if self.answer_line.text():
            self.answer_line.setText(str(-1 * int(self.answer_line.text())))
    
    def remove(self):
        self.answer_line.setText('0')
        self.main_display.setText('')
    
    def action(self):
        action = self.sender()
        if self.answer_line.text():
            self.main_display.setText(self.main_display.text() + self.answer_line.text() + action.text())
            self.answer_line.setText('0')
    
    def calculate_answer(self):
        try:
            answer = eval(self.main_display.text() + self.answer_line.text())
        except:
            self.answer_line.setText("Mistake")
            return
        self.answer_line.setText(str(answer))
        self.main_display.setText('')
