import os
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QMimeData 

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        textCopyButton = QPushButton("&Copy Text")
        imageCopyButton= QPushButton("Co&py Image")
        htmlCopyButton = QPushButton("C&opy HTML")
        textPasteButton = QPushButton("Paste &Text")
        imagePasteButton = QPushButton("Paste &Image")
        htmlPasteButton = QPushButton("Paste &HTML")
        self.textLabel = QLabel("Original text")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "images/clock.png")))
        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(imageCopyButton, 0, 1)
        layout.addWidget(htmlCopyButton, 0, 2)
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(imagePasteButton, 1, 1)
        layout.addWidget(htmlPasteButton, 1, 2)
        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)
        self.setLayout(layout)
        textCopyButton.clicked.connect(self.copyText)
        imageCopyButton.clicked.connect(self.copyImage)
        htmlCopyButton.clicked.connect(self.copyHTML)
        textPasteButton.clicked.connect(self.PasteText)
        imagePasteButton.clicked.connect(self.PasteImage)
        htmlPasteButton.clicked.connect(self.PasteHTML)
        self.setWindowTitle("Clipboard例子")
    
    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("I've been clipped")
        
    def PasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())
        
    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "./images/python.png")))
        
    def PasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())
        
    def copyHTML(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)
        
    def PasteHTML(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Form()
    demo.show()
    sys.exit(app.exec_())
        
        
        

