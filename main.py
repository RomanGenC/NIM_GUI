from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setStyleSheet(
            "QMainWindow{background-image: url(C:/Nim.jpg);}"
        )
        self.centralwidget.setStyleSheet(
            "background-image: none;"  # Стиль фона для centralwidget
        )
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 300, 50))
        self.label.setStyleSheet("background-color: rgb(194, 255, 203);\n"
"font: 9pt \"Segoe UI\";\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(106, 103, 102);background-color: rgb(167, 255, 165);")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(100, 200, 100, 40))
        self.pushButton_reset.setStyleSheet("background-color: rgb(50, 50, 50);"
                                          "color: white;"
                                          "font: 700 9pt \"Segoe UI\";")
        self.pushButton_reset.setObjectName("Reset")
        self.pushButton_reset.clicked.connect(self.reset_buttons)

        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(100, 250, 100, 40))
        self.confirm_button.setStyleSheet("background-color: rgb(50, 50, 50);"
                                          "color: white;"
                                          "font: 700 9pt \"Segoe UI\";")
        self.confirm_button.setObjectName("ConfirmButton")
        self.confirm_button.setText("Confirm")
        self.confirm_button.clicked.connect(self.confirm_move)

        self.buttons_to_change = []

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 600, 100, 40))
        self.pushButton.setStyleSheet("background-color: rgb(194, 255, 203);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(106, 103, 102);background-color: rgb(194, 255, 203);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 550, 100, 40))
        self.pushButton_2.setStyleSheet("background-color: rgb(194, 255, 203);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(106, 103, 102);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 500, 100, 40))
        self.pushButton_3.setStyleSheet("background-color: rgb(194, 255, 203);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(106, 103, 102);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 400, 100, 40))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 64, 74);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(350, 600, 100, 40))
        self.pushButton_14.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"color: rgb(238, 255, 249);\n"
"background-color: rgb(93, 96, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(350, 550, 100, 40))
        self.pushButton_15.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"color: rgb(238, 255, 249);\n"
"background-color: rgb(93, 96, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(350, 500, 100, 40))
        self.pushButton_16.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"color: rgb(238, 255, 249);\n"
"background-color: rgb(93, 96, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(350, 450, 100, 40))
        self.pushButton_17.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
"color: rgb(238, 255, 249);\n"
"background-color: rgb(93, 96, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 450, 100, 40))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 64, 74);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 500, 100, 40))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 64, 74);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(550, 550, 100, 40))
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 64, 74);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(550, 600, 100, 40))
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 64, 74);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.action_button()

        # Сохраняем исходные тексты кнопок и их стили
        self.button_texts = {
            self.pushButton: self.pushButton.text(),
            self.pushButton_2: self.pushButton_2.text(),
            self.pushButton_3: self.pushButton_3.text(),
            self.pushButton_7: self.pushButton_7.text(),
            self.pushButton_8: self.pushButton_8.text(),
            self.pushButton_9: self.pushButton_9.text(),
            self.pushButton_10: self.pushButton_10.text(),
            self.pushButton_11: self.pushButton_11.text(),
            self.pushButton_14: self.pushButton_14.text(),
            self.pushButton_15: self.pushButton_15.text(),
            self.pushButton_16: self.pushButton_16.text(),
            self.pushButton_17: self.pushButton_17.text(),
        }

        self.button_styles = {
            self.pushButton: self.pushButton.styleSheet(),
            self.pushButton_2: self.pushButton_2.styleSheet(),
            self.pushButton_3: self.pushButton_3.styleSheet(),
            self.pushButton_7: self.pushButton_7.styleSheet(),
            self.pushButton_8: self.pushButton_8.styleSheet(),
            self.pushButton_9: self.pushButton_9.styleSheet(),
            self.pushButton_10: self.pushButton_10.styleSheet(),
            self.pushButton_11: self.pushButton_11.styleSheet(),
            self.pushButton_14: self.pushButton_14.styleSheet(),
            self.pushButton_15: self.pushButton_15.styleSheet(),
            self.pushButton_16: self.pushButton_16.styleSheet(),
            self.pushButton_17: self.pushButton_17.styleSheet(),
        }

        self.button_states = {
            self.pushButton: False,
            self.pushButton_2: False,
            self.pushButton_3: False,
            self.pushButton_7: False,
            self.pushButton_8: False,
            self.pushButton_9: False,
            self.pushButton_10: False,
            self.pushButton_11: False,
            self.pushButton_14: False,
            self.pushButton_15: False,
            self.pushButton_16: False,
            self.pushButton_17: False
        }
        for i in self.button_states.keys():
            self.all_button.append(i)

    def action_button(self):
        self.pushButton.clicked.connect(lambda: self.button_used(self.pushButton, self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.button_used(self.pushButton_2, self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.button_used(self.pushButton_3, self.pushButton_3.text()))
        self.pushButton_7.clicked.connect(lambda: self.button_used(self.pushButton_7, self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.button_used(self.pushButton_8, self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.button_used(self.pushButton_9, self.pushButton_9.text()))
        self.pushButton_10.clicked.connect(lambda: self.button_used(self.pushButton_10, self.pushButton_10.text()))
        self.pushButton_11.clicked.connect(lambda: self.button_used(self.pushButton_11, self.pushButton_11.text()))
        self.pushButton_14.clicked.connect(lambda: self.button_used(self.pushButton_14, self.pushButton_14.text()))
        self.pushButton_15.clicked.connect(lambda: self.button_used(self.pushButton_15, self.pushButton_15.text()))
        self.pushButton_16.clicked.connect(lambda: self.button_used(self.pushButton_16, self.pushButton_16.text()))
        self.pushButton_17.clicked.connect(lambda: self.button_used(self.pushButton_17, self.pushButton_17.text()))

    def button_used(self, button, number):
        if button.text() != "Used":
            button.setText("Used")
            self.button_states[button] = True
            self.buttons_to_change.append(button)
        else:
            error = QMessageBox()
            error.setWindowTitle("Этот камень уже взяли")
            error.setText("Возьмите другой камень")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset|QMessageBox.Ok|QMessageBox.Cancel)
            error.buttonClicked.connect(self.pop_action)

            error.exec_()
    used = []
    all_button = []

    def confirm_move(self):
        # Метод для подтверждения хода пользователя
        if self.buttons_to_change:
            # Изменяем цвета кнопок из списка
            for button in self.buttons_to_change:
                button.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
                                     "color: rgb(238, 255, 249);\n"
                                     "background-color: rgb(100, 100, 100);")
            self.used += self.buttons_to_change
            print(self.used)
            print(self.pushButton)
            self.buttons_to_change = []  # Очищаем список после изменения цветов
            if len(self.used) < 12:
                self.take_computer()
            elif len(self.used) == 12:
                self.used = []
                end = QMessageBox()
                end.setWindowTitle("Игра завершена")
                end.setText("Поздравляю, вы победили!")
                end.setIcon(QMessageBox.Warning)
                end.setStandardButtons(QMessageBox.Ok)
                end.buttonClicked.connect(self.pop_action)

                end.exec_()

    def pop_action(self, btn):
        if btn.text() == "Ok":
            print("Clicked Ok now")
        elif btn.text() == "Reset":
            print('Reset')
            self.reset_buttons()

    def reset_buttons(self):
        # Восстановление исходных текстов кнопок и их стилей
        for button, text in self.button_texts.items():
            button.setText(text)
            button.setStyleSheet(self.button_styles[button])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра НИМ"))
        self.label.setText(_translate("MainWindow", "Игра НИМ"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_14.setText(_translate("MainWindow", "1"))
        self.pushButton_15.setText(_translate("MainWindow", "2"))
        self.pushButton_16.setText(_translate("MainWindow", "3"))
        self.pushButton_17.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "4"))
        self.pushButton_9.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "2"))
        self.pushButton_11.setText(_translate("MainWindow", "1"))

    def take_computer(self):
        flug = 0
        for i in self.all_button:
            if (flug == 0) and (i not in self.used):
                i.setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
                                     "color: rgb(238, 255, 249);\n"
                                     "background-color: rgb(100, 100, 100);")
                self.used.append(i)
                if len(self.used) == 12:
                    self.used = []

                    win = QMessageBox()
                    win.setWindowTitle("Игра завершена")
                    win.setText("Увы, но на этот раз компьютер оказался сильнее!")
                    win.setIcon(QMessageBox.Warning)
                    win.setStandardButtons(QMessageBox.Ok)
                    win.buttonClicked.connect(self.pop_action)

                    win.exec_()
                flug = 1

    def best_move(self):
        button_mapping = {
            0: self.pushButton,
            1: self.pushButton_2,
            2: self.pushButton_3,
            3: self.pushButton_7,
            4: self.pushButton_8,
            5: self.pushButton_9,
            6: self.pushButton_10,
            7: self.pushButton_11,
            8: self.pushButton_14,
            9: self.pushButton_15,
            10: self.pushButton_16,
            11: self.pushButton_17,
        }
        global stacks
        for i in range(self.nums):
            if stacks[i] != 0:
                for j in range(1, stacks[i] + 1):
                    temp_stacks = stacks.copy()
                    temp_stacks[i] = temp_stacks[i] - j
                    xor = temp_stacks[0] ^ temp_stacks[1]
                    for k in range(2, self.nums):
                        xor = xor ^ temp_stacks[k]
                    if xor == 0:
                        print('Лучший ход: забрать ' + str(j) + ' камней из ' + str(i) + ' кучки где ' + str(stacks[i]))
                        stacks[i] = stacks[i] - j
                        button_to_click = button_mapping[i]  # Получаем кнопку для нажатия
                        button_to_click.click()
                    return ()
        self.take_computer()
        return ()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())