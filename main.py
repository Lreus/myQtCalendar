import sys

from PyQt6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QWidget()
    label = QtWidgets.QLabel(widget)
    label.setText('hello world')
    widget.show()

    sys.exit(app.exec())