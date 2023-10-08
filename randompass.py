import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализация пользовательского интерфейса
        self.initUI()

    def initUI(self):
        # Настройка окна приложения
        self.setWindowTitle('Генератор паролей')
        self.setGeometry(100, 100, 400, 200)

        # Создание виджетов: метка, поле ввода, кнопка и метки для типа пароля и кнопок переключения
        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit(self)
        self.password_input.setReadOnly(True)  # Поле ввода только для чтения

        self.generate_button = QPushButton('Сгенерировать пароль', self)
        self.generate_button.clicked.connect(self.generate_password)  # Привязка кнопки к методу generate_password

        self.type_label = QLabel('Тип пароля:')
        self.type_buttons = QHBoxLayout()
        self.letters_button = QPushButton('Только буквы')
        self.letters_button.clicked.connect(self.generate_password)  # Привязка кнопок к методу generate_password
        self.digits_button = QPushButton('Только цифры')
        self.digits_button.clicked.connect(self.generate_password)
        self.all_chars_button = QPushButton('Все символы')
        self.all_chars_button.clicked.connect(self.generate_password)

        self.type_buttons.addWidget(self.letters_button)
        self.type_buttons.addWidget(self.digits_button)
        self.type_buttons.addWidget(self.all_chars_button)

        # Организация интерфейса с использованием линий QVBoxLayout и QHBoxLayout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.type_label)
        self.layout.addLayout(self.type_buttons)

        self.setLayout(self.layout)  # Установка макета для виджета

    def generate_password(self):
        length = 12  # Длина пароля по умолчанию
        chars = string.ascii_letters + string.digits  # По умолчанию используются все буквы и цифры

        # Получение символов в зависимости от типа пароля, определенного пользователем
        sender = self.sender()
        if sender == self.letters_button:
            chars = string.ascii_letters
        elif sender == self.digits_button:
            chars = string.digits

        # Генерация случайного пароля и отображение его в поле ввода
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_input.setText(password)

def main():
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
