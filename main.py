# импортируем модули
import os
import subprocess
import sys
import webbrowser
import shlex
from PyQt5.QtCore import Qt, QSize,QTimer
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
folder = os.path.abspath(os.curdir)

# создаем окна
app = QApplication([])
QApplication.processEvents()
screen = QApplication.primaryScreen()
size=screen.size()
w=size.width()
h=size.height()
main_win = QWidget()
main_win.setWindowTitle('ADB Fast Tool')
main_win.setWindowIcon(QIcon(os.path.join(folder, 'resources', 'ICON.png')))
main_win.setStyleSheet("background-color: lightblue;")
main_win.show()
res_win=QWidget()
ter_win=QWidget()
ter_win.setWindowTitle('Терминал')
ter_win.setMinimumSize(w/5,h/8)
ter_win.setStyleSheet("background-color: lightblue;")

# Списки
easy_base=[]
custom_script=[]
gaps=[]
samsung_services=[]
miui_services_medium=[]
miui_services_easy=[]
miui_services_all=[]
google_services=[]
custom_script=[]
with open(os.path.join(folder, 'resources', 'easy_base.txt')) as file:
    for line in file:
        easy_base.append(line.strip())
with open(os.path.join(folder, 'resources', 'gaps.txt')) as file:
    for line in file:
        gaps.append(line.strip())
with open(os.path.join(folder, 'resources', 'samsung_services.txt')) as file:
    for line in file:
        samsung_services.append(line.strip())
with open(os.path.join(folder, 'resources', 'miui_services_medium.txt')) as file:
    for line in file:
        miui_services_medium.append(line.strip())
with open(os.path.join(folder, 'resources', 'google_services.txt')) as file:
    for line in file:
        google_services.append(line.strip())
with open(os.path.join(folder, 'resources', 'miui_services_easy.txt')) as file:
    for line in file:
        miui_services_easy.append(line.strip())
with open(os.path.join(folder, 'resources', 'miui_services_all.txt')) as file:
    for line in file:
        miui_services_all.append(line.strip())

# Объекты
youtube_push=QPushButton('YouTube Канал')
youtube_push.setFixedSize(w/15,h/40)
youtube_push.setIcon(QIcon(os.path.join(folder,'resources','YouTube.png')))
youtube_push.setIconSize(QSize(w/30,h/50))
youtube_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

telegram_push=QPushButton('Telegram Канал')
telegram_push.setFixedSize(w/15,h/40)
telegram_push.setIcon(QIcon(os.path.join(folder,'resources','telegram.png')))
telegram_push.setIconSize(QSize(w/30,h/50))
telegram_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

github_push=QPushButton('GitHub создателя')
github_push.setFixedSize(w/15,h/40)
github_push.setIcon(QIcon(os.path.join(folder,'resources','github.png')))
github_push.setIconSize(QSize(w/30,h/50))
github_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

terminal_push = QPushButton('Терминал')
terminal_push.setFixedSize(w/15,h/40)
terminal_push.setIcon(QIcon(os.path.join(folder, 'resources', 'командная строка.png')))
terminal_push.setIconSize(QSize(w/30,h/40))
terminal_push.setStyleSheet("font-size: 16px;")

logo=QLabel(main_win)
LOGO=QPixmap(os.path.join(folder, 'resources', 'LOGO.png'))
scaled_LOGO=LOGO.scaled(w/8.4,h/4.5)
logo.setPixmap(scaled_LOGO)

devices = QPushButton('Устройства')
devices.setFixedSize(w/2.05,h/20)
devices.setIcon(QIcon(os.path.join(folder, 'resources', 'usb.webp')))
devices.setIconSize(QSize(w/8.3,h/20))
devices.setStyleSheet("background-color: lightblue; font-size: 16px;")

reboot_push=QPushButton('Reboot')
reboot_push.setFixedSize(w/4.12,h/25)
reboot_push.setIcon(QIcon(os.path.join(folder, 'resources', 'reboot.png')))
reboot_push.setIconSize(QSize(w/15,h/30))
reboot_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

