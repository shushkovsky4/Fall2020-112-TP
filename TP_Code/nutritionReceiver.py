from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#nutritionReceiver.py uses Selenium web driving to obtain the user's food's nutrients from nutritionix.com

#Code for turning Selenium into headless (so the user doesn't see Chrome opening) taken from 
#https://stackoverflow.com/questions/46920243/how-to-configure-chromedriver-to-initiate-chrome-browser-in-headless-mode-throug

def nutritionFacts(word): #takes in user input from main script
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path='/Users/MaxS/Downloads/chromedriver', options=options) #/Users/MaxS/Downloads/chromedriver
    driver.get("https://www.nutritionix.com/search?q=" + word) 
    driver.implicitly_wait(3)
    elem = driver.find_elements_by_xpath(".//li[@class='ng-scope']")
    elemFood = elem[0].find_element_by_xpath(".//h4[@class='name ng-binding']").text
    temp = elem[0].click() #Clicks on first food option
    driver.implicitly_wait(5)

    calories = float(driver.find_element_by_xpath(".//span[@itemprop='calories']").text)
    carbohydrates = driver.find_element_by_xpath(".//span[@itemprop='carbohydrateContent']").text
    carbohydrates = float(carbohydrates[:len(carbohydrates)-7]) #removes last 7 additional chars
    protein = driver.find_element_by_xpath(".//span[@itemprop='proteinContent']").text
    protein = float(protein[:len(protein)-7]) #removes last 7 additional chars
    fat = driver.find_element_by_xpath(".//span[@itemprop='fatContent']").text
    fat = float(fat[:len(fat)-7]) #removes last 7 additional chars

    driver.close()
    driver.quit()
    return (calories, carbohydrates, protein, fat)



