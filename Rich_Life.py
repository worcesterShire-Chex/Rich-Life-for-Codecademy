import sys
from time import sleep
import random
#this project is based on the Netflix series, "How to Get Rich," by Ramit Sethi
#It features unique ideas on finances, where you spend lavishly on what you love, but ruthlessly cut expenses on
#things that don't matter to you, as opposed to age-old addages about saving every penny and so on

Price_per_Galon = 2.50 #50% chance increases by randint, 
savings = random.randint(0, 2500)
#IMPORTANT! if gas price > 5.00, pull it down back to 2.50
common_expenses = {"Player" : ["You're low on Gas! We've gotta fill up.", ], 
"Female Spouse" : ["{SSS} wants to go to a {blank}!"],
"Male Spouse" : ["{SSS} wants to go to a {blank}!"],
"Child" : []}
occasional_expenses = {"Player" : ["Something optional, not", ], 
"Female Spouse" : ["{SSS} needs to get a manicure!"],
"Male Spouse" : ["{SSS} wants to go to a gun show!"],
"Child" : [],
"Car" : []
}


mandatory_expenses = {"Player" : ["You're low on Gas! We've gotta fill up."],
"Female Spouse" : [],
"Male Spouse" : [""],
"Female child" : [],
"Male child" : [],
"Car" : []
}

Damage_expenses = {"Player" : ["You broke your arm at the {blank}"], 
"Female Spouse" : ["{SSS} sprained her hand at the {blank}"], 
"Male Spouse" : [""], 
"Child" : [""], 
"Car" : ["Your car broke down! You'll have to pay a towing fee and get it fixed."]
}





#Don't worry about these ^^^^^^ data methods for now, we'll impliment something more sophisticated later


last_random_expense = ''
def random_expense(num, s1):#car crashes and insurance for monthly goes up, accidents, 
    random_chance = random.randint(0, num)
    damage_expense = random.randint(0, 100)
    car_EX = random.randint(0, num)
    if s1.gender == "Man":
        target = "Male Spouse"
    elif s1.gender == "Woman":
        target = "Female Spouse"
    elif s1.gender == "Boy":
        target = "Male Child"
    elif s1.gender == "Girl":
        target = "Female Child"
    else:
        target = "Player"
    if random_chance > 30:
        return False
    if random_chance < 15:# occasional
        
        if damage_expense < 33:#damages, obviously
            if car_EX > 50:
                expense_list = Damage_expenses[target]
            else:
                expense_list = Damage_expenses["Car"]
        else:#normal occasion
            expense_list = occasional_expenses[target]
            
    elif random_chance < 30: #common
        expense_list = common_expenses[target]


    return expense_list[random.randint(0, len(expense_list)-1)]


def mandatory_expense(num): #car crashes, accidents/injuries, incurred fees
    random_chance = random.randint(0, num)
    child_or_spouse = random.randint(0, num)
    damage_expense = random.randint(0, 100)
    common_keys = [i for i in common_expenses.keys()]
    occasional_keys = [i for i in occasional_expenses.keys()]
    e = "Aslo fogor this on"
    if random_chance < 30:
        if damage_expense < 15:
            pass
        if child_or_spouse < 40:
            the_expense = 
            pass
        elif child_or_spouse < 70:
            the_expense = 
        else:
            pass
    else:
        return False
    
        
def monthly_expenses(): #rent/electric and water bills, mortgage, car insurance
    pass
class Credit_Card:
    def __init__(self, bank_name, credit_limit, balance, APR=0.1):
        self.APR = APR # % annual interest rate, 10% = 0.1   5% = 0.05
        self.name = bank_name + " Credit Card"
        if (credit_limit > 0) and (balance > 0):
            self.limit = credit_limit * -1
            self.balance = balance * -1
        elif (credit_limit > 0):
            self.limit = credit_limit * -1
            self.balance = balance
        elif(balance > 0):
            self.limit = credit_limit
            self.balance = balance * -1
        else:
            self.limit = credit_limit # e.g. cannot overcharge under -$1000
            self.balance = balance # how much you owe
    def __repr__(self):
        return "{name} is a card from {bank}.\nIt has a balance of {bal}\nIt's credit limit is {lim}\nIt comes with a {apr}% APR".format(
            name=self.name, bank=self.name[0 : self.name.index(" Credit")], bal=self.balance*-1, lim=self.limit*-1, apr=str(self.APR * 100))
    def charge(self, chrg):
        if chrg < 0: #make sure charge is positive number
            chrg = chrg * -1 #if you have a missing slice of pizza template, and you distribute that to a missing person, there is
            #actually a slice of pizza somewhere, and a person holding it, it's just missing. *brain goes missing instead of exploding*
        if (self.balance - chrg) < self.limit:
            return "Your card was declined: Insufficient funds!"
        self.balance -= chrg
        return "Transaction Success!"
