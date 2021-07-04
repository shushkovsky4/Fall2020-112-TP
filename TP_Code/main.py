from cmu_112_graphics import *
from nutritionReceiver import *
from nutritionCalc import *
from nutritionAndUserToCSV import *
import PIL

#main.py is the bulk of the project; it determines user interface and experience

def appStarted(app):
    app.homePage = True
    app.helpInfoPage = False
    app.userInfoPage = False
    app.trackPage = False
    app.mealPlanPage = False
    app.analyzePage = False
    app.foodEaten = None #stores user input of food eaten, initialized to None
    app.dayCalories = [] #lists calories for foods, will be summed, as will below lists
    app.dayCarbohydrates = []
    app.dayProtein = []
    app.dayFat = []
    app.dayFoods = [] #stores list of app.foodEaten
    app.userHeight = None
    app.userWeight = None
    app.userActivityLevel = None
    app.userGender = None
    app.userAge = None
    app.userWeightGoal = None
    app.dailyCalories = None #Total calories needed per day
    app.foodTypePreference = None
    app.antiFoodTypePreference = None
    app.breakfast = None
    app.snack1 = None
    app.lunch = None
    app.snack2 = None
    app.dinner = None
    app.mealCalories = 0
    app.mealCarbs = 0
    app.mealProtein = 0
    app.mealFat = 0
    app.preferenceCounter = 0
    app.weekData = None
    app.preCalsImage = app.loadImage('images/calories.png')
    app.calsImage = app.preCalsImage.transpose(Image.ROTATE_90)
    app.preGramsImage = app.loadImage('images/grams.png')
    app.gramsImage = app.preGramsImage.transpose(Image.ROTATE_90)

    app.lockedMeals = set()
    app.sortCalories = True
    app.sortCarbs = False
    app.sortProtein = False
    app.sortFat = False
    app.displayCalsPart = False

def keyPressed(app, event): #Saves user preference
    if event.key == '0': #Saves user information
        addUserData(app.userHeight, app.userWeight, app.userActivityLevel, app.userGender, app.userAge, app.userWeightGoal)
        
    elif event.key == '1': #reads in and loads user info
        userData = readUserData()
        app.userHeight = userData[0][0]
        app.userWeight = userData[0][1]
        app.userActivityLevel = userData[0][2]
        app.userGender = userData[0][3]
        app.userAge = userData[0][4]
        app.userWeightGoal = userData[0][5] 
    
    elif event.key == '5': #Shortcut key for some sample user data, does not account for date
        addFoodData(1999,220,110,75.4)
        addFoodData(2625,293,149,101)
        addFoodData(2984,338,185, 99)
        addFoodData(3013,270,170,145)

def mouseMoved(app, event):
    (mouseX, mouseY) = (event.x, event.y)
    if app.analyzePage == True:
        if mouseX >= .2*app.width and mouseX <= .9*app.width and mouseY >= .2*app.height and mouseY <=.8*app.height:
            app.displayCalsPart = True
        else:
            app.displayCalsPart = False
        

### Mouse Pressed Family ###

def mousePressed(app, event): #Wrapper for other mousePresseds
    if app.homePage == True:
        homeMousePressed(app, event)
    elif app.helpInfoPage == True:
        helpMousePressed(app, event)
    elif app.userInfoPage == True:
        userInfoMousePressed(app, event)
    elif app.trackPage == True:
        trackMousePressed(app, event)
    elif app.mealPlanPage == True:
        mealPlanMousePressed(app, event)
    elif app.analyzePage == True:
        analyzeMousePressed(app, event)


def homeMousePressed(app, event): #Home page
    (mouseX, mouseY) = (event.x, event.y) #Find mouse click position more easily
    if mouseX >= .4*app.width and mouseX <= .6*app.width and mouseY >= .45*app.height and mouseY <= .55*app.height: #Help page
        app.homePage = False
        app.helpInfoPage = True
        app.userInfoPage = False
        app.trackPage = False
        app.mealPlanPage = False

    elif mouseX >= .1*app.width and mouseX <= .3*app.width and mouseY >= .6*app.height and mouseY <= .8*app.height: #User info page
        app.homePage = False
        app.helpInfoPage = False
        app.userInfoPage = True
        app.trackPage = False
        app.mealPlanPage = False

    elif mouseX >= .4*app.width and mouseX <= .6*app.width and mouseY >= .6*app.height and mouseY <= .8*app.height: #Track page
        app.homePage = False
        app.helpInfoPage = False
        app.userInfoPage = False
        app.trackPage = True
        app.mealPlanPage = False
    
    elif mouseX >= .7*app.width and mouseX <= .9*app.width and mouseY >= .6*app.height and mouseY <= .8*app.height: #Meal plan page
        app.homePage = False
        app.helpInfoPage = False
        app.userInfoPage = False
        app.trackPage = False
        app.mealPlanPage = True

def helpMousePressed(app, event): 
    mouseX, mouseY = event.x, event.y
    if mouseX >=.85*app.width and mouseX <= app.width and mouseY >= 0 and mouseY <= .1*app.height:
        app.homePage = True
        app.helpInfoPage = False
        app.userInfoPage = False
        app.trackPage = False
        app.mealPlanPage = False
        app.analyzePage = False

def userInfoMousePressed(app, event):
    (mouseX, mouseY) = (event.x, event.y)
    if mouseX >= .85*app.width and mouseX <= app.width and mouseY >= 0 and mouseY <= .1*app.height:
        app.homePage = True
        app.helpInfoPage = False
        app.userInfoPage = False
        app.trackPage = False
        app.mealPlanPage = False
    elif mouseX >= .1*app.width and mouseX <= .30*app.width and mouseY >= .3*app.height and mouseY <= .4*app.height:
        app.userHeight = app.getUserInput("What is your height in inches?") #string result
    elif mouseX >= .1*app.width and mouseX <= .3*app.width and mouseY >= .45*app.height and mouseY <= .55*app.height:
        app.userWeight = app.getUserInput("What is your weight in lbs?") #string result
    elif mouseX >= .1*app.width and mouseX <= .30*app.width and mouseY >= .6*app.height and mouseY <= .7*app.height:
        app.userActivityLevel = app.getUserInput("Is your activity level: low, medium, or high?") #string result
    elif mouseX >= .1*app.width and mouseX <= .30*app.width and mouseY >= .75*app.height and mouseY <= .85*app.height:
        app.userGender = app.getUserInput("Are you: male or female?") #string result
    elif mouseX >= .1*app.width and mouseX <= .3*app.width and mouseY >= .9*app.height and mouseY <= .99*app.height:
        app.userAge = app.getUserInput("How old are you in years?")
    elif mouseX >= .55*app.width and mouseX <= .688*app.width and mouseY >= .35*app.height and mouseY <= .5*app.height:
        app.userWeightGoal = app.getUserInput("Do you want to: lose/maintain/gain weight?")
    elif mouseX >= .55*app.width and mouseX <= .688*app.width and mouseY >= .7*app.height and mouseY <= .85*app.height:
        app.dailyCalories = getDailyCalories(int(app.userHeight), int(app.userWeight), app.userActivityLevel, app.userGender, int(app.userAge), app.userWeightGoal)
        

