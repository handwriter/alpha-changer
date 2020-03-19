from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
import sys
from PIL.ImageQt import ImageQt
from PIL import Image
from design import Ui_Form as Design
from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog
from copy import copy


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = Image.open(QFileDialog.getOpenFileName()[0])
        self.image = self.image.convert("RGBA")
        self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(1)

    def updater(self):
        self.label_2.setText(str(self.horizontalSlider.value()))
        img = copy(self.image)
        img.putalpha(255 - int(self.horizontalSlider.value()))
        self.label.setPixmap(QPixmap.fromImage(ImageQt(img)))


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())