poweroff_push=QPushButton('Poweroff')
poweroff_push.setFixedSize(w/4.12,h/25)
poweroff_push.setIcon(QIcon(os.path.join(folder, 'resources', 'poweroff.png')))
poweroff_push.setIconSize(QSize(w/15,h/30))
poweroff_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

reboot_recovery_push=QPushButton('Recovery')
reboot_recovery_push.setFixedSize(w/4.12,h/25)
reboot_recovery_push.setIcon(QIcon(os.path.join(folder, 'resources', 'twrp.png')))
reboot_recovery_push.setIconSize(QSize(w/15,h/30))
reboot_recovery_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

reboot_fastboot_push=QPushButton('Fastboot')
reboot_fastboot_push.setFixedSize(w/4.12,h/25)
reboot_fastboot_push.setIcon(QIcon(os.path.join(folder, 'resources', 'fastboot.png')))
reboot_fastboot_push.setIconSize(QSize(w/15,h/30))
reboot_fastboot_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

reboot_bootloader_push=QPushButton('Загрузчик')
reboot_bootloader_push.setFixedSize(w/4.12,h/25)
reboot_bootloader_push.setIcon(QIcon(os.path.join(folder, 'resources', 'загрузчик.png')))
reboot_bootloader_push.setIconSize(QSize(w/15,h/30))
reboot_bootloader_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

reboot_edl_push=QPushButton('Перейти в EDL')
reboot_edl_push.setFixedSize(w/4.12,h/25)
reboot_edl_push.setIcon(QIcon(os.path.join(folder, 'resources', 'poweroff.png')))
reboot_edl_push.setIconSize(QSize(w/15,h/30))
reboot_edl_push.setStyleSheet("background-color: lightblue; font-size: 16px;")

easy_base_push = QPushButton('Общее удаление хлама')
easy_base_push.setFixedSize(w/8.3,h/25)
easy_base_push.setIcon(QIcon(os.path.join(folder, 'resources', 'корзина.png')))
easy_base_push.setIconSize(QSize(w/15,h/30))
easy_base_push.setStyleSheet("background-color: white; font-size: 16px;")

gaps_all_delete_push = QPushButton('Удаление Gapps')
gaps_all_delete_push.setFixedSize(w/8.3,h/25)
gaps_all_delete_push.setIcon(QIcon(os.path.join(folder, 'resources', 'google.webp')))
gaps_all_delete_push.setIconSize(QSize(w/15,h/30))
gaps_all_delete_push.setStyleSheet("background-color: yellow; font-size: 16px;")

samsung_services_push=QPushButton('Удалить Samsung Сервисы')
samsung_services_push.setFixedSize(w/8.3,h/25)
samsung_services_push.setIcon(QIcon(os.path.join(folder, 'resources', 'samsung.png')))
samsung_services_push.setIconSize(QSize(w/30,h/30))
samsung_services_push.setStyleSheet("background-color: blue; font-size: 16px;")

google_services_push=QPushButton('Удалить Google Сервисы')
google_services_push.setFixedSize(w/8.3,h/25)
google_services_push.setIcon(QIcon(os.path.join(folder, 'resources', 'google_services_remove.png')))
google_services_push.setIconSize(QSize(w/15,h/30))
google_services_push.setStyleSheet("background-color: red; font-size: 16px;")

custom_script_push=QPushButton('Выбрать свой скрипт')
custom_script_push.setFixedSize(w/8.3,h/25)
custom_script_push.setIcon(QIcon(os.path.join(folder, 'resources', 'script.webp')))
custom_script_push.setIconSize(QSize(w/15,h/30))
custom_script_push.setStyleSheet("background-color: white; font-size: 16px;")

miui_services_easy_push=QPushButton('Легкое удаление MI Сервисов')
miui_services_easy_push.setFixedSize(w/8.3,h/25)
miui_services_easy_push.setIcon(QIcon(os.path.join(folder, 'resources', 'MI.png')))
miui_services_easy_push.setIconSize(QSize(w/15,h/30))
miui_services_easy_push.setStyleSheet("background-color: yellow; font-size: 16px;")

