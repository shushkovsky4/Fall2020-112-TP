import random

#nutritionCalc.py determines the user's caloric needs and randomizes the user's 
#developed meal plan

#Formula for Basal Metabolic Rate taken from
#https://www.thecalculatorsite.com/articles/health/bmr-formula.php#Known 
# Known as the Mifflin - St Jeor formula

def getDailyCalories(height, weight, activity, gender, age, goal):
    dailyCalories = 0
    if gender == 'male':
        dailyCalories = (4.536 * weight) + (15.88 * height) - (5 * age) + 5
    elif gender == 'female':
        dailyCalories = (4.536 * weight) + (15.88 * height) - (5 * age) - 161
    if activity == 'low':
        dailyCalories *= 1.2
    elif activity == 'medium':
        dailyCalories *= 1.55
    elif activity == 'high':
        dailyCalories *= 1.725
    if goal == 'lose':
        dailyCalories -= 500
    elif goal == 'gain':
        dailyCalories += 500
    return int(dailyCalories)

#Takes in meal list, preference for type of food, and needed number of calories 
def getMealPlan(mealList, preference, neededCalories): 
    preferenceCounter = 0 
    foodNumsUsed = set()
    resultMeal = []
    mealCalories = 0
    mealCarbs = 0
    mealProtein = 0
    mealFat = 0
    while mealCalories < (neededCalories - 50): #allow for some leeway with adding final food/calories
        foodIndex = random.randint(0, len(mealList) - 1)
        if (foodIndex not in foodNumsUsed):
            resultMeal.append(mealList[foodIndex][0])
            mealCalories += mealList[foodIndex][2]
            mealCarbs += mealList[foodIndex][3]
            mealProtein += mealList[foodIndex][4]
            mealFat += mealList[foodIndex][5]
            foodNumsUsed.add(foodIndex) #prevents repeat of same food
            if preference in mealList[foodIndex][1]: #check to see if food is of user preference
                preferenceCounter += 1
    if (mealCalories > (neededCalories + 75) or (len(resultMeal) > 2)): #final check, if calories > needed, recall function
       return getMealPlan(mealList, preference, neededCalories) 
    return list((resultMeal, mealCalories, mealCarbs, mealProtein, mealFat, preferenceCounter)) 


#Breakfast Database
#Food, [general types of food] --> (fruit,vegetable, grain, poultry, fish, dairy), calories, carbs, protein, fat
breakfastList = [ ['Bacon egg cheese sandwich', ['grain', 'dairy'], 430, 30, 24, 23], ['Plain bagel With cream cheese', ['grain'], 379, 57, 13, 11],
                  ['Banana', ['fruit'], 105, 27, 1.3, 0.4], ['Honey nut cheerios with reduced fat milk', ['grain', 'dairy'], 524, 83, 22.2, 13.5], 
                  ['4 large scrambled eggs with shredded cheese', ['dairy'], 542.5, 2.9, 36, 41.3], ['Croissant', ['grain'], 272, 31, 5.5, 14], 
                  ['1 cup oatmeal', ['grain'], 166, 28, 5.9, 3.6], ['Fruit parfait with 2 cups orange juice', ['fruit', 'dairy'], 362, 74, 11.7, 3.5], 
                  ['3 Eggo waffles and 2 cups of apple juice', ['grain', 'fruit'], 438, 96.5, 6.5, 4.4], ['Blueberry muffin', ['grain', 'fruit'], 424, 60, 5.1, 18],
                  ['Avocado toast', ['grain', 'fruit'], 189, 20, 3.8, 11], ['Acai bowl', ['fruit', 'grain'], 553, 86, 8.3, 24],
                  ['Yogurt granola parfait', ['grain, fruit'], 250, 48, 10, 3], ['French toast with an English muffin', ['grain'], 505, 71, 10.9, 20],
                  ['4 rice cakes and handful of baby carrots', ['grain', 'fruit'], 175, 37.4, 3.6, 1.1], ['Breakfast fajita burrito', ['grain', 'poultry', 'dairy'], 528, 36, 36, 25],
                  ['Peanut butter banana smoothie', ['dairy', 'fruit'], 599, 64, 21, 33]
                ]