def trackMousePressed(app, event):
    (mouseX, mouseY) = (event.x, event.y)
    if mouseX >= .85*app.width and mouseX <= app.width and mouseY >= 0 and mouseY <= .1*app.height:
        app.homePage = True
        app.helpInfoPage = False
        app.userInfoPage = False
        app.trackPage = False
        app.mealPlanPage = False
    elif mouseX >= .55*app.width and mouseX <= .85*app.width and mouseY >= .3*app.height and mouseY <= .45*app.height: #Add food
        app.foodEaten = app.getUserInput("What did you eat?") #prompt user info for food, run nutritionFacts, and display most recent and add to tally for each nutrient
        if (app.foodEaten != None) and (app.foodEaten != ''):
            (calories, carbohydrates, protein, fat) = nutritionFacts(app.foodEaten)
            app.dayFoods.append(app.foodEaten)
            app.dayCalories.append(calories)
            app.dayCarbohydrates.append(carbohydrates)
            app.dayProtein.append(protein)
            app.dayFat.append(fat)
    elif mouseX >= .55*app.width and mouseX <= .85*app.width and mouseY >= .5*app.height and mouseY <= .65*app.height: #Remove food
        if app.dayFoods != []: 
            app.dayFoods.pop() #must subtract nutrients too, use pop
            app.dayCalories.pop()
            app.dayCarbohydrates.pop()
            app.dayProtein.pop()
            app.dayFat.pop()
    elif mouseX >= .55*app.width and mouseX <= .85*app.width and mouseY >= .7*app.height and mouseY <= .85*app.height: #Analyze button
        app.homePage = False
        app.helpInfoPage = False
        app.userInfoPage = False
        app.trackPage = False
        app.mealPlanPage = False
        app.analyzePage = True
        
    elif (mouseX >= .7*app.width and mouseX <= .85*app.width and mouseY >= 0 and mouseY <= .1*app.height) and app.dayFoods != []: #Finish day
        addFoodData(sum(app.dayCalories), sum(app.dayCarbohydrates), sum(app.dayProtein), sum(app.dayFat)) #add summed elements
        app.dayCalories = [] 
        app.dayCarbohydrates = []
        app.dayProtein = []
        app.dayFat = []
        app.dayFoods = [] 
        

def mealPlanMousePressed(app, event):
    (mouseX, mouseY) = (event.x, event.y)
    if mouseX >= .85*app.width and mouseX <= app.width and mouseY >= 0 and mouseY <= .1*app.height:
        app.homePage = True
        app.helpInfoPage = False
        app.userInfoPage = False
        app.trackPage = False
        app.mealPlanPage = False
    elif mouseX >= .5*app.width and mouseX <= .8*app.width and mouseY >= .15*app.height and mouseY<= .2*app.height: #Food preference button
        app.foodTypePreference = app.getUserInput("Choose food preference: fruit, vegetable, grain, poultry, fish, dairy, or none")
        if app.foodTypePreference != None:
            app.foodTypePreference = app.foodTypePreference.lower()

    elif mouseX >= .5*app.width and mouseX <= .8*app.width and mouseY >= .2*app.height and mouseY <= .25*app.height: #Anti food preference button
        app.antiFoodTypePreference = app.getUserInput("Choose anti-food preference: fruit, vegetable, grain, poultry, fish, dairy, or none")
        if app.foodTypePreference != None:
            app.foodTypePreference = app.foodTypePreference.lower()
    
    #Clicking to lock and unlock each meal, imaginary boxes around foods, color the meal name if locked
    elif mouseX >= .25*app.width and mouseX <= .75*app.width and mouseY >= .32*app.height and mouseY < .38*app.height: #Breakfast
        if 'breakfast' in app.lockedMeals:
            app.lockedMeals.remove('breakfast')
        else:
            app.lockedMeals.add('breakfast')
    elif mouseX >= .25*app.width and mouseX <= .75*app.width and mouseY >= .42*app.height and mouseY < .48*app.height: #Snack1
        if 'snack1' in app.lockedMeals:
            app.lockedMeals.remove('snack1')
        else:
            app.lockedMeals.add('snack1')
    elif mouseX >= .25*app.width and mouseX <= .75*app.width and mouseY >= .52*app.height and mouseY < .58*app.height: #Lunch
        if 'lunch' in app.lockedMeals:
            app.lockedMeals.remove('lunch')
        else:
            app.lockedMeals.add('lunch')
    elif mouseX >= .25*app.width and mouseX <= .75*app.width and mouseY >= .62*app.height and mouseY < .68*app.height: #Snack2 
        if 'snack2' in app.lockedMeals:
            app.lockedMeals.remove('snack2')
        else:
            app.lockedMeals.add('snack2')
    elif mouseX >= .25*app.width and mouseX <= .75*app.width and mouseY >= .72*app.height and mouseY < .78*app.height: #Dinner
        if 'dinner' in app.lockedMeals:
            app.lockedMeals.remove('dinner')
        else:
            app.lockedMeals.add('dinner')

    elif mouseX >= .1*app.width and mouseX <= .4*app.width and mouseY >= .15*app.height and mouseY <= .25*app.height: #Meal Plan button
        app.mealCalories = 0
        app.mealCarbs = 0
        app.mealProtein = 0
        app.mealFat = 0
        app.preferenceCounter = 0
        if app.dailyCalories != None: 
            if (app.foodTypePreference == None or app.foodTypePreference == 'none') and (app.antiFoodTypePreference == None or app.antiFoodTypePreference == 'none'): 
                mealPlan(app, app.foodTypePreference, app.lockedMeals)
            elif ((app.foodTypePreference != None and app.foodTypePreference != 'none') and (app.antiFoodTypePreference == None or app.antiFoodTypePreference == 'none')):
                while app.preferenceCounter < 1:
                    app.mealCalories = 0
                    app.mealCarbs = 0
                    app.mealProtein = 0
                    app.mealFat = 0
                    app.preferenceCounter = 0
                    mealPlan(app, app.foodTypePreference, app.lockedMeals)   
            elif ((app.foodTypePreference == None or app.foodTypePreference == 'none') and (app.antiFoodTypePreference != None and app.antiFoodTypePreference != 'none')):
                mealPlan(app, app.antiFoodTypePreference, app.lockedMeals)
                while app.preferenceCounter != 0:
                    mealPlan(app, app.antiFoodTypePreference, app.lockedMeals)
                

