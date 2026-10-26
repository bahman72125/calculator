import sys
from PyQt5.QtWidgets import QApplication ,QWidget ,QPushButton,QLineEdit
class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.mysignals()
        self.number='0'
        self.last_number = None
        self.last_operator = None


    def setupUI(self):
        self.setGeometry(100,100,255,420)
        self.setWindowTitle('calculator')
        self.lineEdit=QLineEdit(self)
        self.lineEdit.setGeometry(20,20,215,50)

        self.btn7=QPushButton(self,text='7')
        self.btn7.setGeometry(20,90,50,50)
        self.btn8=QPushButton(self,text='8')
        self.btn8.setGeometry(75,90,50,50)
        self.btn9=QPushButton(self,text='9')
        self.btn9.setGeometry(130,90,50,50)
        self.btnz=QPushButton(self,text='*')
        self.btnz.setGeometry(185,90,50,50)
        self.btn4=QPushButton(self,text='4')
        self.btn4.setGeometry(20,150,50,50)
        self.btn5=QPushButton(self,text='5')
        self.btn5.setGeometry(75,150,50,50)
        self.btn6=QPushButton(self,text='6')
        self.btn6.setGeometry(130,150,50,50)
        self.btntt=QPushButton(self,text='/')
        self.btntt.setGeometry(185,150,50,50)
        self.btn1=QPushButton(self,text='1')
        self.btn1.setGeometry(20,210,50,50)
        self.btn2=QPushButton(self,text='2')
        self.btn2.setGeometry(75,210,50,50)
        self.btn3=QPushButton(self,text='3')
        self.btn3.setGeometry(130,210,50,50)
        self.btnj=QPushButton(self,text='+')
        self.btnj.setGeometry(185,210,50,50)  
        self.btnmm=QPushButton(self,text='.')
        self.btnmm.setGeometry(20,270,50,50)
        self.btn0=QPushButton(self,text='0')
        self.btn0.setGeometry(75,270,50,50)
        self.btnn=QPushButton(self,text='=')
        self.btnn.setGeometry(130,270,50,50)
        self.btnm=QPushButton(self,text='-')
        self.btnm.setGeometry(185,270,50,50)  

        self.btne=QPushButton(self,text='Exit')
        self.btne.setGeometry(20,330,215,30)
        self.btnc=QPushButton(self,text='Clear')
        self.btnc.setGeometry(20,370,215,30)
    def mysignals(self):
        self.btn0.clicked.connect(lambda:self.btnclick('0'))
        self.btn1.clicked.connect(lambda:self.btnclick('1'))
        self.btn2.clicked.connect(lambda:self.btnclick('2'))
        self.btn3.clicked.connect(lambda:self.btnclick('3'))
        self.btn4.clicked.connect(lambda:self.btnclick('4'))
        self.btn5.clicked.connect(lambda:self.btnclick('5'))
        self.btn6.clicked.connect(lambda:self.btnclick('6'))
        self.btn7.clicked.connect(lambda:self.btnclick('7'))
        self.btn8.clicked.connect(lambda:self.btnclick('8'))
        self.btn9.clicked.connect(lambda:self.btnclick('9'))
        self.btnj.clicked.connect(lambda:self.btnclick('+'))
        self.btnz.clicked.connect(lambda:self.btnclick('*'))
        self.btnmm.clicked.connect(lambda:self.btnclick('.'))
        self.btnm.clicked.connect(lambda:self.btnclick('-'))
        self.btntt.clicked.connect(lambda:self.btnclick('/'))
        self.btne.clicked.connect(self.close)
        self.btnc.clicked.connect(self.myclear)
        self.btnn.clicked.connect(self.btnEquclick)
    
    def btnEquclick(self):
        if self.last_number is None:
            self.answer = eval(self.number)
            for op in ["+", "-", "*", "/"]:
                if op in self.number:
                    left, right = self.number.rsplit(op, 1)
                    self.last_operator = op
                    self.last_number = right
                    break
        else:
            self.number = str(self.answer) + self.last_operator + str(self.last_number)
            self.answer = eval(self.number)

        self.number = str(self.answer)
        self.lineEdit.setText(self.number)
   
    def myclear(self):
        self.number='0' 
        self.answer='0'
        self.last_number=None
        self.lineEdit.setText(self.number)       
    
    def btnclick(self,txt):
        if txt in'+-*/':
            if self.number[-1] in '+-*/':
                self.number=self.number[:-1]
                self.number+= txt
            else:
                self.number+= txt
        elif txt == '.':
            if  '.' in self.number:
                pass
            else:
                self.number+= txt
        else:        
            if self.number=='0':
                self.number=txt
            else:
                self.number+=txt 
        self.lineEdit.setText(self.number)            
    
if __name__ =='__main__':
    app=QApplication(sys.argv)
    window=Form()
    window.show()  
    sys.exit(app.exec())         