#Snack Database
snackList = [ ['2 handfuls of cashews', ['grain'], 225, 12.8, 6, 18.3], ['Cliff bar chocolate chip', ['grain'], 250, 45, 9, 5],
              ['Apple', ['fruit'], 95, 25, 0.5, 0.3], ['Spinach', ['vegetable'], 41, 6.8, 5.3, 0.5], 
              ['1 chobani yogurt and handful of blueberries', ['dairy'], 143, 23, 12.3, 0.2], ['1 cup edamame', ['vegetable'], 188, 13.8, 18.4, 8],
              ['Beef jerky', ['poultry'], 232, 6.2, 18.8, 14.6], ['Half cup trail mix', ['grain'], 353, 33, 10, 23],
              ['Fruit yogurt smoothie', ['dairy', 'fruit'], 237, 45, 10, 2.7], ['Protein bar', ['dairy'], 211, 21, 20, 5.2],
              ['Canned tuna', ['fish'], 220, 0, 41, 5.1], ['3 boiled eggs', ['dairy'], 234, 1.7, 18.9, 15.9],
              ['Potato chips', ['grain'], 149, 15, 1.8, 9.5], ['Handful of macademia nuts', ['grain'], 204, 3.9, 2.2, 21],
              ['1 cup chickpeas', ['grain'], 269, 45, 15, 4.2], ['Pita chips', ['grain'], 260, 38, 6.6, 8.6],
              ['Half cup of dried fruit', ['fruit'], 220, 58, 2.2, 0.5], ['1.5 oz dark chocolate', ['dairy'], 232.5, 25.5, 2.1, 13.4],
              ['Banana chips', ['fruit'], 294, 34, 1.3, 19], ['2 cups dry honey cheerios', ['grain'], 280, 60, 6.6, 3.8],
              ['Handful tortilla chips', ['grain'], 126, 18, 1.9, 5.6], ['Banana smoothie', ['fruit', 'dairy'], 176, 37, 4.5, 2.2]
            ]

#Lunch Database
lunchList = [ ['1 cup macaroni and cheese, caesar salad', ['vegetables', 'grain', 'dairy'], 857, 70, 19.7, 56], ['2 bowls chicken soup and baguette slice with butter', ['poultry', 'grain', 'dairy'], 582, 74, 24.6, 21.6],
              ['2 bowls tomato soup', ['fruit'], 340, 72, 7, 2.2], ['Grilled chicken sandwich, 2 cups rigatoni pasta and cut plum', ['grain', 'poultry', 'fruit'], 769, 108.9, 52.2, 13.1],
              ['BLT pasta salad and 1 cup of quinoa rice', ['poultry, vegetable, grain'], 653, 80, 21.2, 60], ['5 falafel balls with hummus in pita bread with a clementine', ['grain', 'fruit'], 815, 77.6, 21, 48.9], 
              ['Fried chicken and half a cup of brown rice', ['poultry', 'grain'], 486, 27.4, 42.3, 21.8], ['Chicken curry and 1 cup black beans', ['grain'], 503, 53.5, 44, 12],
              ['Turkey pot pie', ['grain', 'poultry'], 699, 35, 70, 26], ['2 and a half cups pad thai', ['grain', 'poultry', 'dairy', 'vegetable'], 796.1, 43.7, 60.8, 42.8],
              ['6 oz pork loin and 1.5 cups brown rice with shredded cheese', ['dairy, grain', 'poultry'], 881, 70.7, 63.9, 36.2], ['Peanut butter and jelly sandwhich', ['grain'], 378, 46, 12, 18],
              ['2 slices of buffalo chicken pizza and celery', ['grain', 'vegetable', 'poultry'], 734, 76, 35.4, 32.4], ['Ham and cheese sandwich with sliced avocado', ['grain', 'poultry', 'vegetable'], 839, 45, 32, 61],
              ['Veggie wraps and half a cup of spaghetti', ['vegetable', 'grain'], 519, 76.6, 20.5, 19.7], ['Beef shawarma sandwich', ['grain', 'poultry'], 773, 58, 78, 24],
              ['1 chicken leg, 2 Greek yogurts, 1 banana', ['dairy', 'poultry', 'fruit'], 848, 43, 110, 31.1], ['1 chicken leg, 2 Greek yogurts', ['dairy', 'poultry'], 743, 16, 108.7, 24.7],
              ['2 chobani yogurts and 1.5 cups of brown rice', ['dairy', 'grain'], 607, 105, 28.9, 8.4], ['1 fillet tilapia fish and ravioli', ['fish', 'grain', 'dairy'], 623, 45, 65, 20.5],
              ['2 cups of macaroni and cheese', ['grain', 'dairy'], 752, 94, 19.4, 32], ['1 fillet mahi mahi fish with 1.5 cups soybeans', ['fish', 'vegetables'], 617, 21, 84.5, 23.9]

            ]


