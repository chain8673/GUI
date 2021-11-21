from PySide2.QtWidgets import QMainWindow, QTextEdit, QApplication, QPushButton, QRadioButton, QButtonGroup, QLabel, \
    QComboBox

if __name__ == "__main__":
    def test():
        data = []
        data.append(textEdit.toPlainText())
        data.append(buttonGroup1.checkedButton().text())
        data.append(cb.currentText())
        data.append(textEdit2.toPlainText())
        print(data)
        data.clear()

app = QApplication([])
window = QMainWindow()
window.resize(1000, 600)
window.move(600, 200)
window.setWindowTitle('测试窗口')

# 姓名
label1 = QLabel(window)
label1.setText('姓名：')
label1.move(20, 30)
textEdit = QTextEdit(window)
textEdit.move(100, 30)

# 性别选项，采用RadioButton方式
label2 = QLabel(window)
label2.setText('性别：')
label2.move(20, 80)
radioButton1 = QRadioButton('男', window)
radioButton1.setChecked(True)
radioButton2 = QRadioButton('女', window)
radioButton1.move(100, 80)
radioButton2.move(100, 110)

buttonGroup1 = QButtonGroup()
buttonGroup1.addButton(radioButton1)
buttonGroup1.addButton(radioButton2)
buttonGroup1.setExclusive(True)

# 学历选项，采用下拉框方式，也就是ComboBox
label3 = QLabel(window)
label3.setText('学历：')
label3.move(20, 160)
cb = QComboBox(window)
cb.move(100, 160)
cb.addItem('高中')
cb.addItem('本科')
cb.addItem('研究生')

# 描述
label1 = QLabel(window)
label1.setText('描述：')
label1.move(20, 210)
textEdit2 = QTextEdit(window)
textEdit2.resize(300, 100)
textEdit2.move(100, 210)

# 按钮
button = QPushButton('Submit', window)
button.move(300, 100)
button.clicked.connect(test)

window.show()
app.exec_()