def mealPlan(app, preference, lock): #Whole meal plan function, for meal plan page
    app.mealCalories = 0
    app.mealCarbs = 0
    app.mealProtein = 0
    app.mealFat = 0
    app.preferenceCounter = 0

    if 'breakfast' not in lock:
        app.breakfast = getMealPlan(breakfastList, preference, 2*app.dailyCalories/10)
    app.mealCalories += app.breakfast[1]
    app.mealCarbs += app.breakfast[2]
    app.mealProtein += app.breakfast[3]
    app.mealFat += app.breakfast[4]
    app.preferenceCounter += app.breakfast[5]

    if 'snack1' not in lock:
        app.snack1 = getMealPlan(snackList, preference, 1*app.dailyCalories/10)
    app.mealCalories += app.snack1[1]
    app.mealCarbs += app.snack1[2]
    app.mealProtein += app.snack1[3]
    app.mealFat += app.snack1[4]
    app.preferenceCounter += app.snack1[5]

    if 'lunch' not in lock:
        app.lunch = getMealPlan(lunchList, preference, 3*app.dailyCalories/10)
    app.mealCalories += app.lunch[1]
    app.mealCarbs += app.lunch[2]
    app.mealProtein += app.lunch[3]
    app.mealFat += app.lunch[4]
    app.preferenceCounter += app.lunch[5]
    
    if 'snack2' not in lock:
        app.snack2 = getMealPlan(snackList, preference, 1*app.dailyCalories/10)
    app.mealCalories += app.snack2[1]
    app.mealCarbs += app.snack2[2]
    app.mealProtein += app.snack2[3]
    app.mealFat += app.snack2[4]
    app.preferenceCounter += app.snack2[5]
        
    if 'dinner' not in lock:
        app.dinner = getMealPlan(dinnerList, preference, 3*app.dailyCalories/10)
    app.mealCalories += app.dinner[1]
    app.mealCarbs += app.dinner[2]
    app.mealProtein += app.dinner[3]
    app.mealFat += app.dinner[4]
    app.preferenceCounter += app.dinner[5]


def analyzeMousePressed(app, event): #Page where CSV is read and bar graphs created
    mouseX, mouseY = event.x, event.y
    if mouseX >=.85*app.width and mouseX <= app.width and mouseY >= 0 and mouseY <= .1*app.height:
        app.homePage = True
        app.helpInfoPage = False
        app.userInfoPage = False
        app.trackPage = False
        app.mealPlanPage = False
        app.analyzePage = False
    elif mouseX >= .05*app.width and mouseX <= .2*app.width and mouseY >= .85*app.height and mouseY <= .95*app.height: #Get Week
        app.weekData = readFoodData() 
    elif mouseX >= .05*app.width and mouseX <= .2*app.width and mouseY >= .05*app.height and mouseY <= .20*app.height:
        app.sortCalories = True
        app.sortCarbs = False
        app.sortProtein = False
        app.sortFat = False
    elif mouseX >= .25*app.width and mouseX <= .4 *app.width and mouseY >= .05*app.height and mouseY <= .20*app.height:
        app.sortCalories = False
        app.sortCarbs = True
        app.sortProtein = False
        app.sortFat = False       
    elif mouseX >= .45*app.width and mouseX <= .6 *app.width and mouseY >= .05*app.height and mouseY <= .20*app.height:
        app.sortCalories = False
        app.sortCarbs = False
        app.sortProtein = True
        app.sortFat = False
    elif mouseX >= .65*app.width and mouseX <= .8 *app.width and mouseY >= .05*app.height and mouseY <= .20*app.height:   
        app.sortCalories = False
        app.sortCarbs = False
        app.sortProtein = False
        app.sortFat = True

### Drawing Family ###

def drawHome(app, canvas):
    if app.homePage == True:
        
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "#f6c3ab")
        canvas.create_text(app.width/2, app.height/3, text="NutriLog", font= 'Times 50 bold') #Title
        canvas.create_rectangle(.4*app.width, .45*app.height, .6*app.width, .55*app.height, outline='white', fill='#82EEFD')
        canvas.create_text(app.width/2, app.height/2, text="Help Info", font="Times 35 bold") #Help 

        canvas.create_rectangle(.1*app.width, .6*app.height, .3*app.width, .8*app.height, outline="white")
        canvas.create_text(.2*app.width, .7*app.height, text="User Info", fill="black", font="Times 25 bold")
        canvas.create_rectangle(.4*app.width, .6*app.height, .6*app.width, .8*app.height, outline="white")
        canvas.create_text(.5*app.width, .7*app.height, text="Track", fill="black", font="Times 25 bold")
        canvas.create_rectangle(.7*app.width, .6*app.height, .9*app.width, .8*app.height, outline="white")
        canvas.create_text(.8*app.width, .7*app.height, text="Meal Plan", fill="black", font="Times 25 bold")


def drawHelpInfo(app, canvas):
    if app.helpInfoPage == True:
        canvas.create_rectangle(0, 0, app.width, app.height, fill="#e5ff99")
        canvas.create_rectangle(.85*app.width, 0, app.width, .1*app.height, outline='white')
        canvas.create_text(.925*app.width, .05*app.height, text='Home', font='Times 30 bold')

        canvas.create_text(.5*app.width, .10*app.height, text='Help Info', font='Times 40 bold')
        canvas.create_text(.5*app.width, .2*app.height, text='Click on boxes outlined in white', font='Times 23 bold')
        canvas.create_text(.5*app.width, .3*app.height, text='Set user info first, save it by pressing 0, load it by pressing 1', font='Times 23 bold')
        canvas.create_text(.5*app.width, .4*app.height, text='Add food until day has been completed, then press finish day', font='Times 23 bold')
        canvas.create_text(.5*app.width, .5*app.height, text="Review your week's progress in the Analyze section and sort by macronutrient" , font='Times 25 bold')
        canvas.create_text(.5*app.width, .6*app.height, text="Numbers on top of bars are the user's amount, percents in the bar indicate % out of total cals" , font='Times 23 bold')
        canvas.create_text(.5*app.width, .7*app.height, text="Numbers in bars are how many calories that macronutrient contributed to total calories" , font='Times 23 bold')
        canvas.create_text(.5*app.width, .8*app.height, text='Click for sample meal plans based on preference or anti-preference', font='Times 23 bold')
        canvas.create_text(.5*app.width, .9*app.height, text='Click on a meal to lock and unlock it', font='Times 23 bold')


