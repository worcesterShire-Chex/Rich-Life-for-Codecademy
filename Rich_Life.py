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
class Spouse:
    def __init__(self, name, credit_card, gender=False):
        #may want to include some preferences or some other personality traits
        self.name = name
        self.card = credit_card
        if gender == True:
            self.gender = "woman"
        else:
            self.gender = "Man"
    def __repr__(self):
        return "Name {name}\nGender {gen}\nCredit {cred}".format(name=self.name, gen=self.gender, cred=self.card.name)
class Child:
    def __init__(self, name, allowance=30, gender=False):
        self.name = name
        self.allowance = allowance
        if gender == True:
            self.gender = "Girl"
        else:
            self.gender = "Boy"

card1 = Credit_Card("Chase Bank", -1000, -800, 0.2)

print(card1.balance)
print(card1.charge(150))
print(card1.balance)
print(card1.charge(500))
print(card1)
card1.limit = -2000
Betsy = Spouse("Betsy", card1, True)
print()
print()
print()
print()
print(Betsy)