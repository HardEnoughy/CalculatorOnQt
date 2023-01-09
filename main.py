from PySide6.QtWidgets import QApplication
from calculator import Calculator

app = QApplication()
window = Calculator()
window.show()
app.exec()
