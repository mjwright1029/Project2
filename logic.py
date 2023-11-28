import csv
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.main())

    def get_info(self):
        villager_name = self.lineEdit.text()
        image = ''
        URL = ''
        species = ''
        gender = ''
        personality = ''
        hobby = ''
        birthday = ''
        with open('villagers.csv', 'r', newline='', encoding='utf-8') as csvfile:
            content = csv.reader(csvfile, delimiter=',')

            for row in content:
                if row and row[0] == villager_name:
                    image = f'images/{villager_name}.png'
                    species = row[4]
                    gender = row[5]
                    personality = row[6]
                    hobby = row[8]
                    birthday = row[9]
                    return row, image, species, gender, personality, hobby, birthday

    def display_image(self, image):
        pixmap = QPixmap(image)
        self.label.setPixmap(pixmap)

    def main(self):
        info, image, species, gender, personality, hobby, birthday = self.get_info()
        print(f'Species: {species}, Gender: {gender}, Personality: {personality}, Hobby: {hobby}, Birthday: {birthday}')
        self.display_image(image)
