

from PyQt5 import QtCore, QtGui, QtWidgets
from ViewDataSet import ViewDataSet
from UploadDataset import Ui_UploadDataset
from PerformanceCal import performancealg
class Ui_AdminHome(object):

    def upload(self):
        try:
            self.upld = QtWidgets.QDialog()
            self.ui = Ui_UploadDataset()
            self.ui.setupUi(self.upld)
            self.upld.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def viewdataSet(self):
        self.viewds = QtWidgets.QDialog()
        self.ui = ViewDataSet()
        self.ui.setupUi(self.viewds)
        self.ui.viewdata()
        self.viewds.show()

    def algperformance(self):
        performancealg()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 413)
        Dialog.setStyleSheet("background-color: rgb(32, 64, 97);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 90, 211, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(126, 63, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.upload)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 211, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(126, 63, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.viewdataSet)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 270, 211, 41))
        self.pushButton_3.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(126, 63, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.algperformance)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.pushButton.setText(_translate("Dialog", "Upload Dataset"))
        self.pushButton_2.setText(_translate("Dialog", "View Dataset"))
        self.pushButton_3.setText(_translate("Dialog", "Accuracy Measures"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
