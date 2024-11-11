#I'll be using CSV for this project
import csv
from itertools import count
from logging.config import listen
from pickle import FLOAT

#Lists to store each type of data observation individually
listAge = list()
listSex = list()
listBmi = list()
listChildren = list()
listSmoker = list()
listRegion = list()
listCharges = list()

#opening insurance.csv
with open("insurance.csv") as insurance_csv:
    ins_dict = csv.DictReader(insurance_csv)

    #Separates the types of date in its allocated lists
    for row in ins_dict:
        listAge.append(int(row["age"]))
        listSex.append(row["sex"])
        listBmi.append(float(row["bmi"]))
        listChildren.append(int(row["children"]))
        listSmoker.append(row["smoker"])
        listRegion.append(row["region"])
        listCharges.append(float(row["charges"]))


#Defining Main method, will be used as MainMenu
def Main():
    print("U.S. Medical Insurance Data Centre")
    print("1 - Age functions")
    print("2 - Sex functions")
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
        Sex()
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
        avgAge = sum(listAge) / len(listAge)
        print(f"Average age of this study is {avgAge}...")
        Age()
    elif choice == 2:
        selectedAge = int(input("Input age: "))
        countAge = listAge.count(selectedAge)
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

def Sex():
    print("--------------------")
    print("1 - Check Sex count")
    print("2 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        maleCount = listSex.count("male")
        femaleCount = listSex.count("female")
        print(f"There are {maleCount} number of males & {femaleCount} females in our study so far...")
        Sex()
    elif choice == 2:
        Main()
    else:
        print("Not available option")
        Sex()

def Bmi():
    print("--------------------")
    print("1 - Check average BMI count")
    print("2 - Check count of over/under BMI Index")
    print("3 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        avgBmi = sum(listBmi) / len(listBmi)
        print(f"Average BMI  of this study is {avgBmi}...")
        Bmi()
    elif choice == 2:
        choiceI = input("Under/Over: ").lower()
        if choiceI == "under":
            under = float(input("Enter BMI Index: "))
            count = 0
            for bmi in listBmi:
                if bmi <= under:
                    count += 1
            print(f"In our study we have {count} cases with BMI under or equal to {under}")
            Bmi()
        elif choiceI == "over":
            over = float(input("Enter BMI Index: "))
            count = 0
            for bmi in listBmi:
                if bmi >= over:
                    count += 1
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
        avgChilds = sum(listChildren) / len(listChildren)
        print(f"Average age of this study is {avgChilds}...")
        Children()
    elif choice == 2:
        selectedCount = int(input("Input number of children: "))
        countChilds = listChildren.count(selectedCount)
        if countChilds > 0:
            print(f"The chosen age of {selectedCount} appears {countChilds} times in our study...")
        else:
            print("This number of Children doesn't appear in our study!")
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
        noSmoking = listSmoker.count("no")
        yesSmoking = listSmoker.count("yes")
        print(f"There are {noSmoking} number of non-smokers & {yesSmoking} smokers in our study so far...")
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
        southwest = listRegion.count("southwest")
        southeast = listRegion.count("southeast")
        northwest = listRegion.count("northwest")
        northeast = listRegion.count("northeast")
        print(f"There are {southwest} number of people living in southwest")
        print(f"There are {southeast} number of people living in southeast")
        print(f"There are {northwest} number of people living in northwest")
        print(f"There are {northeast} number of people living in northeast")
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
        avgCharge = sum(listCharges) / len(listCharges)
        print(f"Average BMI  of this study is {avgCharge}...")
        Charges()
    elif choice == 2:
        choiceI = input("Under/Over: ").lower()
        if choiceI == "under":
            under = float(input("Enter any amount of charge: "))
            count = 0
            for charges in listCharges:
                if charges <= under:
                    count += 1
            print(f"In our study we have {count} cases with charges under or equal to {under}")
            Charges()
        elif choiceI == "over":
            over = float(input("Enter BMI Index: "))
            count = 0
            for charges in listCharges:
                if charges >= over:
                    count += 1
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
    print("4 - Back to Main - MORE OPTIONS SOON")
    choice = int(input("Select option: "))
    if choice == 1:
        countSex = 0
        sumFemale = 0
        sumMale = 0;
        sumCharge = 0
        for person in listSex:
            if listSex[countSex] == "male":
                sumCharge += listCharges[countSex]
                countSex += 1
                sumMale += 1
            else:
                countSex += 1
        print(f"Average charge for Males is {sumCharge / sumMale}")
        countSex = 0
        sumCharge = 0
        for person in listSex:
            if listSex[countSex] == "female":
                sumCharge += listCharges[countSex]
                countSex += 1
                sumFemale += 1
            else:
                countSex += 1
        print(f"Average charge for Females is {sumCharge / sumFemale}")
        Additional()
    elif choice == 2:
        countSex = 0
        sumSmoke = 0
        sumMale = 0
        sumFemale = 0
        for person in listSex:
            if listSex[countSex] == "male":
                if listSmoker[countSex] == "yes":
                    sumSmoke += 1
                    countSex += 1
                    sumMale += 1
                else:
                    countSex += 1
                    sumMale += 1
            else:
                countSex += 1
        print(f"{sumSmoke} males smoke from {sumMale} males in this study")
        countSex = 0
        sumSmoke = 0
        for person in listSex:
            if listSex[countSex] == "female":
                if listSmoker[countSex] == "yes":
                    sumSmoke += 1
                    countSex += 1
                    sumFemale += 1
                else:
                    countSex += 1
                    sumFemale += 1
            else:
                countSex += 1
        print(f"{sumSmoke} females smoke from {sumFemale} females in this study")
        Additional()
    elif choice == 3:
        countRegion = 0
        sumRegion = 0
        sumCharge = 0
        for region in listRegion:
            if listRegion[countRegion] == "southwest":
                sumRegion += 1
                sumCharge += listCharges[countRegion]
                countRegion += 1
            else:
                countRegion += 1
        print(f"Average charge for SOUTHWEST region is {sumCharge / sumRegion}")
        countRegion = 0
        sumRegion = 0
        sumCharge = 0
        for region in listRegion:
            if listRegion[countRegion] == "southeast":
                sumRegion += 1
                sumCharge += listCharges[countRegion]
                countRegion += 1
            else:
                countRegion += 1
        print(f"Average charge for SOUTHEAST region is {sumCharge / sumRegion}")
        countRegion = 0
        sumRegion = 0
        sumCharge = 0
        for region in listRegion:
            if listRegion[countRegion] == "northwest":
                sumRegion += 1
                sumCharge += listCharges[countRegion]
                countRegion += 1
            else:
                countRegion += 1
        print(f"Average charge for NORTHWEST region is {sumCharge / sumRegion}")
        countRegion = 0
        sumRegion = 0
        sumCharge = 0
        for region in listRegion:
            if listRegion[countRegion] == "northeast":
                sumRegion += 1
                sumCharge += listCharges[countRegion]
                countRegion += 1
            else:
                countRegion += 1
        print(f"Average charge for NORTHEAST region is {sumCharge / sumRegion}")
        countRegion = 0
        sumRegion = 0
        sumCharge = 0

    elif choice == 4:
        Main()
    else:
        print("Invalid option")
        Additional()


Main()

