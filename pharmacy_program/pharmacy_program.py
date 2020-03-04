import sys

import pharmacy_data
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pharmacy_program.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 객체의 이벤트에서 connect 함수를 호출하고 인자에 이벤트 처리기에서 수  행하는 함수를 기재한다.
        self.pushButton.clicked.connect(self.btn_clicked)

    # 약국정보 API 요청 하여 표시 오픈시간 부터 마무리 시간 사이의 약국 정보 표기
    def pharmacy_text(self, msg, start_time, end_time):
        for wday in msg:
            if wday == "일요일":
                text_data = pharmacy_data.pharmarcy_API(wday, start_time, end_time)
                if self.textEdit_8.toPlainText():
                    self.textEdit_8.clear()
                for i in range(len(text_data)):
                    self.textEdit_8.append(text_data[i]['data']['pharmacy_name'] + "(" +
                                           text_data[i]['data']['pharmacy_addr'] + ") Tel : " +
                                           text_data[i]['data']['pharmacy_tel'] + " // Time: " +
                                           str(text_data[i]['data']['am_time']) + " ~ " +
                                           str(text_data[i]['data']['pm_time']))
            elif wday == "월요일":
                text_data = pharmacy_data.pharmarcy_API(wday, start_time, end_time)
                if self.textEdit.toPlainText():
                    self.textEdit.clear()
                for i in range(len(text_data)):
                    self.textEdit.append(text_data[i]['data']['pharmacy_name'] + "(" +
                                           text_data[i]['data']['pharmacy_addr'] + ") Tel : " +
                                           text_data[i]['data']['pharmacy_tel'] + " // Time: " +
                                           str(text_data[i]['data']['am_time']) + " ~ " +
                                           str(text_data[i]['data']['pm_time']))
            elif wday == "화요일":
                text_data = pharmacy_data.pharmarcy_API(wday, start_time, end_time)
                if self.textEdit_2.toPlainText():
                    self.textEdit_2.clear()
                for i in range(len(text_data)):
                    self.textEdit_2.append(text_data[i]['data']['pharmacy_name'] + "(" +
                                           text_data[i]['data']['pharmacy_addr'] + ") Tel : " +
                                           text_data[i]['data']['pharmacy_tel'] + " // Time: " +
                                           str(text_data[i]['data']['am_time']) + " ~ " +
                                           str(text_data[i]['data']['pm_time']))
            elif wday == "수요일":
                text_data = pharmacy_data.pharmarcy_API(wday, start_time, end_time)
                if self.textEdit_3.toPlainText():
                    self.textEdit_3.clear()
                for i in range(len(text_data)):
                    self.textEdit_3.append(text_data[i]['data']['pharmacy_name'] + "(" +
                                           text_data[i]['data']['pharmacy_addr'] + ") Tel : " +
                                           text_data[i]['data']['pharmacy_tel'] + " // Time: " +
                                           str(text_data[i]['data']['am_time']) + " ~ " +
                                           str(text_data[i]['data']['pm_time']))
            elif wday == "목요일":
                text_data = pharmacy_data.pharmarcy_API(wday, start_time, end_time)
                if self.textEdit_4.toPlainText():
                    self.textEdit_4.clear()
                for i in range(len(text_data)):
                    self.textEdit_4.append(text_data[i]['data']['pharmacy_name'] + "(" +
                                           text_data[i]['data']['pharmacy_addr'] + ") Tel : " +
                                           text_data[i]['data']['pharmacy_tel'] + " // Time: " +
                                           str(text_data[i]['data']['am_time']) + " ~ " +
                                           str(text_data[i]['data']['pm_time']))
            elif wday == "금요일":
                text_data = pharmacy_data.pharmarcy_API(wday, start_time, end_time)
                if self.textEdit_5.toPlainText():
                    self.textEdit_5.clear()
                for i in range(len(text_data)):
                    self.textEdit_5.append(text_data[i]['data']['pharmacy_name'] + "(" +
                                           text_data[i]['data']['pharmacy_addr'] + ") Tel : " +
                                           text_data[i]['data']['pharmacy_tel'] + " // Time: " +
                                           str(text_data[i]['data']['am_time']) + " ~ " +
                                           str(text_data[i]['data']['pm_time']))
            elif wday == "토요일":
                text_data = pharmacy_data.pharmarcy_API(wday, start_time, end_time)
                if self.textEdit_6.toPlainText():
                    self.textEdit_6.clear()
                for i in range(len(text_data)):
                    self.textEdit_6.append(text_data[i]['data']['pharmacy_name'] + "(" +
                                           text_data[i]['data']['pharmacy_addr'] + ") Tel : " +
                                           text_data[i]['data']['pharmacy_tel'] + " // Time: " +
                                           str(text_data[i]['data']['am_time']) + " ~ " +
                                           str(text_data[i]['data']['pm_time']))
            elif wday == "공휴일":
                text_data = pharmacy_data.pharmarcy_API(wday, start_time, end_time)
                if self.textEdit_7.toPlainText():
                    self.textEdit_7.clear()
                for i in range(len(text_data)):
                    self.textEdit_7.append(text_data[i]['data']['pharmacy_name'] + "(" +
                                           text_data[i]['data']['pharmacy_addr'] + ") Tel : " +
                                           text_data[i]['data']['pharmacy_tel'] + " // Time: " +
                                           str(text_data[i]['data']['am_time']) + " ~ " +
                                           str(text_data[i]['data']['pm_time']))

    # 검색 클릭 시 요일 체크 및 시간 체크
    def btn_clicked(self):
        msg = []
        if self.checkBox_7.isChecked() == True:
            msg.append("일요일")
        if self.checkBox.isChecked() == True:
            msg.append("월요일")
        if self.checkBox_2.isChecked() == True:
            msg.append("화요일")
        if self.checkBox_3.isChecked() == True:
            msg.append("수요일")
        if self.checkBox_4.isChecked() == True:
            msg.append("목요일")
        if self.checkBox_5.isChecked() == True:
            msg.append("금요일")
        if self.checkBox_6.isChecked() == True:
            msg.append("토요일")
        if self.checkBox_8.isChecked() == True:
            msg.append("공휴일")

        # 시간 포맷바꾸기
        starttime = self.dateTimeEdit.time().toString("hhmm")
        endtime = self.dateTimeEdit_2.time().toString("hhmm")

        if not msg:
            QMessageBox.about(self, "message", "요일을 클릭하세요.")
        else:
            self.pharmacy_text(msg, starttime, endtime)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