miui_services_medium_push=QPushButton('Удаление MI Сервисов')
miui_services_medium_push.setFixedSize(w/8.3,h/25)
miui_services_medium_push.setIcon(QIcon(os.path.join(folder, 'resources', 'MI.png')))
miui_services_medium_push.setIconSize(QSize(w/15,h/30))
miui_services_medium_push.setStyleSheet("background-color: orange; font-size: 16px;")

miui_services_all_push=QPushButton('ПОЛНОЕ удаление MI Сервисов')
miui_services_all_push.setFixedSize(w/8.3,h/25)
miui_services_all_push.setIcon(QIcon(os.path.join(folder, 'resources', 'MI.png')))
miui_services_all_push.setIconSize(QSize(w/15,h/30))
miui_services_all_push.setStyleSheet("background-color: red; font-size: 16px;")

progress_bar = QProgressBar()
progress_bar.setMinimum(1)
progress_bar.setMaximum(len(google_services))
terminal_text=QLabel('Меню для ручного ввода команд')
terminal_text.setStyleSheet("font-size: 20px;")
terminal_line_edit = QLineEdit()
terminal_line_edit.setPlaceholderText('Например ./adb devices')
# Каркас графического интерфейса
line = QVBoxLayout()
main_win.setLayout(line)
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line7 = QHBoxLayout()
line8 = QHBoxLayout()
line9 = QHBoxLayout()
line2v = QVBoxLayout()

line.addLayout(line1)
line.addLayout(line2)
line.addLayout(line3)
line.addLayout(line4)
line.addLayout(line5)
line.addLayout(line6)
line.addLayout(line7)
line.addLayout(line8)
line.addLayout(line9)
line1.addWidget(youtube_push,alignment=Qt.AlignRight)
line1.addWidget(terminal_push)
line1.addWidget(telegram_push)
line1.addWidget(github_push)
line2.addWidget(logo)
line2.addLayout(line2v)
line3.addWidget(devices,alignment=Qt.AlignLeft)
line4.addWidget(reboot_push)
line4.addWidget(poweroff_push,alignment=Qt.AlignLeft)
line5.addWidget(reboot_recovery_push)
line5.addWidget(reboot_fastboot_push,alignment=Qt.AlignLeft)
line6.addWidget(reboot_bootloader_push)
line6.addWidget(reboot_edl_push,alignment=Qt.AlignLeft)
line7.addWidget(easy_base_push)
line7.addWidget(gaps_all_delete_push)
line7.addWidget(samsung_services_push)
line7.addWidget(google_services_push,alignment=Qt.AlignLeft)
line8.addWidget(custom_script_push)
line8.addWidget(miui_services_easy_push)
line8.addWidget(miui_services_medium_push)
line8.addWidget(miui_services_all_push,alignment=Qt.AlignLeft)

line_ter=QVBoxLayout()
ter_win.setLayout(line_ter)
line_ter.addWidget(terminal_text)
line_ter.addWidget(terminal_line_edit)
line_res=QVBoxLayout()
res_win.setLayout(line_res)

# Функции
def youtube_function():
    webbrowser.open('https://www.youtube.com/@DINOR-h5u/featured')
def telegram_function():
    webbrowser.open('https://t.me/DINOR_YouTube')
def github_function():
    webbrowser.open('https://github.com/juuecwpgc')
