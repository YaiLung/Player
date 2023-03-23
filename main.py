import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Audio Player')
window.setWindowIcon(QIcon('icon.ico'))
window.setGeometry(100, 100, 400, 300)

player = QMediaPlayer()

playButton = QPushButton(window)
playButton.setGeometry(50, 50, 50, 50)
playButton.setIcon(QIcon('play.png'))
playButton.clicked.connect(player.play)


pauseButton = QPushButton(window)
pauseButton.setGeometry(100, 50, 50, 50)
pauseButton.setIcon(QIcon('pause.png'))
pauseButton.clicked.connect(player.pause)

label = QLabel(window)
label.setGeometry(150, 50, 200, 50)
label.setText('  No media playing')

def update_label(media):
    if media:
        label.setText('  Now playing: ' + media.canonicalUrl().fileName())
    else:
        label.setText('  No media playing')

player.mediaChanged.connect(update_label)

def open_file():
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Audio Files (*.mp3)")
    if file_dialog.exec_() == QDialog.Accepted:
        selected_file = file_dialog.selectedFiles()[0]
        player.setMedia(QMediaContent(QUrl.fromLocalFile(selected_file)))

openButton = QPushButton(window)
openButton.setGeometry(150, 150, 100, 50)
openButton.setText('Open File')
openButton.clicked.connect(open_file)

window.show()
sys.exit(app.exec_())