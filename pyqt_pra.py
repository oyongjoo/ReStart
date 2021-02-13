import sys
from PyQt5.QtWidgets import *

def clicked_slot():
    print('clicked')

# label = QLabel("hello, PyQt")
# label.show()

btn = QPushButton("Hello, PyQt")
btn.clicked.connect(clicked_slot)
btn.show()

app = QApplication(sys.argv)
print("before event loop")
app.exec_()
print("after event loop")