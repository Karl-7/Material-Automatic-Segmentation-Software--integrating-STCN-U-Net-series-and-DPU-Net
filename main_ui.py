# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAIN_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
#pyuic5 -o MAIN_UI.py MAIN_UI.ui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QFileDialog, QLabel, QComboBox, QDialog, QDialogButtonBox, QFrame, QSplitter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGraphicsPixmapItem
import os
from TRAIN_TEST_METRIC_START import train_test_metric_start
import time
#z
class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('输入数据集地址')
        self.setGeometry(400, 200, 300, 100)
        self.layout = QVBoxLayout()

        self.input_text = QLineEdit(self)
        self.layout.addWidget(self.input_text)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

        
        self.setLayout(self.layout)

    def get_text(self):
        return self.input_text.text()

class Ui_MainWindow(object):  
    def setupUi(self, MainWindow):
        self.expand_percent = 2
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1540, 768)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.insert_add_Button = QtWidgets.QPushButton(self.centralwidget)
        self.insert_add_Button.clicked.connect(self.open_input_dialog)
        self.insert_add_Button.setGeometry(QtCore.QRect(20*self.expand_percent, 10*self.expand_percent, 71*self.expand_percent, 23*self.expand_percent))
        self.insert_add_Button.setMinimumSize(QtCore.QSize(71*self.expand_percent, 0))
        self.insert_add_Button.setStyleSheet("color: rgb(213, 213, 213);\n"
"font: 16pt \"Agency FB\";\n"
"font: 75 6pt \"Agency FB\";\n"
"font: 12pt \"黑体\";\n"
"\n"
"background-color: rgb(127, 15, 255);")
        self.insert_add_Button.setObjectName("insert_add_Button")
        self.net_choose_box = QtWidgets.QComboBox(self.centralwidget)
        self.net_choose_box.setGeometry(QtCore.QRect(100*self.expand_percent, 10*self.expand_percent, 71*self.expand_percent, 20*self.expand_percent))
        self.net_choose_box.setMinimumSize(QtCore.QSize(71*self.expand_percent, 0))
        self.net_choose_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.net_choose_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.net_choose_box.setStyleSheet("\n"
"font: 9pt \"Agency FB\";\n"
"font: 75 6pt \"Agency FB\";\n"
"font: 12pt \"黑体\";\n"
"background-color: rgb(170, 85, 255);\n"
"color: rgb(220, 220, 220);")
        self.net_choose_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.net_choose_box.setObjectName("net_choose_box")
        self.net_choose_box.addItem("")
        self.net_choose_box.addItem("")
        self.net_choose_box.addItem("")
        self.net_choose_box.addItem("")
        self.net_choose_box.addItem("")
        self.train_button = QtWidgets.QPushButton(self.centralwidget)
        self.train_button.clicked.connect(lambda: train_test_metric_start(self.dataset_address,self.net_choose_box.currentText(),'train'))
        # self.train_button.clicked.connect(lambda:(self.epoch_show()))
        self.train_button.setGeometry(QtCore.QRect(50*self.expand_percent, 210*self.expand_percent, 71*self.expand_percent, 23*self.expand_percent))
        self.train_button.setMinimumSize(QtCore.QSize(71*self.expand_percent, 0))
        self.train_button.setStyleSheet("color: rgb(213, 213, 213);\n"
"font: 9pt \"Agency FB\";\n"
"font: 75 6pt \"Agency FB\";\n"
"font: 12pt \"黑体\";\n"
"\n"
"background-color: rgb(127, 15, 255);")
        self.train_button.setObjectName("train_button")
        self.test_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_button.clicked.connect(lambda: (train_test_metric_start(self.dataset_address,self.net_choose_box.currentText(),'test')))
        # self.test_button.clicked.connect(lambda:(self.video_length_show()))
        self.test_button.setGeometry(QtCore.QRect(50*self.expand_percent, 250*self.expand_percent, 71*self.expand_percent, 23*self.expand_percent))
        self.test_button.setMinimumSize(QtCore.QSize(71*self.expand_percent, 0))
        self.test_button.setStyleSheet("color: rgb(213, 213, 213);\n"
"font: 9pt \"Agency FB\";\n"
"font: 75 6pt \"Agency FB\";\n"
"font: 12pt \"黑体\";\n"
"\n"
"background-color: rgb(127, 15, 255);")
        self.test_button.setObjectName("test_button")
        self.metric_button = QtWidgets.QPushButton(self.centralwidget)
        self.metric_button.clicked.connect(lambda: (
                                           train_test_metric_start(self.dataset_address,self.net_choose_box.currentText(),'metric'),
                                           self.update_metric_images()
                                           ))
        self.metric_button.clicked.connect(lambda: (
                                           self.update_metric_images()
                                           ))
        self.metric_button.setGeometry(QtCore.QRect(50*self.expand_percent, 290*self.expand_percent, 71*self.expand_percent, 23*self.expand_percent))
        self.metric_button.setMinimumSize(QtCore.QSize(71, 0))
        self.metric_button.setStyleSheet("color: rgb(213, 213, 213);\n"
"font: 9pt \"Agency FB\";\n"
"font: 75 6pt \"Agency FB\";\n"
"font: 12pt \"黑体\";\n"
"\n"
"background-color: rgb(127, 15, 255);")
        self.metric_button.setObjectName("metric_button")
        self.video_number = QtWidgets.QTextBrowser(self.centralwidget)
        self.video_number.setGeometry(QtCore.QRect(20*self.expand_percent, 40*self.expand_percent, 151*self.expand_percent, 161*self.expand_percent))
        self.video_number.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.video_number.setObjectName("video_number")
        # self.useless_label = QtWidgets.QLabel(self.centralwidget)
        # self.useless_label.setGeometry(QtCore.QRect(20*self.expand_percent, 50*self.expand_percent, 36*self.expand_percent, 8*self.expand_percent))
        # self.useless_label.setObjectName("useless_label")

        
         
        
        # self.net_parameters = QtWidgets.QPushButton(self.centralwidget)
        # self.net_parameters.setGeometry(QtCore.QRect(20*self.expand_percent, 170*self.expand_percent, 71*self.expand_percent, 23*self.expand_percent))
        # self.net_parameters.setMinimumSize(QtCore.QSize(71*self.expand_percent, 0))
        # self.net_parameters.setStyleSheet("\n"
