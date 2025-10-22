# test_pyqt.py
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Test PyQt")
w.resize(400, 300)
label = QLabel("Si ves esto, PyQt funciona!", w)
label.move(50, 50)
w.show()
sys.exit(app.exec_())