def drawUserInfo(app, canvas):
    if app.userInfoPage == True:
        canvas.create_rectangle(0, 0, app.width, app.height, fill="#e5ff99")
        canvas.create_text(.5*app.width, .20*app.height, text='User Information', font='Times 45 bold')
        canvas.create_rectangle(.85*app.width, 0, app.width, .1*app.height, outline='white')
        canvas.create_text(.925*app.width, .05*app.height, text='Home', font='Times 30 bold')
        canvas.create_rectangle(.1*app.width, .3*app.height, .30*app.width, .4*app.height, outline='white')
        canvas.create_text(.2*app.width, .35*app.height, text='Change Height', font='Times 20 bold')
        if app.userHeight != None: #user height
            canvas.create_text(.4*app.width, .35*app.height, text=f'{int(app.userHeight)//12} feet {int(app.userHeight)%12} inches', font='Times 20 bold') 
        else:
            canvas.create_text(.4*app.width, .35*app.height, text='______________', font='Times 20 bold')
        canvas.create_rectangle(.1*app.width, .45*app.height, .30*app.width, .55*app.height, outline='white')
        canvas.create_text(.2*app.width, .5*app.height, text='Change Weight', font='Times 20 bold')
        if app.userWeight != None: #user weight
            canvas.create_text(.4*app.width, .5*app.height, text=f'{int(app.userWeight)} lbs', font='Times 20 bold') 
        else:
            canvas.create_text(.4*app.width, .5*app.height, text='______________', font='Times 20 bold')
        canvas.create_rectangle(.1*app.width, .6*app.height, .30*app.width, .70*app.height, outline='white')
        canvas.create_text(.2*app.width, .65*app.height, text='Activity Level', font='Times 20 bold')
        if app.userActivityLevel != None: #user activity level
            canvas.create_text(.4*app.width, .65*app.height, text=f'{app.userActivityLevel.lower()}', font='Times 20 bold') 
        else:
            canvas.create_text(.4*app.width, .65*app.height, text='______________', font='Times 20 bold')

        canvas.create_rectangle(.1*app.width, .75*app.height, .30*app.width, .85*app.height, outline='white')
        canvas.create_text(.2*app.width, .8*app.height, text='Changer Gender', font='Times 20 bold')
        if app.userGender != None: #user gender
            canvas.create_text(.4*app.width, .8*app.height, text=f'{app.userGender}', font='Times 20 bold')
        else:
            canvas.create_text(.4*app.width, .8*app.height, text='______________', font='Times 20 bold')

        canvas.create_rectangle(.1*app.width, .9*app.height, .30*app.width, .99*app.height, outline='white')
        canvas.create_text(.2*app.width, .945*app.height, text='Change Age', font='Times 20 bold')
        if app.userAge != None: #user age
            canvas.create_text(.4*app.width, .945*app.height, text=f'{int(app.userAge)} years', font='Times 20 bold')
        else:
            canvas.create_text(.4*app.width, .945*app.height, text='______________', font='Times 20 bold')


        canvas.create_text(.75*app.width, .3*app.height, text='Weight Goal', font='Times 25 bold')
        canvas.create_rectangle(.55*app.width, .35*app.height, .688*app.width, .5*app.height, outline='white')
        canvas.create_text(.62*app.width, .425*app.height, text='Change Goal', font='Times 20 bold')
        if app.userWeightGoal != None:
            canvas.create_text(.8*app.width, .425*app.height, text=f'{app.userWeightGoal}', font='Times 25 bold')
        else:
             canvas.create_text(.8*app.width, .425*app.height, text='___________', font='Times 25 bold')

        canvas.create_text(.75*app.width, .65*app.height, text='You need to eat...', font='Times 25 bold')
        canvas.create_rectangle(.55*app.width, .7*app.height, .688*app.width, .85*app.height, outline='white')
        canvas.create_text(.62*app.width, .775*app.height, text='Get Calories', font='Times 20 bold')
        if app.dailyCalories != None:
            canvas.create_text(.8*app.width, .775*app.height, text=f'{app.dailyCalories} calories', font='Times 25 bold')
        else:
            canvas.create_text(.8*app.width, .775*app.height, text='___________', font='Times 25 bold')


