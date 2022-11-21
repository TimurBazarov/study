import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint, choices
from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Yellow_Circles')
        self.pushButton.clicked.connect(self.draw_ellipse)

    def draw_ellipse(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for _ in range(randint(1, 4)):
            qp.setBrush(QColor(*choices(range(0, 255), k=3)))
            color = randint(5, 100)
            qp.drawEllipse(color + 150, color + 150, color, color)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
