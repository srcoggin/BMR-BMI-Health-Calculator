class DataStore:
    def __init__(self):
        pass

    def bmi_calc(self, height, weight):
        bmi = round((weight / ((height / 100)*(height / 100))))
        return bmi
    
    @staticmethod
    def calc_bmr(height, weight, age, sex, activity):
        if sex == "male":
            startVal = 66.5
            weight_modifier = 13.7
            height_modifier = 5
            age_modifier = 6.8
        else:
            startVal = 665.1
            weight_modifier = 9.6
            height_modifier = 1.8
            age_modifier = 4.7
        if activity == "sedentary":
            activity_modifier = 1.2
        if activity == "lightly active":
            activity_modifier = 1.375
        if activity == "moderately active":
            activity_modifier = 1.5
        if activity == "very active":
            activity_modifier = 1.725
        if activity == "extremely active":
            activity_modifier = 1.9
        
        return int(startVal + (weight_modifier * weight) + (height_modifier * height) - (age_modifier * age) * activity_modifier)