spouse_balance = random.randint(0, 1000)

#We'll need .split() to convert these into useable text and prices
male_spouse_favorites = {"Food" : ["Chicken Parmesan$8.79", "Hamburger and Fries$10.99", "Pizza Cookie$20", 
"Breakfast Croissant$7.59", "Calamari$14.59", "Ma Po Tofu$8.99", "Jalapeno Poppers$12.39", 
"Americana True Colors Test All-American Pulled Pork and Roast Beef(with expired lettuce) Americwich$55", 
"", "", ""], 
"games" : ["Call of Duty: The New One$59.99", "Beet Barry and the Second Great Emu War$19.99", "Star Wars Battlefront XXXVIII$49.99", 
"Jump Force$39.99", "Dust Force$14.99", "Battlestar Galactica IV$39.99", "Azure Skies$24.99", "Dishonored$39.99", "Slime Rancher$19.99"], 
"clothes": ["", "", "", "", "", "", ""], 
"shoes" : ["", "", "", "", "", "", "", "", "", "", ""]}
female_spouse_favorites = {"Food" : ["Chicken Parmesan$8.79", "Strawberry Sorbet$6.89", "Seared Steak with Asparagus$14.45", 
"Pizza Cookie$20", "Spring Rolls$13.89", "Jalapeno Poppers$12.39", "Sex on the Beach$17.69", "Bloody Mary$14.49"], 
"games" : ["Voez$19.99", "Beet Barry and the Second Great Emu War$19.99", "Wolly World$19.99", 
"Wizard of Legend$14.99", "Dust Force$14.99", "Balan Wonderland$29.99", "Azure Skies$24.99", "Dishonored$39.99", "Slime Rancher$19.99"], 
"clothes": ["Victoria's Secret Blouse$39.99", "High Heels$49.99", "", "", "", "", ""], 
"shoes" : ["High Heels$49.99", "", "", "", "", "", "", "", "", "", ""], 
"Makeup" : ["Thrive Foundation and Eyeliner kit$17.79", "", "", "", "", "", "", "", ""]}

class Spouse:
    def __init__(self, name, gender=False):
        #may want to include some preferences or some other personality traits
# add something to spouse and child favorites that, when they change, they are either added to gift command list,
# or added to an invisible list, to try and trick player into forgetting their favorite things
        self.name = name
        self.cards = {"Express Credit Card": Credit_Card("Express Bank", 2300, spouse_balance, 0.075)}
        self.favorites = {"Food" : [], "Games" : [], "Clothes": [], "Shoes" : []}
        self.old_games = []
        if gender == True:
            self.gender = "Woman"
            self.favorites["Makeup"] = []
        else:
            self.gender = "Man"
    def __repr__(self):
        return "Name {name}\nGender {gen}\n".format(name=self.name, gen=self.gender)
    


male_child_favorites = {"Food" : [], "games" : [], "clothes": [], "Toys" : []}
female_child_favorites = {"Food" : [], "games" : [], "clothes": [], "Toys" : []}
class Child:
    def __init__(self, name, allowance=30, gender=False, age=7, favorite_toy="Lego"):
        self.name = name
        self.allowance = allowance
        self.age = age
        self.toy = favorite_toy
        self.favorites = {"Food" : [], "games" : [], "clothes": [], "Toys" : []}
        self.old_toys = []
        self.old_toys.append(favorite_toy)
        if gender == True:
            self.gender = "Girl"
        else:
            self.gender = "Boy"