def drawTrack(app, canvas):
    if app.trackPage == True:
        canvas.create_rectangle(0, 0, app.width, app.height, fill="#e5ff99")
        canvas.create_rectangle(.85*app.width, 0, app.width, .1*app.height, outline='white')
        canvas.create_text(.5*app.width, .20*app.height, text='Track Food', font='Times 45 bold')
        canvas.create_text(.925*app.width, .05*app.height, text='Home', font='Times 30 bold')
        canvas.create_rectangle(.7*app.width, 0, .85*app.width, .1*app.height, outline='white')
        canvas.create_text(.775*app.width, .05*app.height, text='Finish Day', font='Times 25 bold')


        canvas.create_rectangle(.55*app.width, .30*app.height, .85*app.width, .45*app.height, outline='white')
        canvas.create_text(.7*app.width, .375*app.height, text='Add Food', font='Times 30 bold')
        canvas.create_rectangle(.55*app.width, .5*app.height, .85*app.width, .65*app.height, outline='white')
        canvas.create_text(.7*app.width, .575*app.height, text='Remove Last Food', font='Times 30 bold')
        canvas.create_rectangle(.55*app.width, .7*app.height, .85*app.width, .85*app.height, outline='white')
        canvas.create_text(.7*app.width, .775*app.height, text='Analyze', font='Times 30 bold')

        canvas.create_text(.25*app.width, .30*app.height, text='Most recent food:', font='Times 30 bold')
        if app.foodEaten != None:
            canvas.create_text(.25*app.width, .40*app.height, text='______________________', font='Times 25')
            if app.dayFoods == []:
                canvas.create_text(.25*app.width, .40*app.height, text='______________________', font='Times 25')
            else:
                canvas.create_text(.25*app.width, .39*app.height, text=app.dayFoods[-1], font='Times 25')
        elif app.foodEaten == None:
            canvas.create_text(.25*app.width, .40*app.height, text='______________________', font='Times 25')

        canvas.create_text(.25*app.width, .5*app.height, text="Day's Nutrition", font='Times 30 bold')
        canvas.create_text(.05*app.width, .6*app.height, text="Calories:", font='Times 20 bold', anchor=W)
        canvas.create_text(.05*app.width, .7*app.height, text="Carbohydrates:", font='Times 20 bold', anchor=W)
        canvas.create_text(.05*app.width, .8*app.height, text="Protein:", font='Times 20 bold', anchor=W)
        canvas.create_text(.05*app.width, .9*app.height, text="Fat:", font='Times 20 bold', anchor=W)
        if app.dayCalories == 0:
            canvas.create_text(.3*app.width, .6*app.height, text="0 calories", font='Times 20 bold')
            canvas.create_text(.3*app.width, .7*app.height, text="0 grams", font='Times 20 bold')
            canvas.create_text(.3*app.width, .8*app.height, text="0 grams", font='Times 20 bold')
            canvas.create_text(.3*app.width, .9*app.height, text="0 grams", font='Times 20 bold')
        elif app.dayCalories != 0:
            canvas.create_text(.3*app.width, .6*app.height, text=str(round(sum(app.dayCalories), 1))+" calories", font='Times 20 bold')
            canvas.create_text(.3*app.width, .7*app.height, text=str(round(sum(app.dayCarbohydrates), 1))+" grams", font='Times 20 bold')
            canvas.create_text(.3*app.width, .8*app.height, text=str(round(sum(app.dayProtein), 1))+" grams", font='Times 20 bold')
            canvas.create_text(.3*app.width, .9*app.height, text=str(round(sum(app.dayFat), 1))+" grams", font='Times 20 bold')


def drawMealPlan(app, canvas):
    if app.mealPlanPage == True:
        canvas.create_rectangle(0, 0, app.width, app.height, fill="#e5ff99")
        canvas.create_rectangle(.85*app.width, 0, app.width, .1*app.height, outline='white')
        canvas.create_text(.925*app.width, .05*app.height, text='Home', font='Times 30 bold')
        canvas.create_text(.5*app.width, .1*app.height, text='Custom Meal Plan', font='Times 30 bold')
        canvas.create_rectangle(.10*app.width, .15*app.height, .40*app.width, .25*app.height, outline='white')
        canvas.create_text(.25*app.width, .2*app.height, text='Click for free meal plan!', font='Times 20 bold')
        canvas.create_rectangle(.5*app.width, .15*app.height, .8*app.width, .20*app.height, outline='white')
        canvas.create_text(.65*app.width, .175*app.height, text='Choose food type preference', font='Times 20 bold')
        canvas.create_rectangle(.5*app.width, .2*app.height, .8*app.width, .25*app.height, outline='white')
        canvas.create_text(.65*app.width, .225*app.height, text='Choose anti-preference', font='Times 20 bold')

        if app.foodTypePreference != None:
            canvas.create_text(.90*app.width, .175*app.height, text=app.foodTypePreference, font='Times 20 bold')
        else:
            canvas.create_text(.90*app.width, .175*app.height, text='_______________', font='Times 20 bold')

        if app.antiFoodTypePreference != None:
            canvas.create_text(.90*app.width, .225*app.height, text=app.antiFoodTypePreference, font='Times 20 bold')
        else:
            canvas.create_text(.90*app.width, .225*app.height, text='_______________', font='Times 20 bold')
        if 'breakfast' in app.lockedMeals:
            canvas.create_text(.1*app.width, .35*app.height, text="Breakfast:", font='Times 20 bold', fill='#FA8128') #orange
        elif 'breakfast' not in app.lockedMeals:
            canvas.create_text(.1*app.width, .35*app.height, text="Breakfast:", font='Times 20 bold')
        if app.breakfast != None: 
            canvas.create_text(.6*app.width, .35*app.height, text=', '.join(app.breakfast[0]), font='Times 19 bold')
        if 'snack1' in app.lockedMeals:
            canvas.create_text(.1*app.width, .45*app.height, text="Snack 1:", font='Times 20 bold', fill='#FA8128')
        elif 'snack1' not in app.lockedMeals:
            canvas.create_text(.1*app.width, .45*app.height, text="Snack 1:", font='Times 20 bold')
        if app.snack1 != None:
            canvas.create_text(.6*app.width, .45*app.height, text=', '.join(app.snack1[0]), font='Times 19 bold')
        if 'lunch' in app.lockedMeals:
            canvas.create_text(.1*app.width, .55*app.height, text="Lunch:", font='Times 20 bold', fill='#FA8128')
        elif 'lunch' not in app.lockedMeals:
            canvas.create_text(.1*app.width, .55*app.height, text="Lunch:", font='Times 20 bold')
        if app.lunch != None:
            canvas.create_text(.6*app.width, .55*app.height, text=', '.join(app.lunch[0]), font='Times 19 bold')
        if 'snack2' in app.lockedMeals:
            canvas.create_text(.1*app.width, .65*app.height, text="Snack 2:", font='Times 20 bold', fill='#FA8128')
        elif 'snack2' not in app.lockedMeals:
            canvas.create_text(.1*app.width, .65*app.height, text="Snack 2:", font='Times 20 bold')
        if app.snack2 != None:
            canvas.create_text(.6*app.width, .65*app.height, text=', '.join(app.snack2[0]), font='Times 19 bold')
        if 'dinner' in app.lockedMeals:
            canvas.create_text(.1*app.width, .75*app.height, text="Dinner:", font='Times 20 bold', fill='#FA8128')
        elif 'dinner' not in app.lockedMeals:
            canvas.create_text(.1*app.width, .75*app.height, text="Dinner:", font='Times 20 bold')
        if app.dinner != None:
            canvas.create_text(.6*app.width, .75*app.height, text=', '.join(app.dinner[0]), font='Times 19 bold')

        canvas.create_line(0, .8*app.height, app.width, .8*app.height, fill='black')
        canvas.create_text(.1*app.width, .9*app.height, text="Day's Total:", font='Times 20 bold')
        if app.mealCalories != 0:
            canvas.create_text(.6*app.width, .9*app.height, text=f'{round(app.mealCalories, 1)} calories, {round(app.mealCarbs, 1)} g carbohydrates, {round(app.mealProtein, 1)} g protein, {round(app.mealFat, 1)} g fat',
            font='Times 20 bold')
        
