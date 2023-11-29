import csv
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        font = QFont()
        font.setPointSize(16)

        self.villager_image.setFont(font)
        self.villager_image.setText('Learn more about the canine villagers of Animal Crossing: New Horizons!')

        self.name_label.setFont(font)
        self.name_label.setText('Name:')

        self.gender_label.setFont(font)
        self.gender_label.setText('Gender: ')

        self.personality_label.setFont(font)
        self.personality_label.setText('Personality: ')

        self.hobby_label.setFont(font)
        self.hobby_label.setText('Hobby: ')

        self.birthday_label.setFont(font)
        self.birthday_label.setText('Birthday: ')


        self.name_menue.addItems(['Bea', 'Benjamin', 'Biskit', 'Bones', 'Butch', 'Cherry', 'Cookie', 'Daisy',
                                  'Goldie', 'Lucky', 'Mac', 'Maddie', 'Marcel', 'Portia', 'Shep', 'Walker'])
        self.name_menue.currentTextChanged.connect(lambda: self.main())

    def get_info(self):
        villager_name = self.name_menue.currentText()
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
                    return villager_name, image, species, gender, personality, hobby, birthday

    def display_image(self, image):
        pixmap = QPixmap(image)
        self.villager_image.setPixmap(pixmap)

    def display_info(self, name, gender, personality, hobby, birthday):
        self.name_label.setText(f'Name: {name}')
        self.gender_label.setText(f'Gender: {gender}')
        self.personality_label.setText(f'Personality: {personality}')
        self.hobby_label.setText(f'Hobby: {hobby}')
        self.birthday_label.setText(f'Birthday: {birthday}')

    def main(self):
        name, image, species, gender, personality, hobby, birthday = self.get_info()
        self.display_image(image)
        self.display_info(name, gender, personality, hobby, birthday)
