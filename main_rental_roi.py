# This program calculates your rental ROI


# from classes import parkingGarage
import time
import os
from classes import roiProperty



expenses = {}
# parking_spaces_available = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# new_roi = roiProperty(name, cost_prop)

def run():
    os.system('clear')
    flag = True
    while flag:
        os.system('clear')
        print('\n\n\n')
        print(f"Welcome to our ROI Calculator for your property!\n\n".center(100))
        print("INSTRUCTIONS : Please answer the following questions before proceeding....\n\n")
        name = input("\nWhat's your first name ? \n\n--> \n\n")
        name.lower()
        response = input(f'\n\nWould you like to calculate the ROI in a property, {name.title()} ? y/n \n\n ---> ')
        
        if response.lower() == 'y':
            cost_prop = float(input(f'\n\nHow much are you planning on paying/paid  in total for the property, {name.title()} ? \n\n--> '))
            new_roi = roiProperty(name, cost_prop, expenses)
            new_roi.valueProp()
            # print(f'\n\nThank you , you can now proceed to your assigned spot ......!\n\n'.center(100))
        elif response.lower() == 'n':
            os.system('clear')
            print(f'Sorry you dont want to stay. See you next time!\n\n'.center(100))
            flag = False
        else:
            print('Try another command\n')
            os.system('clear')
                  
run()