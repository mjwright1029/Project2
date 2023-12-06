import csv
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class representing the logic for how the program will work
    """

    def __init__(self) -> None:
        """
        Method to set the default text and values of a logic object
        """
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

        self.name_menu.addItems(['Bea', 'Benjamin', 'Biskit', 'Bones', 'Butch', 'Cherry', 'Cookie', 'Daisy',
                                 'Goldie', 'Lucky', 'Mac', 'Maddie', 'Marcel', 'Portia', 'Shep', 'Walker'])
        self.name_menu.setCurrentIndex(-1)
        self.name_menu.currentTextChanged.connect(lambda: self.update_info())

    def get_info(self) -> tuple:
        """
        Method to gather the needed information based on the user's choice
        :return: character's image, name, species, gender, personality, hobby, and birthday
        """
        villager_name = self.name_menu.currentText()
        try:
            with open('villager.csv', 'r', newline='', encoding='utf-8') as csvfile:
                content = csv.reader(csvfile, delimiter=',')

                for row in content:
                    if row and row[0] == villager_name:
                        image = f'images/{villager_name}.png'

                        gender = row[5]
                        personality = row[6]
                        hobby = row[8]
                        birthday = row[9]
                        return villager_name, image, gender, personality, hobby, birthday

        except FileNotFoundError:
            villager_name = ''
            image = 'images/icon.png'
            gender = ''
            personality = ''
            hobby = ''
            birthday = ''
            return villager_name, image, gender, personality, hobby, birthday

    def display_image(self, image: str) -> None:
        """
        Method to display the correct image to the user
        :param image: the URL of the required image
        """
        pixmap = QPixmap(image)
        self.villager_image.setPixmap(pixmap)

    def display_info(self, name: str, gender: str, personality: str, hobby: str, birthday: str) -> None:
        """
        Method to display the information to the user by setting the labels
        :param name: the name of the character
        :param gender: the gender of the character
        :param personality: the personality type of the character
        :param hobby: the hobby of the character
        :param birthday: the birthday of the character
        """
        self.name_label.setText(f'Name: {name}')
        self.gender_label.setText(f'Gender: {gender}')
        self.personality_label.setText(f'Personality: {personality}')
        self.hobby_label.setText(f'Hobby: {hobby}')
        self.birthday_label.setText(f'Birthday: {birthday}')

    def update_info(self) -> None:
        """
        Method to update the image and text
        """
        name, image, gender, personality, hobby, birthday = self.get_info()
        self.display_image(image)
        self.display_info(name, gender, personality, hobby, birthday)