def drawAnalyze(app, canvas):
    if app.analyzePage == True:
        
        canvas.create_rectangle(0, 0, app.width, app.height, fill="#e5ff99")
        canvas.create_rectangle(.85*app.width, 0, app.width, .1*app.height, outline='white')
        canvas.create_text(.925*app.width, .05*app.height, text='Home', font='Times 30 bold')

        canvas.create_rectangle(.05*app.width, .05*app.height, .2*app.width, .15*app.height, outline='white')
        canvas.create_text(.125*app.width, .1*app.height, text='Calories', font='Times 25')

        canvas.create_rectangle(.25*app.width, .05*app.height, .40*app.width, .15*app.height, outline='white')
        canvas.create_text(.325*app.width, .1*app.height, text='Carbohydrates', font='Times 25')

        canvas.create_rectangle(.45*app.width, .05*app.height, .6*app.width, .15*app.height, outline='white')
        canvas.create_text(.525*app.width, .1*app.height, text='Protein', font='Times 25')

        canvas.create_rectangle(.65*app.width, .05*app.height, .8*app.width, .15*app.height, outline='white')
        canvas.create_text(.725*app.width, .1*app.height, text='Fat', font='Times 25')

        canvas.create_rectangle(.05*app.width, .85*app.height, .2*app.width, .95*app.height, outline='white')
        canvas.create_text(.125*app.width, .9*app.height, text='Get Data', font='Times 25')

        if app.sortCalories == True:
            sortCalories(app, canvas)
        
        elif app.sortCarbs == True:
            sortCarbs(app, canvas)

        elif app.sortProtein == True:
            sortProtein(app, canvas)

        elif app.sortFat == True:
            sortFat(app, canvas)

def keyChart(app, canvas):
    #Key for colors
    canvas.create_rectangle(.85*app.width, .15*app.height, .88*app.width, .18*app.height, fill='#B7E9F7')
    canvas.create_text(.89*app.width, .165*app.height, text='Too low', font='Times 15', anchor=W)
    canvas.create_rectangle(.85*app.width, .20*app.height, .88*app.width, .23*app.height, fill='#29b6f6')
    canvas.create_text(.89*app.width, .215*app.height, text='Perfect', font='Times 15', anchor=W)
    canvas.create_rectangle(.85*app.width, .25*app.height, .88*app.width, .28*app.height, fill='#FF2800')
    canvas.create_text(.89*app.width, .265*app.height, text='Too much', font='Times 15', anchor=W)

def sortFat(app, canvas):
    #y-axis
    canvas.create_line(.2*app.width, .20*app.height, .2*app.width, .80*app.height, width=2)
    canvas.create_line(.19*app.width, .7*app.height, .21*app.width, .7*app.height, width=1)
    canvas.create_text(.15*app.width, .7*app.height, text='25', font='Times 20 bold')
    canvas.create_line(.19*app.width, .6*app.height, .21*app.width, .6*app.height, width=1)
    canvas.create_text(.15*app.width, .6*app.height, text='50', font='Times 20 bold')
    canvas.create_line(.19*app.width, .5*app.height, .21*app.width, .5*app.height, width=1)
    canvas.create_text(.15*app.width, .5*app.height, text='75', font='Times 20 bold')
    canvas.create_line(.19*app.width, .4*app.height, .21*app.width, .4*app.height, width=1)
    canvas.create_text(.15*app.width, .4*app.height, text='100', font='Times 20 bold')
    canvas.create_line(.19*app.width, .3*app.height, .21*app.width, .3*app.height, width=1)
    canvas.create_text(.15*app.width, .3*app.height, text='125', font='Times 20 bold')
    #y-axis title: 'grams'
    canvas.create_image(.075*app.width, .5*app.height, image=ImageTk.PhotoImage(app.gramsImage))
    
    #x-axis
    canvas.create_line(.2*app.width, .8*app.height, .9*app.width, .8*app.height, width=2)
    canvas.create_line(.286*app.width, .79*app.height, .286*app.width, .81*app.height, width=1)
    canvas.create_line(.371*app.width, .79*app.height, .371*app.width, .81*app.height, width=1)
    canvas.create_line(.457*app.width, .79*app.height, .457*app.width, .81*app.height, width=1)
    canvas.create_line(.543*app.width, .79*app.height, .543*app.width, .81*app.height, width=1)
    canvas.create_line(.629*app.width, .79*app.height, .629*app.width, .81*app.height, width=1)
    canvas.create_line(.714*app.width, .79*app.height, .714*app.width, .81*app.height, width=1)
    canvas.create_line(.8*app.width, .79*app.height, .8*app.width, .81*app.height, width=1)
    canvas.create_text(.5*app.width, .92*app.height, text='Day', font='Times 25 bold')

    canvas.create_text(.5*app.width, .18*app.height, text='Fat', font='Times 25 bold')
    if (app.weekData != None) and (app.dailyCalories != None):
        drawFatBars(app, canvas, app.weekData, len(app.weekData))

    keyChart(app, canvas)

#Macronutrient percent ranges taken from
#https://www.healthline.com/nutrition/best-macronutrient-ratio#bottom-line
def drawFatBars(app, canvas, weekData, numOfBars):
    leftX = 0.2577*app.width #left x-point
    rightX = .2577*app.width + 2*.085*app.width/3 #right x-point
    leftHeight = .8*app.height
    rightHeight = .8*app.height
    axisTextX = .286*app.width
    axisTextY = .83*app.height
    middleTextX = .286*app.width
    
    for i in range(numOfBars): #loop through numOfBars and draw bars
        calorieHeight = (float(app.weekData[i][3])/125/2*app.height)
        canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight)
        canvas.create_text(middleTextX, .8*app.height - calorieHeight - .02*app.height, text=f'{round(float(app.weekData[i][3]), 1)}', font='Times 15')
        canvas.create_text(axisTextX, axisTextY, text=f'{app.weekData[i][4]}', font='Times 18 bold')
        percent = round((float(app.weekData[i][3])*9/app.dailyCalories) * 100, 2)
        if percent < 25:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#B7E9F7')
        elif 25 <= percent <= 35:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#29b6f6')
        else:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#FF2800')
        canvas.create_text(middleTextX, (.8*app.height - (calorieHeight/2)), text=f'{percent}%', font='Times 15')
        if app.displayCalsPart == True:
            canvas.create_text(middleTextX, (.8*app.height - (calorieHeight/4)), text=f'{round(float(app.weekData[i][3])*9, 1)}', font='Times 15')
        leftX += .085*app.width
        rightX += 2*.085*app.width/2
        axisTextX += .085*app.width
        middleTextX += .085*app.width


