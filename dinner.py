# Developed By: Yosra Alim
# Date: Feb 6th
# Description: Below are the codes for a program accommodating dietary restrictions

print("Welcome Friends!")

print("--------------------------------")

noInvitees = int(input("Please enter the number of invitees:"))

# dictionary to save invitee food preference
prefDict = {}
# dictionary to save order
orderDict = {"Pizza": [0, 44.5], "Pasta": [0, 48.99], "Falafel": [0, 52.99], "Steak": [0, 49.6], "beverage": [0, 5.99]}


# method to return the invitees meal depending on how they answer. A list is passed to the method.
def getOrder(pref):
    if pref[0] == "yes" and pref[1] == "yes" and pref[2] == "no":
        return "Pizza"

    elif pref[0] == "no" and pref[1] == "yes" and pref[2] == "no":
        return "Pasta"

    elif pref[0] == "yes" and pref[1] == "yes" and pref[2] == "yes":
        return "Falafel"

    elif pref[0] == "yes" and pref[1] == "yes" and pref[2] == "yes":
        return "Steak"

    else:
        return "beverage"


# for all the invitees, ask about their food preference. Save it into a hashmap containing a list of the users answers.
for i in range(noInvitees):
    print(f"Please enter the order details for invitee Number {i + 1}/{noInvitees}")

    keto = str(input("Do you want a keto friendly meal?"))
    if keto == "y":
        prefDict[i] = ["yes"]
    else:
        prefDict[i] = ["no"]

    vegan = str(input("Do you want a vegan meal?"))
    if vegan == "y":
        prefDict[i].append("yes")
    else:
        prefDict[i].append("no")

    glutenFree = str(input("Do you want a Gluten-free meal?"))
    if glutenFree == "y":
        prefDict[i].append("yes")
    else:
        prefDict[i].append("no")

    # update the order details
    orderDict[getOrder(prefDict[i])][0] += 1

tipPercentage = int(input("How much do you want to tip your server (% percent)?"))

total = 0

print(f"You have {noInvitees} invitees with the following orders:")

# iterate over the order dictionary to get the meal and meal cost
for i in orderDict.keys():
    curTotal = orderDict[i][0] * orderDict[i][1]
    total += curTotal
    print(f"{orderDict[i][0]} invitees ordered {i}. The cost is: ${curTotal}")

print(f"The total cost before tax is ${round(total, 2)}")

totalTax = round(total, 2) * 1.13

print(f"The total cost after tax is ${totalTax}")

totalTaxTip = totalTax * ((100 + tipPercentage) / 100)

print(f"The total cost after {tipPercentage}% tip is ${totalTaxTip}")