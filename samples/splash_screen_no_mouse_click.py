from PyQt6 import QtCore, QtGui, QtWidgets
import time
import sys


class SplashScreen(QtWidgets.QSplashScreen):
    def mousePressEvent(self, event):
        return


class MyWindow(QtWidgets.QPushButton):  # Создаем класс и простую кнопку
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText('Close...')  # Создаем текст на кнопке
        self.clicked.connect(QtWidgets.QApplication.quit)  # Привязываем событие к кнопке

    def load_data(self, sp):
        for i in range(1, 11):  # Имитация прогресса
            time.sleep(1)  # Что-то загружаем
            sp.showMessage(f'Loading... {i}%',
                           QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignBottom,
                           QtCore.Qt.GlobalColor.black)
            QtWidgets.QApplication.processEvents()  # Запускаем оборот цикла


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    splash = SplashScreen(QtGui.QPixmap('lotus pose_600.png'))  # Загружаем изображение
    splash.showMessage(f'Loading... 0%',
                       QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignBottom,
                       QtCore.Qt.GlobalColor.black)
    splash.show()  # Отображаем заставку
    QtWidgets.QApplication.processEvents()
    window = MyWindow()  # Создаем экземпляр окна
    window.setWindowTitle('Заставка')
    window.resize(300, 30)
    window.load_data(splash)  # загружаем данные
    window.show()
    splash.finish(window)
    sys.exit(app.exec())
