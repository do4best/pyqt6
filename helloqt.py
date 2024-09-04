from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QMainWindow,QPushButton,QHBoxLayout,QLineEdit,QVBoxLayout
from PyQt6.QtCore import Qt,QSize
import sys

class GuiMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")
        self.nice = QLabel("Hello Again")
        self.button = QPushButton("Press It")
        self.button.setCheckable(True)
        layout = QHBoxLayout()
        self.button.clicked.connect(self.clicked_me)
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        layout.addWidget(container)
        self.setLayout(layout)

        self.show()

    def clicked_me(self):
        print("Clicked")




if __name__ == "__main__":
    app = QApplication([])
    window = GuiMain()
    app.exec()