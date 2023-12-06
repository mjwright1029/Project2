from logic import *


def main() -> None:
    """
    Method to initialize the GUI
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
