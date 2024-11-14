import pandas as pd

studyDataFrame = pd.read_csv("insurance.csv")

def User():
    print("U.S. Medical Insurance Data Centre")
    print("--------------------")
    print("1 - Calculate your insurance cost")
    print("2 - Check U.S. Medical Insurance stats from our study")
    choice = int(input("Select option: "))
    if choice == 1:
        age = int(input("Input age:"))
        gender = input("Input gender:")
        g_cost = 0
        if gender.lower() == "male":
            g_cost = 1
        bmi = float(input("Input BMI index:"))
        n_children = int(input("Input num of children:"))
        region = input("Region:")
        s_cost = 0
        smoker = input("You smoke? no/yes:")
        if smoker.lower() == "yes":
            s_cost = 1
        cost = 250*age - 128*g_cost + 370*bmi + 425*n_children + 24000*s_cost - 12500
        print(f"Your insurance is estimated at {cost}$")
        saveToCsv = {
            "age": age,
            "sex": gender,
            "bmi": bmi,
            "children": n_children,
            "smoker": smoker,
            "region": region,
            "charges": cost
        }

        pd.DataFrame([saveToCsv]).to_csv("userInsurance.csv", index = False)
        Main()
    elif choice == 2:
        Main()

userDataFrame = pd.read_csv("userInsurance.csv")

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
    print("8 - Compare your data to data of participants in our study")
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
        print(f"Your age is {userDataFrame.age[0]}")
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
    print("1 - Check average for your region")
    print("2 - Check average for your gender")
    print("3 - Average charge for a region")
    print("4 - Back to Main")
    choice = int(input("Select option: "))
    if choice == 1:
        avgRegion = studyDataFrame.groupby("region").charges.mean()
        print(f"Your charge is {userDataFrame.charges[0]}")
        if userDataFrame.region[0] == "northwest":
            print(f"The average for the NORTHWEST region is {round(avgRegion["northwest"],2)}")
        elif userDataFrame.region[0] == "northeast":
            print(f"The average for the NORTHWEST region is {round(avgRegion["northeast"], 2)}")
        elif userDataFrame.region[0] == "southwest":
            print(f"The average for the NORTHWEST region is {round(avgRegion["southwest"], 2)}")
        elif userDataFrame.region[0] == "southeast":
            print(f"The average for the NORTHWEST region is {round(avgRegion["southeast"], 2)}")
        Additional()
    elif choice == 2:
        genderCount = studyDataFrame.groupby("sex").charges.mean()
        if userDataFrame.sex[0] == "female":
            print(f"The average charge for the females is {round(genderCount["female"],2)}")
        elif userDataFrame.sex[0] == "male":
            print(f"The average charge for the males is {round(genderCount["male"], 2)}")



User()


#northeast - 1
#northwest - 2
#southeast - 3
#southwest - 4