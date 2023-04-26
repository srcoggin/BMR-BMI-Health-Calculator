#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MainWindow import Ui_MainWindow
from DataStore import DataStore



class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ds = DataStore()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
       
        self.ui.bmr_button.clicked.connect(self.showBMR)
        self.ui.bmi_button.clicked.connect(self.showBMI)

        self.ui.bmr_calculate_button.clicked.connect(self.calcBMR)
        self.ui.bmi_calculate_button.clicked.connect(self.calcBMI)

    def show(self):
        self.main_win.show()

    def showBMR(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bmr)

    def showBMI(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bmi)

    def calcBMR (self):
        pass

    def calcBMI (self):
        #get input values from ui
        height = int(self.ui.bmi_height_input.text())
        weight = int(self.ui.bmi_weight_input.text())
        #pass those to data store
        result = self.ds.bmi_calc(height, weight)
        #format output
        output = (f"You entered the following information for BMI: Height {height}cm & Weight {weight}kg. This means your BMI is {result}")
        #output to ui
        self.ui.bmi_calculate_output.setText(output)

 
    def showBMR(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bmr)

    def calcBMR(self):
        # get input values from ui
        height = int(self.ui.bmr_height_input.text())
        weight = int(self.ui.bmr_weight_input.text())
        age = int(self.ui.bmr_age_input.text())
        if self.ui.bmr_male_radio.isChecked():
            sex = "male"
        else:
            sex = "female"
        # pass these values to data store
        if self.ui.bmr_sedintary.isChecked():
            activity = "sedentary"
        elif self.ui.bmr_lightly.isChecked():
            activity = "lightly active"
        elif self.ui.bmr_moderatly.isChecked():
            activity = "moderately active"
        elif self.ui.bmr_very.isChecked():
            activity = "very active"
        elif self.ui.bmr_extremely.isChecked():
            activity = "extremely active"
            
        result = self.ds.calc_bmr(height, weight, age, sex, activity)
        # format output
        output = (f"The total calorie intake for a {age} year old {sex}, who is {height}cm tall and weighs {weight}kg, who is {activity} is: {result} calories.")
        # output to ui
        self.ui.bmr_output.setText(output)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())