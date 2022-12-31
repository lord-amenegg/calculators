"""Simple Hello, World example with PyQt6."""

import sys
import urllib.request
import urllib
import pychromecast
import denonavr
import asyncio
import time
import datetime


from PyQt6.QtWidgets import (
    QStyle,
    QApplication,
    QDial,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QGridLayout,
    QVBoxLayout,
    QRadioButton,
    QProgressBar,
    QPushButton,
    QWidget
    )
import PyQt6.QtGui
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QDateTime, Qt, QTimer, QSize
from PyQt6.QtWidgets import QStyleFactory, QStyle

class StatusMediaListener:
    def __init__(self, name, cast):
        self.name = name
        self.cast = cast

    
    def new_media_status(self, status):
        print("[", time.ctime(), " - ", self.name, "] status media change:")
        print("\nCurrent Title:", status.title)
        window.update_player()
        
        if status.current_time == status.duration:
            window.update_player()
            #self.cast.set_volume_muted(True)
            #print("Cast device is muted")
        else:
            pass

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Susan's Player")
        self.dialogLayout = QVBoxLayout()
        self.LabelsLayout = QVBoxLayout()
        self.infoLayout = QHBoxLayout()
        self.info2Layout = QHBoxLayout()
        self.rejillaLayout = QGridLayout()
        self.setLayout(self.dialogLayout)
        
        


        self.connect_to_stereo()
        #listenerMedia = StatusMediaListener(self.cast.name, self.cast)
        #self.mc.register_status_listener(listenerMedia)
        self.UiComponents()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_player)
        self.timer.start(5000)

    def connect_to_stereo(self):
        self.chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["El Altavoz de Susan"])
        print(pychromecast.get_listed_chromecasts())
        self.cast = self.chromecasts[0]
        self.cast.wait()
        print(self.cast.name)        
        self.mc = self.cast.media_controller
        self.mc.block_until_active()
        self.d = denonavr.DenonAVR("192.168.86.151")
        self.d.setup()
        self.d.update()
        print(self.d.state)
        self.d.power_on()

        self.musi_dict = {}
        self.artist , self.name_song = self.mc.status.artist, self.mc.status.title
        self.quality = self.mc.status.media_custom_data['playingQuality']
        self.musi_dict.update({'artista': self.artist, 'titulo': self.name_song, 'calidad': self.quality})
        pixmapi = QStyle.StandardPixmap.SP_MediaVolumeMuted
        icon_mute = self.style().standardIcon(pixmapi)
        pixmapi = QStyle.StandardPixmap.SP_MediaSkipBackward
        icon_skip_b = self.style().standardIcon(pixmapi)
        pixmapi = QStyle.StandardPixmap.SP_MediaSkipForward
        icon_skip_f = self.style().standardIcon(pixmapi)
        pixmapi = QStyle.StandardPixmap.SP_BrowserReload
        icon_update = self.style().standardIcon(pixmapi)
        icon_play_pause = 'p_p.png'


        self.player_keys = {'Previous': [self.mc.rewind, icon_skip_b], 'Play/Pause':  [self.play_pause, icon_play_pause],'Next': [self.mc.skip, icon_skip_f], 'Mute': [self.mute, icon_mute], 'On/OFF': [self.on_off, 'on_off.png'], 'Update': [self.update_player, icon_update]}
        
       
        
    def mute(self):
        
        print(self.cast.status)
        pregunta = self.cast.status.volume_muted
        if pregunta is False:
            self.cast.set_volume_muted(True)
            print('merde')
        else:
            print('cojones')
            self.cast.set_volume_muted(False)

    def play_pause(self):
        pregunta = self.mc.is_playing
        print(type(pregunta))

        if pregunta is True:
            print('polla')
            self.mc.pause()
        else:
            self.mc.play()
            print('puto')

    def on_off(self):
        if self.d.state == 'off':
            self.d.power_on()
        if self.d.power == 'ON':
            self.d.power_off()

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setGeometry(200, 10, 250, 10)
        self.progressBar.setRange(0, int(self.mc.status.duration))
        self.progressBar.setValue(int(self.mc.status.current_time))
        self.progressBar.setTextVisible(False)
        bar_timer = QTimer(self)
        bar_timer.timeout.connect(self.advanceProgressBar)
        bar_timer.start(500)
    

    def advanceProgressBar(self):
        momento = datetime.timedelta(seconds = int(self.mc.status.current_time))
        self.remaining_time_label.setText(str(momento))
        
        if self.mc.status.current_time == self.mc.status.duration:
           

            print('bar full')
            self.advanceProgressBar()
        else:
            self.mc.update_status()
            self.progressBar.setValue(int(self.mc.status.current_time))

    
    def update_player(self):
        self.mc.update_status()
        
        self.artist, self.name_song = self.mc.status.artist, self.mc.status.title
        duracion = datetime.timedelta(seconds = int(self.mc.status.duration))
        momento = datetime.timedelta(seconds = int(self.mc.status.current_time))
        self.remaining_time_label.setText(str(momento))
        self.total_time_label.setText(str(duracion))
        try:
            self.quality = self.mc.status.media_custom_data['playingQuality']
            if self.musi_dict['titulo'] != self.name_song:
                self.musi_dict.update({'artista': self.artist, 'titulo': self.name_song, 'calidad': self.quality})

                print(self.musi_dict.items())
                url = (self.mc.status.images[0][0])
                data = urllib.request.urlopen(url).read()
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                smaller_pixmap = pixmap.scaled(450, 450)
                self.portada.setPixmap(smaller_pixmap)
                self.LabelTitle.setText('Title: ' + self.name_song)
                self.LabelArtist.setText('Artist: ' + self.artist)
                self.QualityLabel.setText('Quality : ' + self.quality)
                self.adjustSize()
                print('I am updated')
            else:
                pass
        except KeyError:
            ErrorTimer = QTimer(self)
            ErrorTimer.timeout.connect(self.update_player)
            ErrorTimer.start(5000)
            


    def UiComponents(self):
        self.portada = QLabel()
        self.pixmap = QPixmap()
        dial = QDial()
        dial.setValue(30)
        dial.setNotchesVisible(True)
        dial.valueChanged.connect(lambda: self.cast.set_volume(dial.value()/100))
        self.LabelTitle = QLabel('Title: ' + self.name_song)
        self.LabelTitle.setWordWrap(True)
        self.LabelArtist = QLabel('Artist: ' + self.artist)
        self.LabelArtist.setWordWrap(True)
        self.QualityLabel = QLabel('Quality : ' + self.quality)
        self.LabelsLayout.addWidget(self.LabelTitle)
        self.LabelsLayout.addWidget(self.LabelArtist)
        self.LabelsLayout.addWidget(self.QualityLabel)
        self.infoLayout.addLayout(self.LabelsLayout)
        self.infoLayout.addWidget(dial)
        self.dialogLayout.addWidget(self.portada)
        self.dialogLayout.addLayout(self.infoLayout) 
        self.createProgressBar()
        self.dialogLayout.addWidget(self.progressBar)
        self.remaining_time_label = QLabel('cuanto')
        self.total_time_label = QLabel('mucho')
        self.total_time_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.info2Layout.addWidget(self.remaining_time_label)
        self.info2Layout.addWidget(self.total_time_label)
        self.dialogLayout.addLayout(self.info2Layout)

        for i, (k,v) in enumerate(self.player_keys.items()):
            player_button = QPushButton(k)
            player_button.setIcon(QIcon(v[1]))
            player_button.clicked.connect(v[0])
            player_button.setIconSize(QSize(30, 30))
            if i < 3:
                self.rejillaLayout.addWidget(player_button, 0, i)
            else:
                self.rejillaLayout.addWidget(player_button, 1, i-3)
        self.dialogLayout.addLayout(self.rejillaLayout)
        
        
        print(self.mc.status.images)
        url = (self.mc.status.images[0][0])
        data = urllib.request.urlopen(url).read()
        self.pixmap.loadFromData(data)
        smaller_pixmap = self.pixmap.scaled(450, 450)
        self.portada.setPixmap(smaller_pixmap)
        self.portada.show()
        

       


        

            


        
        


        


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet("""
    QWidget {
    background-color: "dark gray";
    color: "white";
    font-size: 20px;
    }
     QProgressBar
    {
    min-height: 5px;
    max-height: 5px;
    border: solid grey;
    border-radius: 6px;
    color: 'black';
    }
    QProgressBar::chunk 
    {
    background-color: 'sienna';
    border-radius :3px;
    }
    QLabel {
        color: 'black';
    }
    QPushButton {
        background-color: "dim gray";
        color: 'black';
    }
    """)
    window = Window()
    window.show()
    sys.exit(app.exec())