
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

list_num = []
list_ca = [0]
list_return = []


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("rPtksrl.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)
        self.btn_3.clicked.connect(self.button3Function)
        self.btn_4.clicked.connect(self.button4Function)
        self.btn_5.clicked.connect(self.button5Function)
        self.btn_6.clicked.connect(self.button6Function)
        self.btn_7.clicked.connect(self.button7Function)
        self.btn_8.clicked.connect(self.button8Function)
        self.btn_9.clicked.connect(self.button9Function)
        self.btn_0.clicked.connect(self.button10Function)
        self.btn_back.clicked.connect(self.button11Function)
        self.btn_c.clicked.connect(self.button12Function)
        self.btn_div.clicked.connect(self.button13Function)
        self.btn_dot.clicked.connect(self.button14Function)
        self.btn_equal.clicked.connect(self.button15Function)
        self.btn_minus.clicked.connect(self.button16Function)
        self.btn_mul.clicked.connect(self.button17Function)
        self.btn_plus.clicked.connect(self.button18Function)
    def button1Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'1')

    def button2Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'2')

    def button3Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'3')

    def button4Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'4')

    def button5Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'5')
    
    def button6Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'6')

    def button7Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'7')

    def button8Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'8')

    def button9Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'9')
    
    def button10Function(self) :
        self.lineEdit.setText(self.lineEdit.text()+'0')

    def button11Function(self) :
        if self.lineEdit.text() != '':    
            self.lineEdit.setText(self.lineEdit.text().replace(self.lineEdit.text()[-1],''))
    
    def button12Function(self) :
        if self.lineEdit.text() != '':
            a = 0
            b = 0
            c = 0    
            self.lineEdit.setText('')
    
    def button13Function(self) :
        global a
        a = self.lineEdit.text()
        if a.find('.') == True:
            float(a)
        else:
            int(a)
        del list_ca[0]
        a = int(self.lineEdit.text())
        list_ca.append('/')
        self.lineEdit.setText(self.lineEdit.text()+'/')
        self.lineEdit.setText('')
    
    def button14Function(self) :
        list_num.append(int(self.lineEdit.text()))
        list_ca.append('.')
        self.lineEdit.setText(self.lineEdit.text()+'.')
        

    def button15Function(self) :
        global a,b,c
        if a == 0:
            a = c
        else:
            b = int(self.lineEdit.text())
        if list_ca[0] == '+':
            print(a+b)
            c = a + b
            a = 0
            self.lineEdit.setText(str(c))

        elif list_ca[0] == '-':
            print(a-b)
            c = a - b
            a = 0
            self.lineEdit.setText(str(c))

        elif list_ca[0] == 'x':
            print(a*b)
            c = a * b
            a = 0
            self.lineEdit.setText(str(c))

        elif list_ca[0] == '/':
            print(a/b)
            c = a / b
            a = 0
            self.lineEdit.setText(str(c))
            


    
    def button16Function(self) :
        global a
        a = self.lineEdit.text()
        if a.find('.') == True:
            float(a)
        else:
            int(a)
        list_num.append(int(self.lineEdit.text()))
        del list_ca[0]
        list_ca.append('-')
        self.lineEdit.setText(self.lineEdit.text()+'-')
        self.lineEdit.setText('')
    
    def button17Function(self) :
        global a
        a = self.lineEdit.text()
        if a.find('.') == True:
            float(a)
        else:
            int(a)
        list_num.append(int(self.lineEdit.text()))
        del list_ca[0]
        list_ca.append('x')
        self.lineEdit.setText(self.lineEdit.text()+'x')
        self.lineEdit.setText('')
        print(a)

    def button18Function(self) :
        global a
        a = self.lineEdit.text()
        
        if a.find('.') == True:
            float(a)
        else:
            int(a)
            print(a)
        del list_ca[0]
        list_ca.append('+')
        self.lineEdit.setText(self.lineEdit.text()+'+')
        self.lineEdit.setText('')
        print(a)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
