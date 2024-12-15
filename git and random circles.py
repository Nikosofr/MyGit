import random
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6 import QtGui


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Git и случайные окружности")
        self.setGeometry(100, 100, 800, 600)
        self.circles = []
        self.pushButton = QPushButton("Нарисуй!", self)
        self.pushButton.clicked.connect(self.draw_circles)
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

    def draw_circles(self):
        self.circles.clear()
        for _ in range(10):
            diameter = random.randint(20, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            color = QtGui.QColor(random.randint(0, 255),
                                 random.randint(0, 255),
                                 random.randint(0, 255))
            self.circles.append((x, y, diameter, color))
        self.update()


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.central_widget = MainWindow()
        self.setCentralWidget(self.central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())
