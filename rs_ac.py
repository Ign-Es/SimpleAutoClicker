import pyautogui
import keyboard
import time
import random 
import numpy as np


# alias spython='sudo $(printenv VIRTUAL_ENV)/bin/python3'
auto_clicker_on = False

try:
    while True:
        if keyboard.is_pressed('9'):
            auto_clicker_on = True
            
            if auto_clicker_on:
                print("Auto clicker turned on.")   
                     
        while auto_clicker_on:
            if keyboard.is_pressed('0'):
                auto_clicker_on = False
                print("Auto clicker turned off.")
                break
            pyautogui.click() 
            center = random.uniform(0.77, 0.84)
            variance = random.uniform(0.1, 0.3)
            interval = np.random.normal(center, variance )
            time.sleep(interval)
        if keyboard.is_pressed('esc'):
            print("Exiting...")
            break      
            
except Exception as e:
    print(f"Error: {str(e)}")