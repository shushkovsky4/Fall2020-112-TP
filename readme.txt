Project Name: NutriLog

Project Description: NutriLog is a nutrition tracker that stores and analyzes your food data based on what you ate each day over the course of a week. NutriLog also calculates your daily caloric needs based on user information and develops sample meal plans based on food group preferences, with the ability to differentiate between preference and anti-preference, and with the ability to lock meals in place.

How to run the project:
Make sure the images are in the 'images' folder, and that the 'images' folder is in the same directory as the python files. Run main.py to run the project.

Libraries to be installed:

To install PIL: run below in a python file and then paste into terminal
import sys
print(f'sudo "{sys.executable}" -m pip install pillow')
print(f'sudo "{sys.executable}" -m pip install requests')

To install Selenium: Enter in terminal
pip install selenium

Libraries in each file:
In main.py:
from cmu_112_graphics import *
from nutritionReceiver import *
from nutritionCalc import *
from nutritionAndUserToCSV import *
import PIL

In nutritionCalc.py:
import random

In nutritionReceiver.py:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

In nutritionAndUserToCSV.py:
import csv
from datetime import date

Shortcut commands:
Press '5' to append some sample user data
