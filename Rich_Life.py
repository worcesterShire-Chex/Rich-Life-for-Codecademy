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
"Female Spouse" : ["{SSS} wants to go to a gun"],
"Male Spouse" : ["{QQQ} wants to go to a gun show!"],
"Child" : []}
occasional_expenses = {"Player" : ["You're low on Gas! We've gotta fill up.", ], 
"Female Spouse" : ["{SSS} wants to go to a gun show!"],
"Male Spouse" : ["{QQQ} wants to go to a gun show!"],
"Child" : []}




#Don't worry about these ^^^^^^ data methods for now, we'll impliment something more sophisticated later

"Added class for dictionaries of commands, allowing access as list.set[type_of_command](i.e. list.spouse[finance]); most likely easiest solution, needs testing. Added functions to while loop, incomplete. "

def random_expense():#car crashes and insurance for monthly goes up, accidents, 
    pass
def monthly_expenses(): #rent/electric and water bills, mortgage, car insurance
    pass
class Credit_Card:
    def __init__(self, bank_name, credit_limit, balance, APR=0.1):
        self.APR = APR # % annual interest rate, take percent you want, say "10.0%", and move decimal two to the left
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
            return "Bad! Overcharge!"
        self.balance -= chrg
        return "Transaction Success!"
spouse_balance = random.randint(0, 1000)
class Spouse:
    def __init__(self, name, gender=False, age=38):
        #may want to include some preferences or some other personality traits
        self.name = name
        self.cards = {"Express Credit Card": Credit_Card("Express Bank", 2300, spouse_balance, 0.075)}
        self.age = age
        if gender == True:
            self.gender = "Woman"
        else:
            self.gender = "Man"
    def __repr__(self):
        return "Name {name}\nGender {gen}\nCredit {cred}".format(name=self.name, gen=self.gender, cred=self.card.name)
class Child:
    def __init__(self, name, allowance=30, gender=False, age=7, favorite_toy="Lego"):
        self.name = name
        self.allowance = allowance
        self.age = age
        self.toy = favorite_toy
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
    spouse_favorite_restaurant = input("What is your spouse' favorite restaurant?")
    spouse = Spouse(spouse_name, spouse_gender)
    break

print()
print()
#when the time comes, this will be appended to like this:
#do some calculations on how their finances are going, determine whether
#or not their credit limit and APR starts high or low,
#and write variables to be numbers in randint equation
class Commands:
    def __init__(self):
        self.bank = {}
        self.spouse = {}
        self.child = {}
        self.work = {}
command_list = Commands()
comms need work

card_list = {"Chase Credit Card" : Credit_Card("Chase Bank", 1000, 2000, 0.9)}
card_list_count = len(card_list)
VERY IMPORTANT!!!  ^^^this is for giving each card a unique ID
Total_Debt = 0
while Total_Debt < 20000:
#     sleep(0.5)
    input("You're at home, and " + spouse)


    inpout = input("Which bank will you call?")
    input2 = input("Hello, " + inpout + ", how can I help you today?")
    if input2 == "add card":
        inclout = input("what will this card's name be?")
        new_card_name = inclout
        card_cumulative = 0
        for crd in card_list.keys():
    #let's add up all the money they owe
            card_cumulative += (card_list[crd].balance * -1)
        new_limit = round(random.randint(3000, 6000) - (card_cumulative /1.2), -2)
        new_APR = (5 + (card_cumulative/200))/100
        card_list[new_card_name] = Credit_Card(new_card_name, new_limit, 0, new_APR)
        print(card_list[new_card_name])


    for crd in card_list.keys():
#let's add up all the money they owe
        Total_Debt += (card_list[crd].balance * -1)



input("You owe too much! you can't sustain your living expenses anymore.")