#early card tests
# card1 = Credit_Card("Chase Bank", -1000, -800, 0.2)
# print(card1.balance)
# print(card1.charge(150))
# print(card1.balance)
# print(card1.charge(500))
# print(card1)
# card1.limit = -2000
while True:
    sleep(0.5)
    spouse_gender = input("Do you have a wife, a husband, or neither?")
    if spouse_gender.lower() == "neither":
        spouse = None
        break
    elif spouse_gender.lower() == "wife":
        spouse_gender = True
    elif spouse_gender.lower() == "husband":
        spouse_gender = False
    else:
        print("please check your spelling and try again")
        print()
        sleep(0.8)
        continue
            
    spouse_name = input("What is your spouse' name?")
    spouse1 = Spouse(spouse_name, spouse_gender)
    spouse_favorite_things = input("What is your spouse' favorite food, and how much does it cost?(please include '$' symbol)")
    if not '$' in spouse_favorite_things:
        raise ValueError("Dollar sign was not present!")
    spouse1.favorites["Food"] = [spouse_favorite_things]
    spouse_favorite_things = input("What is your spouse' favorite game, and how much does it cost?")
    if not '$' in spouse_favorite_things:
        raise ValueError("Dollar sign was not present!")
    spouse1.favorites["Games"] = [spouse_favorite_things]
    spouse_favorite_things = input("What is your spouse' favorite type of shirt, and how much does it cost?")
    if not '$' in spouse_favorite_things:
        raise ValueError("Dollar sign was not present!")
    spouse1.favorites["Clothes"] = [spouse_favorite_things]
    spouse_favorite_things = input("What are your spouse' favorite shoes, and how much do they cost?")
    if not '$' in spouse_favorite_things:
        raise ValueError("Dollar sign was not present!")
    spouse1.favorites["Shoes"] = [spouse_favorite_things]
    if spouse_gender == True:
        spouse_favorite_things = input("What is your spouse' favorite Makeup brand, and how much does it cost?")
        if not '$' in spouse_favorite_things:
            raise ValueError("Dollar sign was not present!")
        spouse1.favorites["Makeup"] = [spouse_favorite_things]
    break

#when the time comes, this will be appended to like this:
#do some calculations on how their finances are going, determine whether
#or not their credit limit and APR starts high or low,
#and write variables to be numbers in randint equation
class Commands:
    def __init__(self):
        self.bank = {"call bank" : ["add card", "cancel card", "loans"]}
        self.spouse = {"buy gift" : ["needs access to gift list"]}
        self.child = {"buy toy" : ["needs access to gift list"]}
        self.work = {}
        self.house = {}
        
user_guide = Commands()
# comms need work

card_list = {"Chase Credit Card" : Credit_Card("Chase Bank", 1000, 2000, 0.9)}
gas_prices = round(random.randint(1.25, 3.70), 2)
Total_Debt = 0
total_days = 0
total_weeks = 0
while Total_Debt < 20000:
    print()
    print()
    sleep(0.2)
    print()
    sleep(0.2)
    print()
    sleep(0.2)
    print()
    sleep(0.2)
    sleep(0.6)
    print("Day " + str(total_days))
    # random_expense()
    # random_event_handler()
    sleep(1.5)

    inpout = input("Which bank will you call?")
    input2 = input("Hello, " + inpout + ", how can I help you today?")
    if input2 == "add card":
        inclout = input("what will this card's name be?")
        if new_card_name in card_list.keys():
            card_occurence = {}
            for crd in card_list.keys():
                card_occurence[crd] = card_occurence[crd] + 1
            new_card_name = inclout + '(' + str(card_occurence[new_card_name]) + ')'
        else:
            new_card_name = inclout
        card_cumulative = 0
        for crd in card_list.keys():
    #let's add up all the money they owe
            card_cumulative += (card_list[crd].balance * -1)
        new_limit = round(random.randint(3000, 6000) - (card_cumulative /1.2), -2)
        new_APR = (5 + (card_cumulative/200))/100
        card_list[new_card_name] = Credit_Card(new_card_name, new_limit, 0, new_APR)
        print("We've added a new card for you!")
        print(card_list[new_card_name])


    for crd in card_list.keys():
#let's add up all the money they owe
        Total_Debt += (card_list[crd].balance * -1)
    total_weeks += 1
        
        



input("You owe too much! you can't sustain your living expenses anymore.")