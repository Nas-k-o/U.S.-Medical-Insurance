#I'll be using CSV for this project
import csv
from itertools import count
from logging.config import listen
from pickle import FLOAT
import pandas as pd

studyDataFrame = pd.read_csv("insurance.csv")

listAge = studyDataFrame["age"]
listGender = studyDataFrame["sex"]
listBmi = studyDataFrame["bmi"]
listChildren = studyDataFrame["children"]
listSmoker = studyDataFrame["smoker"]
listRegion = studyDataFrame["region"]
listCharges = studyDataFrame["charges"]


#Defining Main method, will be used as MainMenu
def Main():
    print("U.S. Medical Insurance Data Centre")
    print("1 - Age functions")
    print("2 - Gender functions")
    print("3 - Bmi functions")
    print("4 - Children functions")
    print("5 - Smoker functions")
    print("6 - Region functions")
    print("7 - Charges functions")
    print("8 - Cross column functions")
    choice = int(input("Select option from the ones above: "))
    if choice == 1:
        Age()
    elif choice == 2:
        Gender()
    elif choice == 3:
        Bmi()
    elif choice == 4:
        Children()
    elif choice == 5:
        Smoker()
    elif choice == 6:
        Region()
    elif choice == 7:
        Charges()
    elif choice == 8:
        Additional()

#Definign Methods for each data category individually
def Age():
    print("--------------------")
    print("1 - Average age")
    print("2 - Check Age count")
    print("3 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        avgAge = studyDataFrame["age"].mean()
        print(f"Average age of this study is {round(avgAge,2)}...")
        Age()
    elif choice == 2:
        selectedAge = int(input("Input age: "))
        countAge = studyDataFrame["age"].value_counts().get(selectedAge, 0)
        if countAge > 0:
            print(f"The chosen age of {selectedAge} appears {countAge} times in our study...")
        else:
            print("This age doesn't appear in our study!")
        Age()
    elif choice == 3:
        Main()
    else:
        print("Not available option")
        Age()

def Gender():
    print("--------------------")
    print("1 - Check Gender count")
    print("2 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        gender_counts = studyDataFrame["sex"].value_counts()
        print(f"There are {gender_counts.get('male', 0)} males & {gender_counts.get('female', 0)} females in our study so far...")
        Gender()
    elif choice == 2:
        Main()
    else:
        print("Not available option")
        Gender()


def Bmi():
    print("--------------------")
    print("1 - Check average BMI")
    print("2 - Check count of over/under BMI Index")
    print("3 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        avgBmi = studyDataFrame["bmi"].mean()
        print(f"Average BMI of this study is {round(avgBmi,2)}...")
        Bmi()
    elif choice == 2:
        choiceI = input("Under/Over: ").lower()
        if choiceI == "under":
            under = float(input("Enter BMI Index: "))
            count = (studyDataFrame["bmi"] <= under).sum()
            print(f"In our study we have {count} cases with BMI under or equal to {under}")
            Bmi()
        elif choiceI == "over":
            over = float(input("Enter BMI Index: "))
            count = (studyDataFrame["bmi"] >= over).sum()
            print(f"In our study we have {count} cases with BMI over or equal to {over}")
            Bmi()
        else:
            print("Not available option")
            Bmi()
    elif choice == 3:
        Main()
    else:
        print("Not available option")
        Bmi()


def Children():
    print("--------------------")
    print("1 - Average num of children")
    print("2 - Check Children count")
    print("3 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        avgChilds = studyDataFrame["children"].mean()
        print(f"Average number of children in this study is {round(avgChilds,2)}...")
        Children()
    elif choice == 2:
        selectedCount = int(input("Input number of children: "))
        countChilds = studyDataFrame["children"].value_counts().get(selectedCount, 0)
        if countChilds > 0:
            print(f"The chosen number of children ({selectedCount}) appears {countChilds} times in our study...")
        else:
            print("This number of children doesn't appear in our study!")
        Children()
    elif choice == 3:
        Main()
    else:
        print("Not available option")
        Children()

def Smoker():
    print("--------------------")
    print("1 - Check Smoker count")
    print("2 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        smoker_counts = studyDataFrame["smoker"].value_counts()
        print(f"There are {smoker_counts.get('no', 0)} non-smokers & {smoker_counts.get('yes', 0)} smokers in our study so far...")
        Smoker()
    elif choice == 2:
        Main()
    else:
        print("Not available option")
        Smoker()


def Region():
    print("--------------------")
    print("1 - Check Region count")
    print("2 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        region_counts = studyDataFrame["region"].value_counts()
        for region, count in region_counts.items():
            print(f"There are {count} people living in {region} region")
        Region()
    elif choice == 2:
        Main()
    else:
        print("Not available option")
        Region()


def Charges():
    print("--------------------")
    print("1 - Check average charge")
    print("2 - Check count of over/under selected charge")
    print("3 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        avgCharge = studyDataFrame["charges"].mean()
        print(f"Average charge of this study is {round(avgCharge,2)}...")
        Charges()
    elif choice == 2:
        choiceI = input("Under/Over: ").lower()
        if choiceI == "under":
            under = float(input("Enter any amount of charge: "))
            count = (studyDataFrame["charges"] <= under).sum()
            print(f"In our study we have {count} cases with charges under or equal to {under}")
            Charges()
        elif choiceI == "over":
            over = float(input("Enter charge amount: "))
            count = (studyDataFrame["charges"] >= over).sum()
            print(f"In our study we have {count} cases with charges over or equal to {over}")
            Charges()
        else:
            print("Not available option")
            Charges()
    elif choice == 3:
        Main()
    else:
        print("Not available option")
        Charges()



#Adding cross columns functions here
def Additional():
    print("--------------------")
    print("1 - Average charge for different genders")
    print("2 - Gender/Smoking ratio")
    print("3 - Average charge for a region")
    print("4 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        gender_avg_charges = studyDataFrame.groupby("sex")["charges"].mean()
        print(f"Average charge for Males: {round(gender_avg_charges.get('male', 0),2)}")
        print(f"Average charge for Females: {round(gender_avg_charges.get('female', 0),2)}")
        Additional()
    elif choice == 2:
        gender_smoker_ratio = studyDataFrame.groupby("sex")["smoker"].value_counts(normalize=True).unstack(fill_value=0)
        print(f"Gender/Smoking ratio:\n{gender_smoker_ratio}")
        Additional()
    elif choice == 3:
        region_avg_charges = studyDataFrame.groupby("region")["charges"].mean()
        for region, charge in region_avg_charges.items():
            print(f"Average charge for {region} region: {round(charge,2)}")
        Additional()
    elif choice == 4:
        Main()
    else:
        print("Invalid option")
        Additional()


Main()