#Dinner Database
dinnerList = [ ['6 oz rib eye steak and 2 cups pasta', ['poultry', 'grain'], 852, 76, 56.4, 34.4], ['3 oz Rib eye steak and 1 cup pasta', ['poultry', 'grain'], 426, 38, 28.2, 17.2],
               ['5 oz flank steak and 2 cups vodka pasta', ['poultry', 'grain'], 816, 75, 55, 29.7], ['3 oz flank steak and 1.5 cups vodka pasta', ['poultry', 'grain'], 571.8, 56.3, 35.3, 20.5],
               ['6 oz skirt steak and 2 cups jasmine rice', ['poultry', 'grain'], 814, 90, 50.6, 24.9], ['6 oz skirt steak and 1 cup jasmine rice', ['poultry', 'grain'], 609, 45, 45.3, 24.4],
               ['7 oz filet mignon and 2 cups basmati rice', ['poultry', 'grain'], 939.9, 90, 59.9, 35.9], ['6 oz filet mignon and 2 cups basmati rice', ['poultry', 'grain'], 864, 90, 52.6, 30.9],
               ['Tofu, 2 sweet potatoes, cup of steamed broccoli', ['vegetable', 'dairy'], 716, 65.8, 63, 32.9], ['6 oz tuna, sausage, and artichoke', ['fish', 'vegetable'], 286, 14, 53.5, 1.4],
               ['1 fillet salmon, 1.5 cups roasted corn, 1 cup yam cubes', ['fish', 'vegetable'], 888.5, 77.5, 59.2, 39.8], ['Cod and 2 cups basmati rice with tossed salad', ['fish', 'grain', 'vegetable'], 747, 96.4, 53.4, 15.4],
               ['Ham omelette and mushrooms', ['dairy', 'vegetables', 'poultry'], 588, 6.7, 41.2, 43.6], ['5 oz roast chicken, 2 cups mashed potato, 1 cup broccoli', ['poultry', 'dairy', 'grain'], 844.7, 83.2, 45.3, 36.5],
               ['Hamburger', ['grain', 'poultry', 'vegetable'], 540, 40, 34, 27], ['1 fillet salmon with half a cup of jasmine rice', ['fish', 'grain'], 570.5, 22.5, 52.1, 28.2], 
               ['Spinach empanada with stir fry', ['vegetable', 'grain', 'poultry'], 804, 37, 46, 53], ['Grilled chicken and 2 cups mashed potatoes', ['grain', 'poultry'], 758, 72, 65.2, 24.1],
               ['Sushi roll and 1 cup shrimp salad', ['fish', 'vegetable', 'grain', 'vegetable'], 699, 42,9, 29.8, 45], ['Poke bowl and three scrambled eggs', ['dairy', 'grain', 'fish'], 878, 82.2, 62.9, 36.4],
               ['Chipotle burrito', ['grain', 'poultry', 'vegetable'], 976, 116, 49, 35], ['1 block tofu, 1 avocado, half cup of soybeans', ['dairy', 'vegetable'], 850, 29.6, 65, 68], 
               ['2 lamb chops and 1.5 cups of soybeans', ['poultry', 'vegetable'], 774, 21, 76.5, 44.5], ['1 fillet salmon with sliced avocado', ['fish', 'vegetable'], 790, 17, 54, 57]
            ]