# "font: 9pt \"Agency FB\";\n"
# "font: 75 6pt \"Agency FB\";\n"
# "font: 9pt \"黑体\";\n"
# "background-color: rgb(170, 85, 255);\n"
# "color: rgb(220, 220, 220);")
#         self.net_parameters.setObjectName("net_parameters")
        self.dataset_image = QtWidgets.QLabel(self.centralwidget)
        self.dataset_image.setGeometry(QtCore.QRect(190*self.expand_percent, 30*self.expand_percent, 261*self.expand_percent, 281*self.expand_percent))
        self.dataset_image.setStyleSheet("color: rgb(255, 85, 127);\n"
"background-color: rgb(205, 208, 255);")
        self.dataset_image.setText("")
        self.dataset_image.setObjectName("dataset_image")
        self.dataset_label = QtWidgets.QLabel(self.centralwidget)
        self.dataset_label.setGeometry(QtCore.QRect(460*self.expand_percent, 30*self.expand_percent, 251*self.expand_percent, 281*self.expand_percent))
        self.dataset_label.setStyleSheet("color: rgb(255, 85, 127);\n"
"background-color: rgb(205, 208, 255);")
        self.dataset_label.setText("")
        self.dataset_label.setObjectName("dataset_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.dataset_address=''


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Material VOS Application"))
        self.insert_add_Button.setText(_translate("MainWindow", "数据集地址"))
        self.net_choose_box.setItemText(0, _translate("MainWindow", "选择模型"))
        self.net_choose_box.setItemText(1, _translate("MainWindow", "STCN"))
        self.net_choose_box.setItemText(2, _translate("MainWindow", "U-Net"))
        self.net_choose_box.setItemText(3, _translate("MainWindow", "WPU-Net"))
        self.net_choose_box.setItemText(4, _translate("MainWindow", "DPU-Net"))
        self.train_button.setText(_translate("MainWindow", "开始训练"))
        self.test_button.setText(_translate("MainWindow", "开始测试"))
        self.metric_button.setText(_translate("MainWindow", "开始评估"))
        # self.useless_label.setText(_translate("MainWindow", "视频："))
        # self.net_parameters.setText(_translate("MainWindow", "超参调整"))

    def open_input_dialog(self):
        dialog = InputDialog()
        if dialog.exec_():
            self.dataset_address = dialog.get_text()
            self.update_images()
        # Show directory and subdirectories
        directory = self.dataset_address
        if directory:
            subdirectories = []
            for root, dirs, files in os.walk(directory):
                level = root.replace(directory, '').count(os.sep)
                indent = ' ' * 4 * (level)
                subdirectories.append('{}{}'.format(indent, os.path.basename(root)))
            subdirectories_text = ''
            for subdirectory in subdirectories:
                level = subdirectory.count('/')
                indent = ' ' * level
                subdirectories_text += f"{indent}{subdirectory}\n"
            self.video_number.setText(f"dataset:\n{subdirectories_text}")
        else:
            self.video_number.setText('No directory selected.')
               #D:\QT5_VOS_slicer\dataset
    def update_images(self):
        if self.dataset_address:
            image_files = [file for file in os.listdir(os.path.join(self.dataset_address, 'trainval/train/JPEGImages/video1')) if (file.endswith('.png') or file.endswith('.jpg') or file.endswith('.tif')) and file[:-4].isdigit()]
            label_files = [file for file in os.listdir(os.path.join(self.dataset_address, 'trainval/train/Annotations/video1')) if (file.endswith('.png') or file.endswith('.jpg') or file.endswith('.tif')) and file[:-4].isdigit()]
            if image_files:
                min_image_file = min(image_files, key=lambda x: int(x[:-4]))
                min_label_file = min(label_files, key=lambda x: int(x[:-4]))
                image_path = os.path.join(self.dataset_address, 'trainval/train/JPEGImages/video1', min_image_file)
                label_path = os.path.join(self.dataset_address, 'trainval/train/Annotations/video1', min_label_file)
                # Rest of the code...
            else:
                self.dataset_image.setText('No image found.')
                self.dataset_label.setText('No label found.')

            if os.path.exists(image_path):
                if os.path.exists(image_path):
                    pixmap = QPixmap(image_path)
                    scaled_pixmap = pixmap.scaled(560,560, Qt.AspectRatioMode.KeepAspectRatio)
                    self.dataset_image.setPixmap(scaled_pixmap)
                    self.dataset_image.setAlignment(Qt.AlignCenter)
                else:
                    self.dataset_image.setText('No image found.')
            else:
                self.dataset_image.setText('No image found.')

            if os.path.exists(label_path):
                if os.path.exists(label_path):
                    pixmap = QPixmap(label_path)
                    scaled_pixmap = pixmap.scaled(560, 560, Qt.AspectRatioMode.KeepAspectRatio)
                    self.dataset_label.setPixmap(scaled_pixmap)
                    self.dataset_label.setAlignment(Qt.AlignCenter)
                else:
                    self.dataset_label.setText('No label found.')
            else:
                self.dataset_label.setText('No label found.')

    def update_metric_images(self):
        if self.dataset_address:
            image_files = [file for file in os.listdir(os.path.join(self.dataset_address, 'METRIC_PICS/video1')) if (file.endswith('.png') or file.endswith('.jpg') or file.endswith('.tif')) and file[:-4].isdigit()]
            label_files = [file for file in os.listdir(os.path.join(self.dataset_address, 'label_results/video1')) if (file.endswith('.png') or file.endswith('.jpg') or file.endswith('.tif')) and file[:-4].isdigit()]
            if image_files:
                min_image_file = min(image_files, key=lambda x: int(x[:-4]))
                min_label_file = min(label_files, key=lambda x: int(x[:-4]))
                image_path = os.path.join(self.dataset_address, 'METRIC_PICS/video1', min_image_file)
                label_path = os.path.join(self.dataset_address, 'label_results/video1', min_label_file)
                # Rest of the code...
            else:
                self.dataset_image.setText('No image found.')
                self.dataset_label.setText('No label found.')

            if os.path.exists(image_path):
                if os.path.exists(image_path):
                    pixmap = QPixmap(image_path)
                    scaled_pixmap = pixmap.scaled(560,560, Qt.AspectRatioMode.KeepAspectRatio)
                    self.dataset_image.setPixmap(scaled_pixmap)
                    self.dataset_image.setAlignment(Qt.AlignCenter)
                else:
                    self.dataset_image.setText('No image found.')
            else:
                self.dataset_image.setText('No image found.')

            if os.path.exists(label_path):
                if os.path.exists(label_path):
                    pixmap = QPixmap(label_path)
                    scaled_pixmap = pixmap.scaled(560, 560, Qt.AspectRatioMode.KeepAspectRatio)
                    self.dataset_label.setPixmap(scaled_pixmap)
                    self.dataset_label.setAlignment(Qt.AlignCenter)
                else:
                    self.dataset_label.setText('No label found.')
            else:
                self.dataset_label.setText('No label found.')

    def epoch_show(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Epoch Progress")
        dialog.setGeometry(100, 100, 300, 100)
        #D:\QT5_VOS_slicer\dataset
        epoch_progressBar = QtWidgets.QProgressBar(dialog)
        epoch_progressBar.setGeometry(QtCore.QRect(20*self.expand_percent, 10*self.expand_percent, 191*self.expand_percent, 23*self.expand_percent))
        epoch_progressBar.setObjectName("epoch_progressBar")
        epoch_label = QtWidgets.QLabel(dialog)
        epoch_label.setGeometry(QtCore.QRect(220*self.expand_percent, 10*self.expand_percent, 61*self.expand_percent, 21*self.expand_percent))
        total_epochs = 500
        current_epoch = 0
        epoch_label.setObjectName("epoch_label")
        while current_epoch <= total_epochs:
            epoch_progressBar.setValue(int(current_epoch / total_epochs * 100))
            epoch_label.setText(f"{current_epoch}/{total_epochs}")
            current_epoch += 1
            QApplication.processEvents()  # 处理所有当前的事件
            # time.sleep(10)
        
        dialog.exec_()


    def video_length_show(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("test progress")
        dialog.setGeometry(100, 100, 300, 100)
        
        video_length_progressBar = QtWidgets.QProgressBar(dialog)
        video_length_progressBar.setGeometry(QtCore.QRect(20*self.expand_percent, 10*self.expand_percent, 191*self.expand_percent, 23*self.expand_percent))
        video_length_progressBar.setObjectName("test_progressBar")
        video_length_label=QtWidgets.QLabel(dialog)
        video_length_label.setGeometry(QtCore.QRect(220*self.expand_percent, 10*self.expand_percent, 61*self.expand_percent, 21*self.expand_percent))
        total_video_length = 146
        current_video_length = 0
        while current_video_length <= total_video_length:
            video_length_progressBar.setValue(int(current_video_length / total_video_length * 100))

            video_length_label.setText(f"{current_video_length}/{total_video_length}")
            current_video_length += 1
            QApplication.processEvents()  # 处理所有当前的事件
            # time.sleep(5)
        
        video_length_label = QtWidgets.QLabel(dialog)
        video_length_label.setGeometry(QtCore.QRect(220*self.expand_percent, 10*self.expand_percent, 61*self.expand_percent, 21*self.expand_percent))
        video_length_label.setObjectName("video_length_label")
        video_length_label.setText(current_video_length,"/",total_video_length)
        
        dialog.exec_()

if __name__=="__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(str(e))
        error_dialog.exec_()
        # sys.exit(app.exec_())  # Comment out this line to ignore the error and continue running the application