import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import random

class LPS(QDialog):
    def __init__(self):
        super(LPS,self).__init__()
        self.widget=QtWidgets.QStackedWidget()
        loadUi("LPS.ui",self)

        self.dna_bttn.clicked.connect(self.generateDNA)
        self.lps_bttn.clicked.connect(self.generateLPS)
    
    def generateDNA(self):
        letters = ['C', 'G', 'A', 'T']
        length = random.randint(5, 15)
        random_string = ''.join(random.choice(letters) for _ in range(length))
        self.dna_txt.setText(random_string)
        self.lps_label.setText('')

    def generateLPS(self):
        dna_seq = self.dna_txt.text()
        dna_len = len(dna_seq)
        if dna_len < 1:
            self.show_warning_message_box("Please enter DNA sequence.")
            self.dna_txt.setText('')
        else:
            if self.checkString(dna_seq, dna_len):
                dna_seq = self.dna_txt.text()
                dna_lps = self.longest_palindromic_subsequence(dna_seq)
                self.lps_label.setText(dna_lps)
            else:
                self.show_warning_message_box("Invalid DNA sequence.")
                self.dna_txt.setText('')

    def longest_palindromic_subsequence(self, seq):
        N = len(seq)
        L = [[0] * N for _ in range(N)]
        
        for i in range(N):
            L[i][i] = 1
        
        for i in range(2, N + 1):
            for j in range(N - i + 1):
                k = j + i - 1

                if seq[j] == seq[k] and i == 2:
                    L[j][k] = 2
                elif seq[j] == seq[k]:
                    L[j][k] = L[j + 1][k - 1] + 2
                else:
                    L[j][k] = max(L[j + 1][k], L[j][k - 1])

        subsequence = []
        i, j = 0, N - 1
        while i < N and j >= 0:
            if seq[i] == seq[j]:
                subsequence.append(seq[i])
                i += 1
                j -= 1
            elif j > 0 and L[i][j - 1] >= L[i + 1][j]:
                j -= 1
            else:
                i += 1

        return ''.join(subsequence)
        
    def checkString(self, dna_sequence, dna_length):
        for i in range(dna_length):
            if dna_sequence[i] != 'G' and dna_sequence[i] != 'A' and dna_sequence[i] != 'C' and dna_sequence[i] != 'T':
                return False
        return True
    
    def show_warning_message_box(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

        button_ok = msg_box.button(QMessageBox.Ok)
        button_ok.clicked.connect(msg_box.reject)

        msg_box.exec_()

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
MainWindow = LPS()
widget = QtWidgets.QStackedWidget()
widget.addWidget(MainWindow)
widget.setFixedWidth(662)
widget.setFixedHeight(464)
widget.show()
app.exec_()