def sortProtein(app, canvas):
    #y-axis
    canvas.create_line(.2*app.width, .20*app.height, .2*app.width, .80*app.height, width=2)
    canvas.create_line(.19*app.width, .7*app.height, .21*app.width, .7*app.height, width=1)
    canvas.create_text(.15*app.width, .7*app.height, text='40', font='Times 20 bold')
    canvas.create_line(.19*app.width, .6*app.height, .21*app.width, .6*app.height, width=1)
    canvas.create_text(.15*app.width, .6*app.height, text='80', font='Times 20 bold')
    canvas.create_line(.19*app.width, .5*app.height, .21*app.width, .5*app.height, width=1)
    canvas.create_text(.15*app.width, .5*app.height, text='120', font='Times 20 bold')
    canvas.create_line(.19*app.width, .4*app.height, .21*app.width, .4*app.height, width=1)
    canvas.create_text(.15*app.width, .4*app.height, text='160', font='Times 20 bold')
    canvas.create_line(.19*app.width, .3*app.height, .21*app.width, .3*app.height, width=1)
    canvas.create_text(.15*app.width, .3*app.height, text='200', font='Times 20 bold')
    #y-axis title: 'grams'
    canvas.create_image(.075*app.width, .5*app.height, image=ImageTk.PhotoImage(app.gramsImage))
    
    #x-axis
    canvas.create_line(.2*app.width, .8*app.height, .9*app.width, .8*app.height, width=2)
    canvas.create_line(.286*app.width, .79*app.height, .286*app.width, .81*app.height, width=1)
    canvas.create_line(.371*app.width, .79*app.height, .371*app.width, .81*app.height, width=1)
    canvas.create_line(.457*app.width, .79*app.height, .457*app.width, .81*app.height, width=1)
    canvas.create_line(.543*app.width, .79*app.height, .543*app.width, .81*app.height, width=1)
    canvas.create_line(.629*app.width, .79*app.height, .629*app.width, .81*app.height, width=1)
    canvas.create_line(.714*app.width, .79*app.height, .714*app.width, .81*app.height, width=1)
    canvas.create_line(.8*app.width, .79*app.height, .8*app.width, .81*app.height, width=1)
    canvas.create_text(.5*app.width, .92*app.height, text='Day', font='Times 25 bold')

    canvas.create_text(.5*app.width, .18*app.height, text='Protein', font='Times 25 bold')
    if (app.weekData != None) and (app.dailyCalories != None):
        drawProteinBars(app, canvas, app.weekData, len(app.weekData))

    keyChart(app, canvas)


#Percent numbers taken from: https://www.healthline.com/nutrition/best-macronutrient-ratio#bottom-line
def drawProteinBars(app, canvas, weekData, numOfBars):
    leftX = 0.2577*app.width #left x-point
    rightX = .2577*app.width + 2*.085*app.width/3 #right x-point
    leftHeight = .8*app.height
    rightHeight = .8*app.height
    axisTextX = .286*app.width
    axisTextY = .83*app.height
    middleTextX = .286*app.width
    
    for i in range(numOfBars): #loop through numOfBars and draw bars
        calorieHeight = (float(app.weekData[i][2])/200/2*app.height)
        canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight)
        canvas.create_text(middleTextX, .8*app.height - calorieHeight - .02*app.height, text=f'{round(float(app.weekData[i][2]), 1)}', font='Times 15')
        canvas.create_text(axisTextX, axisTextY, text=f'{app.weekData[i][4]}', font='Times 18 bold')
        percent = round((float(app.weekData[i][2])*4/app.dailyCalories) * 100, 2)
        if percent < 10:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#B7E9F7')
        elif 10 <= percent <= 35:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#29b6f6')
        else:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#FF2800')
        canvas.create_text(middleTextX, (.8*app.height - (calorieHeight/2)), text=f'{percent}%', font='Times 15')
        if app.displayCalsPart == True:
            canvas.create_text(middleTextX, (.8*app.height - (calorieHeight/4)), text=f'{round(float(app.weekData[i][2])*4, 1)}', font='Times 15')
        leftX += .085*app.width
        rightX += 2*.085*app.width/2
        axisTextX += .085*app.width
        middleTextX += .085*app.width

def sortCarbs(app, canvas):
    #y-axis
    canvas.create_line(.2*app.width, .20*app.height, .2*app.width, .80*app.height, width=2)
    canvas.create_line(.19*app.width, .7*app.height, .21*app.width, .7*app.height, width=1)
    canvas.create_text(.15*app.width, .7*app.height, text='80', font='Times 20 bold')
    canvas.create_line(.19*app.width, .6*app.height, .21*app.width, .6*app.height, width=1)
    canvas.create_text(.15*app.width, .6*app.height, text='160', font='Times 20 bold')
    canvas.create_line(.19*app.width, .5*app.height, .21*app.width, .5*app.height, width=1)
    canvas.create_text(.15*app.width, .5*app.height, text='240', font='Times 20 bold')
    canvas.create_line(.19*app.width, .4*app.height, .21*app.width, .4*app.height, width=1)
    canvas.create_text(.15*app.width, .4*app.height, text='320', font='Times 20 bold')
    canvas.create_line(.19*app.width, .3*app.height, .21*app.width, .3*app.height, width=1)
    canvas.create_text(.15*app.width, .3*app.height, text='400', font='Times 20 bold')
    #y-axis title: 'grams'
    canvas.create_image(.075*app.width, .5*app.height, image=ImageTk.PhotoImage(app.gramsImage))
    
    #x-axis
    canvas.create_line(.2*app.width, .8*app.height, .9*app.width, .8*app.height, width=2)
    canvas.create_line(.286*app.width, .79*app.height, .286*app.width, .81*app.height, width=1)
    canvas.create_line(.371*app.width, .79*app.height, .371*app.width, .81*app.height, width=1)
    canvas.create_line(.457*app.width, .79*app.height, .457*app.width, .81*app.height, width=1)
    canvas.create_line(.543*app.width, .79*app.height, .543*app.width, .81*app.height, width=1)
    canvas.create_line(.629*app.width, .79*app.height, .629*app.width, .81*app.height, width=1)
    canvas.create_line(.714*app.width, .79*app.height, .714*app.width, .81*app.height, width=1)
    canvas.create_line(.8*app.width, .79*app.height, .8*app.width, .81*app.height, width=1)
    canvas.create_text(.5*app.width, .92*app.height, text='Day', font='Times 25 bold')

    canvas.create_text(.5*app.width, .18*app.height, text='Carbohydrates', font='Times 25 bold')
    if (app.weekData != None) and (app.dailyCalories != None):
        drawCarbBars(app, canvas, app.weekData, len(app.weekData))
    keyChart(app, canvas)
    
