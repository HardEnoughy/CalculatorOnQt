from PySide6.QtWidgets import QApplication
from calculator import Calculator

from sys import argv

app = QApplication(argv)
window = Calculator()
window.show()
app.exec()
