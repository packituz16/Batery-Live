# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox_batteryw = QtWidgets.QSpinBox(Dialog)
        self.spinBox_batteryw.setMaximum(100)
        self.spinBox_batteryw.setProperty("value", 20)
        self.spinBox_batteryw.setObjectName("spinBox_batteryw")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_batteryw)
        self.checkBox_autostart = QtWidgets.QCheckBox(Dialog)
        self.checkBox_autostart.setObjectName("checkBox_autostart")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_autostart)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox_update = QtWidgets.QSpinBox(Dialog)
        self.spinBox_update.setMinimum(1)
        self.spinBox_update.setMaximum(60)
        self.spinBox_update.setSingleStep(1)
        self.spinBox_update.setObjectName("spinBox_update")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_update)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.spinBox_batteryw)
        self.label_2.setBuddy(self.spinBox_update)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label.setText(_translate("Dialog", "&Battery Warning"))
        self.spinBox_batteryw.setSuffix(_translate("Dialog", "%"))
        self.checkBox_autostart.setText(_translate("Dialog", "&Autostart"))
        self.label_2.setText(_translate("Dialog", "&Update Time:"))
        self.spinBox_update.setSuffix(_translate("Dialog", " sec"))