#Percent numbers taken from: https://www.healthline.com/nutrition/best-macronutrient-ratio#bottom-line
def drawCarbBars(app, canvas, weekData, numOfBars):
    leftX = 0.2577*app.width #left x-point
    rightX = .2577*app.width + 2*.085*app.width/3 #right x-point
    leftHeight = .8*app.height
    rightHeight = .8*app.height
    axisTextX = .286*app.width
    axisTextY = .83*app.height
    middleTextX = .286*app.width
    
    for i in range(numOfBars): #loop through numOfBars and draw bars
        calorieHeight = (float(app.weekData[i][1])/400/2*app.height)
        canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight)
        canvas.create_text(middleTextX, .8*app.height - calorieHeight - .02*app.height, text=f'{round(float(app.weekData[i][1]), 1)}', font='Times 15')
        canvas.create_text(axisTextX, axisTextY, text=f'{app.weekData[i][4]}', font='Times 18 bold')
        percent = round((float(app.weekData[i][1])*4/app.dailyCalories) * 100, 2)
        if percent < 45:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#B7E9F7')
        elif 45 <= percent <= 65:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#29b6f6')
        else:
            canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#FF2800')
        canvas.create_text(middleTextX, (.8*app.height - (calorieHeight/2)), text=f'{percent}%', font='Times 15')
        if app.displayCalsPart == True:
            canvas.create_text(middleTextX, (.8*app.height - (calorieHeight/4)), text=f'{round(float(app.weekData[i][1])*4, 1)}', font='Times 15')
        leftX += .085*app.width
        rightX += 2*.085*app.width/2
        axisTextX += .085*app.width
        middleTextX += .085*app.width

def sortCalories(app, canvas):
    #y-axis
    canvas.create_line(.2*app.width, .20*app.height, .2*app.width, .80*app.height, width=2)
    canvas.create_line(.19*app.width, .7*app.height, .21*app.width, .7*app.height, width=1)
    canvas.create_text(.15*app.width, .7*app.height, text='700', font='Times 20 bold')
    canvas.create_line(.19*app.width, .6*app.height, .21*app.width, .6*app.height, width=1)
    canvas.create_text(.15*app.width, .6*app.height, text='1400', font='Times 20 bold')
    canvas.create_line(.19*app.width, .5*app.height, .21*app.width, .5*app.height, width=1)
    canvas.create_text(.15*app.width, .5*app.height, text='2100', font='Times 20 bold')
    canvas.create_line(.19*app.width, .4*app.height, .21*app.width, .4*app.height, width=1)
    canvas.create_text(.15*app.width, .4*app.height, text='2800', font='Times 20 bold')
    canvas.create_line(.19*app.width, .3*app.height, .21*app.width, .3*app.height, width=1)
    canvas.create_text(.15*app.width, .3*app.height, text='3500', font='Times 20 bold')
    #y-axis title: 'calories'
    canvas.create_image(.075*app.width, .5*app.height, image=ImageTk.PhotoImage(app.calsImage))
    
    #x-axis
    canvas.create_line(.2*app.width, .8*app.height, .9*app.width, .8*app.height, width=2)
    canvas.create_line(.286*app.width, .79*app.height, .286*app.width, .81*app.height, width=1)
    canvas.create_line(.371*app.width, .79*app.height, .371*app.width, .81*app.height, width=1)
    canvas.create_line(.457*app.width, .79*app.height, .457*app.width, .81*app.height, width=1)
    canvas.create_line(.543*app.width, .79*app.height, .543*app.width, .81*app.height, width=1)
    canvas.create_line(.629*app.width, .79*app.height, .629*app.width, .81*app.height, width=1)
    canvas.create_line(.714*app.width, .79*app.height, .714*app.width, .81*app.height, width=1)
    canvas.create_line(.8*app.width, .79*app.height, .8*app.width, .81*app.height, width=1)
    canvas.create_text(.5*app.width, .92*app.height, text='Day', font='Times 25 bold')
    if (app.weekData != None) and (app.dailyCalories != None):
        drawCalorieBars(app, canvas, app.weekData, len(app.weekData))
    canvas.create_text(.5*app.width, .2*app.height, text=f'{app.dailyCalories} cals/day', font='Times 20 bold')

    keyChart(app, canvas)

def drawCalorieBars(app, canvas, weekData, numOfBars): #Draws bars from user data
    leftX = 0.2577*app.width #left x-point
    rightX = .2577*app.width + 2*.085*app.width/3 #right x-point
    leftHeight = .8*app.height
    rightHeight = .8*app.height
    axisTextX = .286*app.width
    axisTextY = .83*app.height
    middleTextX = .286*app.width
    
    for i in range(numOfBars): #loop through numOfBars and draw bars
        calorieHeight = (float(app.weekData[i][0])/3500/2*app.height)
        canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight)
        canvas.create_text(middleTextX, .8*app.height - calorieHeight - .02*app.height, text=f'{app.weekData[i][0]}', font='Times 15')
        canvas.create_text(axisTextX, axisTextY, text=f'{app.weekData[i][4]}', font='Times 18 bold')
        if app.dailyCalories != None:
            percent = round((float(app.weekData[i][0])/app.dailyCalories) * 100, 2)
            if percent < 95:
                canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#B7E9F7')
            elif 95 <= percent <= 105:
                canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#29b6f6')
            else:
                canvas.create_rectangle(leftX, leftHeight - calorieHeight, rightX, rightHeight, fill='#FF2800')
            canvas.create_text(middleTextX, (.8*app.height - (calorieHeight/2)), text=f'{percent}%', font='Times 15')
            middleTextX += .085*app.width
        leftX += .085*app.width
        rightX += 2*.085*app.width/2
        axisTextX += .085*app.width
            

def redrawAll(app, canvas):
    drawHome(app, canvas)
    drawHelpInfo(app, canvas)
    drawUserInfo(app, canvas) 
    drawTrack(app, canvas) 
    drawMealPlan(app, canvas)
    drawAnalyze(app, canvas)

runApp(width=1300, height=800)