def terminal_dialog_function():
    ter_win.show()
    command = terminal_line_edit.text().strip()  # Убираем лишние пробелы
    if not command:
        print("No command entered.")
        return  # Выход из функции, если команда пустая
    try:
        result = subprocess.run(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            output_text = f"BASH: {result.stdout.strip()}"
        else:
            output_text = f"BASH: ERROR: {result.returncode}\n{result.stderr.strip()}"
        
        console_text = QLabel(output_text)
        line_ter.addWidget(console_text)
        line_ter.update()  # Обновите интерфейс (если необходимо)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        console_text = QLabel(error_message)
        line_ter.addWidget(console_text)
        line_ter.update()
def devices_function():
    command1 = "./adb devices"
    result = os.popen(command1).readline()
    result = ''.join(result)
    console_text=QLabel(result)
    line2v.addWidget(console_text)
def easy_base_function():
    procent = 0
    for package in easy_base:
        package = package.strip()
        command2 = ['./adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package]
        result = subprocess.run(command2, capture_output=True, text=True)
        if result.returncode == 0:
            output_text = f"Успешно удален пакет: {package}"
            procent += 1
            progress_bar.setValue(procent)
            QApplication.processEvents()
        else:
            output_text = f"Ошибка при удалении пакета {package}: {result.stderr}"
        with open(os.path.join(folder, '.history.txt'), 'a') as file:
            file.write(output_text)
        procent += 1
        progress_bar.setValue(procent)
        line9.addWidget(progress_bar)
        QApplication.processEvents()
    if 'adb: no devices/emulators found' in output_text:
        res=QLabel('Устройство не подключено')
    elif 'Успешно удален пакет' in output_text:
        res=QLabel('Пакеты были успешно удалены')
    else:
        res=QLabel('Пакеты не установлены или их удаление невозможно')
    line_res.addWidget(res)
    res_win.show()
def google_services_function():
    procent = 0
    for package in google_services:
        package = package.strip()
        command2 = ['./adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package]
        result = subprocess.run(command2, capture_output=True, text=True)
        if result.returncode == 0:
            output_text = f"Успешно удален пакет: {package}"
            procent += 1
            progress_bar.setValue(procent)
            QApplication.processEvents()
        else:
            output_text = f"Ошибка при удалении пакета {package}: {result.stderr}"
        with open(os.path.join(folder, '.history.txt'), 'a') as file:
            file.write(output_text)
        procent += 1
        progress_bar.setValue(procent)
        line9.addWidget(progress_bar)
        QApplication.processEvents()
    if 'adb: no devices/emulators found' in output_text:
        res=QLabel('Устройство не подключено')
    elif 'Успешно удален пакет' in output_text:
        res=QLabel('Пакеты были успешно удалены')
    else:
        res=QLabel('Пакеты не установлены или их удаление невозможно')
    line_res.addWidget(res)
    res_win.show()
def gaps_function():
    procent = 0
    for package in gaps:
        package = package.strip()
        command2 = ['./adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package]
        result = subprocess.run(command2, capture_output=True, text=True)
        if result.returncode == 0:
            output_text = f"Успешно удален пакет: {package}"
            procent += 1
            progress_bar.setValue(procent)
            QApplication.processEvents()
        else:
            output_text = f"Ошибка при удалении пакета {package}: {result.stderr}"
        with open(os.path.join(folder, '.history.txt'), 'a') as file:
            file.write(output_text)
        procent += 1
        progress_bar.setValue(procent)
        line9.addWidget(progress_bar)
        QApplication.processEvents()
    if 'adb: no devices/emulators found' in output_text:
        res=QLabel('Устройство не подключено')
    elif 'Успешно удален пакет' in output_text:
        res=QLabel('Пакеты были успешно удалены')
    else:
        res=QLabel('Пакеты не установлены или их удаление невозможно')
    line_res.addWidget(res)
    res_win.show()
def samsung_services_function():
    procent = 0
    for package in samsung_services:
        package = package.strip()
        command2 = ['./adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package]
        result = subprocess.run(command2, capture_output=True, text=True)
        if result.returncode == 0:
            output_text = f"Успешно удален пакет: {package}"
            procent += 1
            progress_bar.setValue(procent)
            QApplication.processEvents()
        else:
            output_text = f"Ошибка при удалении пакета {package}: {result.stderr}"
        with open(os.path.join(folder, '.history.txt'), 'a') as file:
            file.write(output_text)
        procent += 1
        progress_bar.setValue(procent)
        line9.addWidget(progress_bar)
        QApplication.processEvents()
    if 'adb: no devices/emulators found' in output_text:
        res=QLabel('Устройство не подключено')
    elif 'Успешно удален пакет' in output_text:
        res=QLabel('Пакеты были успешно удалены')
    else:
        res=QLabel('Пакеты не установлены или их удаление невозможно')
    line_res.addWidget(res)
    res_win.show()
def miui_services_medium_function():
    procent = 0
    for package in miui_services_medium:
        package = package.strip()
        command2 = ['./adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package]
        result = subprocess.run(command2, capture_output=True, text=True)
        if result.returncode == 0:
            output_text = f"Успешно удален пакет: {package}"
            procent += 1
            progress_bar.setValue(procent)
            QApplication.processEvents()
        else:
            output_text = f"Ошибка при удалении пакета {package}: {result.stderr}"
        with open(os.path.join(folder, '.history.txt'), 'a') as file:
            file.write(output_text)
        procent += 1
        progress_bar.setValue(procent)
        line9.addWidget(progress_bar)
        QApplication.processEvents()
    if 'adb: no devices/emulators found' in output_text:
        res=QLabel('Устройство не подключено')
    elif 'Успешно удален пакет' in output_text:
        res=QLabel('Пакеты были успешно удалены')
    else:
        res=QLabel('Пакеты не установлены или их удаление невозможно')
    line_res.addWidget(res)
    res_win.show()
def miui_services_easy_function():
    procent = 0
    for package in miui_services_easy:
        package = package.strip()
        command2 = ['./adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package]
        result = subprocess.run(command2, capture_output=True, text=True)
        if result.returncode == 0:
            output_text = f"Успешно удален пакет: {package}"
            procent += 1
            progress_bar.setValue(procent)
            QApplication.processEvents()
        else:
            output_text = f"Ошибка при удалении пакета {package}: {result.stderr}"
        with open(os.path.join(folder, '.history.txt'), 'a') as file:
            file.write(output_text)
        procent += 1
        progress_bar.setValue(procent)
        line9.addWidget(progress_bar)
        QApplication.processEvents()
    if 'adb: no devices/emulators found' in output_text:
        res=QLabel('Устройство не подключено')
    elif 'Успешно удален пакет' in output_text:
        res=QLabel('Пакеты были успешно удалены')
    else:
        res=QLabel('Пакеты не установлены или их удаление невозможно')
    line_res.addWidget(res)
    res_win.show()
def miui_services_all_function():
    procent = 0
    for package in miui_services_all:
        package = package.strip()
        command2 = ['./adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package]
        result = subprocess.run(command2, capture_output=True, text=True)
        if result.returncode == 0:
            output_text = f"Успешно удален пакет: {package}"
            procent += 1
            progress_bar.setValue(procent)
            QApplication.processEvents()
        else:
            output_text = f"Ошибка при удалении пакета {package}: {result.stderr}"
        with open(os.path.join(folder, '.history.txt'), 'a') as file:
            file.write(output_text)
        procent += 1
        progress_bar.setValue(procent)
        line9.addWidget(progress_bar)
        QApplication.processEvents()
    if 'adb: no devices/emulators found' in output_text:
        res=QLabel('Устройство не подключено')
    elif 'Успешно удален пакет' in output_text:
        res=QLabel('Пакеты были успешно удалены')
    else:
        res=QLabel('Пакеты не установлены или их удаление невозможно')
    line_res.addWidget(res)
    res_win.show()
def poweroff_function():
    command = ['./adb', 'shell', 'poweroff']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        output_text = "Команда POWEROFF выполнена успешно."
    else:
        output_text = f"Ошибка при выполнении команды POWEROFF: {result.stderr}"
    console_text = QLabel(output_text)
    line2v.addWidget(console_text) 
def reboot_function():
    command = ['./adb','shell','reboot']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        output_text = "Команда REBOOT выполнена успешно."
    else:
        output_text = f"Ошибка при выполнении команды REBOOT: {result.stderr}"
    console_text = QLabel(output_text)
    line2v.addWidget(console_text)
def reboot_recovery_function():
    command = ['./adb','reboot','recovery']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        output_text = "Команда reboot recovery выполнена успешно."
    else:
        output_text = f"Ошибка при выполнении команды reboot recovery: {result.stderr}"
    console_text = QLabel(output_text)
    line2v.addWidget(console_text) 
def reboot_fastboot_function():
    command = ['./adb','reboot','fastboot']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        output_text = "Команда reboot fastboot выполнена успешно."
    else:
        output_text = f"Ошибка при выполнении команды reboot fastboot: {result.stderr}"
    console_text = QLabel(output_text)
    line2v.addWidget(console_text)
def reboot_bootloader_function():
    command = ['./adb','reboot','bootloader']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        output_text = "Команда reboot bootloader выполнена успешно."
    else:
        output_text = f"Ошибка при выполнении команды reboot bootloader: {result.stderr}"
    console_text = QLabel(output_text)
    line2v.addWidget(console_text)
def reboot_edl_function():
    command = ['./adb','reboot','edl']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        output_text = "Команда reboot edl выполнена успешно."
    else:
        output_text = f"Ошибка при выполнении команды reboot edl: {result.stderr}"
    console_text = QLabel(output_text)
    line2v.addWidget(console_text)
def custom_script_function():
    custom_script_file, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Text Files (*.txt)")
    print(custom_script_file)
    with open(os.path.join(custom_script_file)) as file:
        for line in file:
            custom_script.append(line.strip())
    procent = 0
    for package in miui_services_all:
        package = package.strip()
        command2 = ['./adb', 'shell', 'pm', 'uninstall', '-k', '--user', '0', package]
        result = subprocess.run(command2, capture_output=True, text=True)
        if result.returncode == 0:
            output_text = f"Успешно удален пакет: {package}"
            procent += 1
            progress_bar.setValue(procent)
            QApplication.processEvents()
        else:
            output_text = f"Ошибка при удалении пакета {package}: {result.stderr}"
        with open(os.path.join(folder, '.history.txt'), 'a') as file:
            file.write(output_text)
        procent += 1
        progress_bar.setValue(procent)
        line9.addWidget(progress_bar)
        QApplication.processEvents()
    if 'adb: no devices/emulators found' in output_text:
        res=QLabel('Устройство не подключено')
    elif 'Успешно удален пакет' in output_text:
        res=QLabel('Пакеты были успешно удалены')
    else:
        res=QLabel('Пакеты не установлены или их удаление невозможно')
    res_win.show()

# Подключаем сигналы
devices.clicked.connect(devices_function)
easy_base_push.clicked.connect(easy_base_function)
samsung_services_push.clicked.connect(samsung_services_function)
poweroff_push.clicked.connect(poweroff_function)
reboot_push.clicked.connect(reboot_function)
reboot_recovery_push.clicked.connect(reboot_recovery_function)
reboot_fastboot_push.clicked.connect(reboot_fastboot_function)
miui_services_medium_push.clicked.connect(miui_services_medium_function)
gaps_all_delete_push.clicked.connect(gaps_function)
google_services_push.clicked.connect(google_services_function)
telegram_push.clicked.connect(telegram_function)
github_push.clicked.connect(github_function)
terminal_push.clicked.connect(terminal_dialog_function)
reboot_bootloader_push.clicked.connect(reboot_bootloader_function)
reboot_edl_push.clicked.connect(reboot_edl_function)
miui_services_all_push.clicked.connect(miui_services_all_function)
miui_services_easy_push.clicked.connect(miui_services_easy_function)
custom_script_push.clicked.connect(custom_script_function)
terminal_line_edit.returnPressed.connect(terminal_dialog_function)
youtube_push.clicked.connect(youtube_function)
main_win.show()
app.exec_()