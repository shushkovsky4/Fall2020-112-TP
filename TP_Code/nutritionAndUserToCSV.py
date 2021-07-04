import csv
from datetime import date

#nutritionAndUserToCSV.py appends and reads user data from local CSV files

def addFoodData(calories, carbohydrates, protein, fat): #append user's day's food data to local CSV
    #Code for date taken from https://www.programiz.com/python-programming/datetime/current-datetime
    today = date.today()
    # mm/dd/y
    day = today.strftime("%m/%d/%y")
    
    fields = calories, carbohydrates, protein, fat, day
    
    with open('nutritionCSV.csv', 'a') as nutrition_csv:
        csvWriter = csv.writer(nutrition_csv)
        csvWriter.writerow(fields)

def readFoodData(): #Return stored user data
    result = []
    with open('nutritionCSV.csv', 'r') as nutrition_csv:
        csvReader = list(csv.reader(nutrition_csv))
        length = len(csvReader)
        if length >= 8: #checks if at least a week has been entered
            for i in range(-7, 0, 1): 
                result.append(csvReader[i])
        else: #gets the couple of days that have been entered
            for i in range((-1 * length + 1), 0, 1):
                result.append(csvReader[i])
    return result

def addUserData(height, weight, activity, gender, age, goal):
    fields = height, weight, activity, gender, age, goal
    with open('userInfo.csv', 'a') as userInfo_csv:
        csvWriter = csv.writer(userInfo_csv)
        csvWriter.writerow(fields)

def readUserData():
    result = []
    with open('userInfo.csv', 'r') as userInfo_csv:
        csvReader = list(csv.reader(userInfo_csv))
        result.append(csvReader[-1])
    return result

        