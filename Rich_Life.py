#this project is based on the Netflix series, "How to Get Rich," by Ramit Sethi
#It features unique ideas on finances, where you spend lavishly on what you love, but ruthlessly cut expenses on
#things that don't matter to you, as opposed to age-old addages about saving every penny and so on
#Item was not able to be implimented in a timely manor
import sys
from time import sleep
import random

#We'll need .split() to convert these into useable text and prices
male_spouse_favorites = {"Food" : ["Chicken Parmesan<$>8.79", "Hamburger and Fries<$>10.99", "Pizza Cookie<$>20", 
"Breakfast Croissant<$>7.59", "Calamari<$>14.59", "Ma Po Tofu<$>8.99", "Jalapeno Poppers<$>12.39", 
"Americana True Colors Test All-American Pulled Pork and Roast Beef(with expired lettuce) Americwich<$>55"], 
"games" : ["Call of Duty: The New One<$>59.99", "Beet Barry and the Second Great Emu War<$>19.99", "Star Wars Battlefront XXXVIII<$>49.99", 
"Jump Force<$>39.99", "Dust Force<$>14.99", "Battlestar Galactica IV<$>39.99", "Azure Skies<$>24.99", "Dishonored<$>39.99", "Slime Rancher<$>19.99"], 
"clothes": ["Greg Norman Polo<$>59.99", "Levi Performance Jeans<$>39.99", "Carhartt Winter Gloves<$>29.99", "Slackswear Sweatpants<$>28.99"], 
"shoes" : ["Sketchers Slip-Ins<$>59.99", "Nike Plush+ Tennis Shoes<$>69.99", "Andrea Bochelli Dress Shoes<$>79.99"]}
female_spouse_favorites = {"food" : ["Chicken Parmesan<$>8.79", "Strawberry Sorbet<$>6.89", "Seared Steak with Asparagus<$>14.45", 
"Pizza Cookie<$>20", "Spring Rolls<$>13.89", "Jalapeno Poppers<$>12.39", "Sex on the Beach<$>17.69", "Bloody Mary<$>14.49"], 
"games" : ["Voez<$>19.99", "Beet Barry and the Second Great Emu War<$>19.99", "Wolly World<$>19.99", 
"Wizard of Legend<$>14.99", "Dust Force<$>14.99", "Balan Wonderland<$>29.99", "Azure Skies<$>24.99", "Dishonored<$>39.99", "Slime Rancher<$>19.99", 
"Just Cause 2<$>39.99"], 
"clothes": ["Victoria's Secret Blouse<$>39.99", "Kaitlyn's Boutique Slip, Small<$>23.99", "Drawstring Corset<$>18.99"], 
"shoes" : ["Kaitlyn's Boutique High Heels<$>49.99", "R & B Home Shoes<$>27.99", "Women's Running Shoes<$>46.99"], 
"makeup" : ["Thrive Foundation and Eyeliner kit<$>17.79", "Thrive Eyeshadow Kit<$>19.89", "Naked Foundation and lotions<$>35.75"]}


# (See Line 4)male_child_favorites = {"Food" : [], "games" : [], "clothes": [], "Toys" : []}
# (See Line 4)female_child_favorites = {"Food" : [], "games" : [], "clothes": [], "Toys" : []}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
savings = random.randint(0, 2500)
#IMPORTANT! if gas price > 5.00, pull it down back to 2.50
common_expenses = {"Female Spouse" : [" wants to go to a gun show!<$>20", " wants to get a manicure!<$>30"],
"Male Spouse" : [" wants to go to the mall together!<$>", "wants to go to a gun show!<$>20"],
"Female Child" : [" wants a new toy!<$>18", " really wants to go see a movie with her friends!<$>15"],
"Male Child" : [" asked you to buy him a brand new bike!<$>150", " would like a new comic book<$>20"],
}
#because of our price average calc in r.e. function, gas prices will naturally fluctuate. It's marked for wholesale galons purchase
occasional_expenses = {"Player" : ["You're low on Gas! We've gotta fill up.<$>18", "You've run out of toilet paper! Oh no!<$>16"], 
"Female Spouse" : [" would like to get a manicure!<$>30", " Feels she needs to spend some time with you. Maybe go out to dinner?<$>25"],
"Male Spouse" : [" Wants to buy some flowers!<$>20", " wants to eat out at the buffet!<$>30"],
"Female Child" : [" has been complaining about not having any games to play, and she won't take no for an answer.<$>30", 
" got an infected ear and needs to see a doctor.<$>100"],
"Male Child" : [" needs to buy a new gym uniform<$>20", " needs to go to the doctor because he got sunburn<$>30"],
"Car" : ["You need to change your car's oil<$>35", "Your wife needs her car's oil changed<$>35"]
}

#let's just keep this simple: s1.name + the expense(like first female dmage expense)
Damage_expenses = {"Player" : ["you broke your arm!<$>3000", "You need a kidney stone removed!<$>280"], 
"Female Spouse" : [" sprained her hand!<$>50", " Broke some exercise equipment at the gym!<$>400"], 
"Male Spouse" : [" Had a stroke!<$>1400", " Got stuck in a vending machine! Again!<$>30"], 
"Female Child" : [" Got hit by a car! She has some serious injuries.<$>1600", " Got a very high fever! She needs to go to the hospital.<$>80"],
"Male Child" : [" Tore a ligament during soccer practice!<$>600", " Got a case of pneumonia!<$>350"],
"Car" : ["Your car broke down! You'll have to pay a towing fee and get it fixed.<$>800", "The radiator of your spouse' car broke!<$>400"]
}


#(see line 4)
# payment_messages = {"Spouse" : [""],
# "Child" : []
# }



#Don't worry about these ^^^^^^ data methods for now, we'll impliment something more sophisticated later


last_exp = ""
# last_random_expense = ''
def random_expense(last_random_expense, s1=None, num=80, dam_num = 100):
    optional = True
    the_expense = last_random_expense
    random_chance = random.randint(0, num)
    damage_expense = random.randint(0, dam_num)
    car_EX = random.randint(0, 100)
    try:
        if s1.gender == "Man":
            target = "Male Spouse"
        elif s1.gender == "Woman":
            target = "Female Spouse"
        elif s1.gender == "Boy":
            target = "Male Child"
        elif s1.gender == "Girl":
            target = "Female Child"
    except:
        target = "Player"
    print(random_chance)
    if random_chance > 30:
        return False
    if random_chance < 15:# occasional
        
        if damage_expense < 33:#damages, obviously
            optional = False
            if car_EX > 50:
                expense_list = Damage_expenses[target]
            else:
                expense_list = Damage_expenses["Car"]
        else:#normal occasion
            optional = False
            expense_list = occasional_expenses[target]
    elif random_chance < 30: #common
        expense_list = common_expenses[target]
    elif random_chance >= 30:
        expense_list = None

    while the_expense == last_random_expense:
        the_expense = expense_list[random.randint(0, len(expense_list)-1)].split("<$>")[0]
        expense_cost = expense_list[random.randint(0, len(expense_list)-1)].split("<$>")[-1]
        if the_expense == last_random_expense:
            print("Line 106 did it's jub.")
            print(last_random_expense, the_expense)
        #     sleep(6)
        #     continue
        # else:
        #     break
    inc_or_dec = random.randint(0, 100)
    if inc_or_dec < 50:
        numb = random.randint(50, 99)#target min/max is x0.5, x2, range is between 0.5 and 2
        amount = round((int(expense_cost) * (numb / 100)), 2)
    else:
        numb = random.randint(100, 200)
        amount = round((int(expense_cost) * (numb / 100)), 2)
    print()
    if target == "Player":
        print(the_expense)
    elif target != "Player" or target != "Car":
        print(s1.name + the_expense)
    elif expense_list == Damage_expenses["Car"]:
        print(the_expense)
    print()
    print()
    sleep(0.3)
    print("It will cost $" + str(amount))
    print()
    sleep(0.6)
    fam_afford = True
    sleep(2)
    if "Child" in target:
        
        if s1.allowance - amount > 0:
            pass
        else:
            fam_afford = False
    elif "Spouse" in target:
        for ke in s1.cards.keys():
            a_card = s1.cards.get(ke)
            if (a_card.balance - amount) > a_card.limit:
                fam_afford = True
                break
            else:
                fam_afford = False
                continue
            
    #part that checks to see if family member can pay(not if it's a car, obvs)
    while (amount > 0) and (damage_expense < 33 or random_chance < 30):
        if optional == True:
            damage_expense = 100
            random_chance = 100
        if fam_afford == False:
            print(s1.name + " can't pay for it.")
            input2 = input("Will you pay?")
        else:
            print(s1.name + " can pay for it.")
            input2 = input("Will you pay for it instead?")
        if input2.lower() == 'yes':
            numbered_cards = []
            print("Which Card will you use?")
            print()
            sleep(0.4)
            for index, crd in enumerate(player_card_list.keys(), start = 1):
                if (player_card_list[crd].balance == player_card_list[crd].limit):
                    string_to_print = f"{index}) {crd} (ineligible)"
                else:
                    string_to_print = f"{index}) {crd}"
                numbered_cards.append(crd)
                print()
                print(string_to_print)
                print()
            input2 = input("Which Card will you use?\n(select a number)")
            # for index, crd in enumerate(player_card_list.keys(), start = 1):
            #     if (player_card_list[crd].balance - amount) < player_card_list[crd].limit:         Redundant Code Reiteration
            #         string_to_print = f"{index}) {crd} (ineligible)"
            #     else:
            #         string_to_print = f"{index}) {crd}"
            #     numbered_cards.append(crd)
            #     print()
            #     print(string_to_print)
            #     print()
            input3 = input("How much will you pay on this card?(say 'all' if paying full amount)")
            try:
                the_card = numbered_cards[int(input2) - 1]
                message = player_card_list[the_card].charge(int(input3), amount)
            except:
                the_card = numbered_cards[int(input2) - 1]
                message = player_card_list[the_card].charge(amount, amount)
            if input3.lower() != 'all':
                print("You payed " + input3 + " of the full amount due.")
                sleep(0.3)
                amount -= float(input3)
                continue
            if message == "Transaction Success!":
                damage_expense = 100
                random_chance = 100
                print()
                sleep(1)
                print()
                print("You pay " + str(amount) + " for the item(s)")
                print()
                sleep(1)
                return the_expense
            else:
                print()
                sleep(1)
                print()
                print(message)
                sleep(4)
                    
                
                
            #a few if statements
            #some variable representing card
            #some_variable.charge(amount)
        elif input2.lower() == 'no':
            if 'Spouse' in target:
                message = a_card.charge(amount, amount)
                #this needs to include a 'heart' functionality, with a list of different payment flavor text
                #based on how much love is lost or maintained
                if message == "Transaction Success!":
                    damage_expense = 100
                    random_chance = 100
                    print(s1.name + " reluctantly pays.\n" + s1.name + "'s Card Balance is now " + str(s1.cards.get(ke).balance))
                    return the_expense
                elif damage_expense < 33:
                    print()
                    sleep(1)
                    print()
                    print("You have to pay for these damages! This expense is unavoidable.")
                    sleep(4)
                    continue
                else:
                    print()
                    sleep(1)
                    print()
                    print("You decided not to pay for " + s1.name + "'s item(s).")
                    sleep(4)
                    return the_expense
                    
            elif 'Child' in target:
                message = s1.use_allowance(amount)
                if message == "Piggy Bank Success!":
                    print(s1.name + "'s allowance is now " + str(s1.allowance))
                    damage_expense = 100
                    random_chance = 100
                    print(s1.name + " reluctlantly pays for the item")
                    return the_expense
                elif damage_expense < 33:
                    print()
                    sleep(1)
                    print()
                    print("You have to pay for these damages! This expense is unavoidable.")
                    sleep(4)
                    continue

                else:
                    print()
                    sleep(1)
                    print()
                    print("You decided not to pay for " + s1.name + "'s item(s).")
                    sleep(4)
                    return the_expense

            break
            pass
        elif (input2.lower() != 'yes') or (input2.lower() != 'no'):
            print("Please answer yes or no !")
            random_chance = 20
            continue


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def new_favorites(s1, item_type):
    new_fav_chance = random.randint(0, 100)
    if s1.gender == "Man":
        target = male_spouse_favorites
    elif s1.gender == "Woman":
        target = female_spouse_favorites
    else:
        target = "ERROR" #if it a child, will just cause
    
    if new_fav_chance < 99:
        listed = target.get(item_type, "NO FAVORITES IN LIST")
        old_spouse_list = s1.favorites.get(item_type, "NO FAVORITES IN LIST")
        stopper = 200
        while True:
            if listed == []:
                print("Wall3")
                rando_fav = None
                break
            stopper -= 1
            sleep(0.03)
            ran_num = [num for num in range(0, len(listed))]
            rando_fav = listed[random.randint(0, len(listed)-1)]
            if rando_fav in s1.favorites[item_type]:
                print("Wall2")
                print(listed.remove(rando_fav))
                sleep(0.03)
                rando_fav = None
                continue
            break
                
        
        if rando_fav == None:
            print(len(target.get(item_type, "NN")), len(old_spouse_list))#print max number of items and number in spouse list
            return "Issue with NF function"
        old_spouse_list.append(rando_fav)
        s1.favorites[item_type] = old_spouse_list
        return s1.favorites[item_type]
    else:
        return None
    var = 0


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Objectives:
# DONE! (for now...)
# 1) Impliment same method for asking spouse favs but for kids(easy, just copy code block and 
# make while loop bound to kidAmount = input('How many kids do you have?'), then 
# while kidAmount > 0 keep going until 0, will never activate if answered 0)


# DONE!
# 2) Impliment system involving damage_exp variable in rando-expense where the damage-exp var
# will be changed to 100 when the amount is changed to 0(paid off). this makes it so the mandatory-expenses
# function is obsolete. An additional thing in getting list of player cards to display when a card is not eligible to
# pay off the amount.

#Done!
# 4) work on the implimentation of child and spouse favorites. We need a chance calculation for whether or not 
# spouse/child gains a new interest/fav. It will be fairly simple to add, just add to their object's list

# DOOOOONE!!!!!!
#4.5) Write in the rest of the favorites(just don't make it too difficult, just a couple per category)
#Figure out what else we can do/how to make work the damage expenses
#Damage expenses NEED to be shortened. 1 or 2 per category

# 5) Long-Term Goal: get the main while loop up and going, which will be the end-goal


# (See Line 4)def mandatory_expense(num): #car crashes, accidents/injuries, incurred fees
#     (See Line 4)random_chance = random.randint(0, num)
#     (See Line 4)child_or_spouse = random.randint(0, num)
#     (See Line 4)damage_expense = random.randint(0, 100)
#     (See Line 4)if random_chance < 30:
#         (See Line 4)if damage_expense < 15:
#             (See Line 4)pass
#         (See Line 4)if child_or_spouse < 40:
#             # the_expense = 
#             (See Line 4)pass
#         (See Line 4)elif child_or_spouse < 70:
#             # the_expense = 
#             (See Line 4)pass
#         (See Line 4)else:
#             (See Line 4)pass
#     (See Line 4)else:
#         (See Line 4)return False
    
        
# (See Line 4)def monthly_expenses(): #rent/electric and water bills, mortgage, car insurance
#     (See Line 4)pass
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
    def charge(self, chrg, full):
        if chrg < 0:
            chrg = chrg * -1
        if full < 0:
            full = full * -1
        
        if (chrg < full) and ((self.balance - chrg) > self.limit):
            pass
        elif (self.balance - chrg) < self.limit:
            return "Card was declined: Insufficient funds!"
        self.balance -= chrg#2 in here goes to tenths place
        self.balance = round(self.balance, 2)#2 in here goes to tenths place
        return "Transaction Success!"
    def pay_card(self, dol):
        self.balance = self.balance + dol


spouse_balance = random.randint(0, 1000)
class Spouse:
    def __init__(self, name, gender=False):
        #may want to include some preferences or some other personality traits
# add something to spouse and child favorites that, when they change, they are either added to gift command list,
# or added to an invisible list, to try and trick player into forgetting their favorite things
        self.name = name
        self.cards = {"Express Credit Card": Credit_Card("Express Bank", 2300, spouse_balance, 0.075),
                      "Chase Card 1": Credit_Card("Chase Bank", 1500, spouse_balance, 0.25)}
        self.favorites = {"food" : [], "games" : [], "clothes": [], "shoes" : []}
        self.old_games = []
        self.love = 5
        if gender == True:
            self.gender = "Woman"
            self.favorites["Makeup"] = []
        else:
            self.gender = "Man"
    def __repr__(self):
        return "Name {name}\nGender {gen}\n".format(name=self.name, gen=self.gender)
    

class Child:
    def __init__(self, name, allowance=30, gender=False, age=7):
        self.name = name
        self.allowance = allowance
        self.age = age
        # (See Line 4)self.toy = favorite_toy
        self.favorites = {"Food" : [], "Games" : [], "Clothes": [], "Shoes" : []}
        # (See Line 4)self.old_toys = []
        self.love = 5
        # (See Line 4)self.old_toys.append(favorite_toy)
        if gender == True:
            self.gender = "Girl"
        else:
            self.gender = "Boy"
    
    def __repr__(self):
        return """{name} is a(n) {age}-year-old {gender}. 
        (s)he has ${allc}, and some of their favorite things 
        are: {f1}, {f2}, {f3}""".format(name=self.name, age=str(self.age), allc=str(self.allowance), 
        f1=self.favorites['food'][0], f2=self.favorites['clothes'][0], f3=self.favorites['games'][0])
    def use_allowance(self, chrg):
        if chrg < 0: #make sure charge is positive number
            chrg = chrg * -1
        if (self.allowance - chrg) < 0:
            return self.name + " can't afford it!"
        self.allowance -= chrg
        self.allowance = round(self.allowance, 2)
        return "Piggy Bank Success!"

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

kidA = input("How many children do you have?")
kidAmount = int(kidA)
child_dict = {}
child_diff = 1
while kidAmount > 0:
    sleep(0.5)
    print("child " + str(child_diff))
    Child_gender = input("Is this child a boy or a girl?")
    if Child_gender.lower() == "neither":
        Child = None
        break
    elif Child_gender.lower() == "girl":
        Child_gender = True
    elif Child_gender.lower() == "boy":
        Child_gender = False
    else:
        print("please check your spelling and try again")
        print()
        sleep(0.8)
        continue
            
    Child_name = input("What is this Child's name?")
    child_dict[child_diff] = Child(Child_name, Child_gender)
    Child_favorite_things = input("What is " + Child_name + "'s favorite food, and how much does it cost?(please include '$' symbol)")
    if not '$' in Child_favorite_things:
        raise ValueError("Dollar sign was not present!")
    child_dict[child_diff].favorites["Food"] = [Child_favorite_things]
    print(child_dict[child_diff].favorites["Food"])
    Child_favorite_things = input("What is " + Child_name + "'s favorite game, and how much does it cost?")
    if not '$' in Child_favorite_things:
        raise ValueError("Dollar sign was not present!")
    child_dict[child_diff].favorites["Games"] = [Child_favorite_things]
    print(child_dict[child_diff].favorites["Games"])
    Child_favorite_things = input("What is " + Child_name + "'s favorite type of clothes, and how much does it cost?")
    if not '$' in Child_favorite_things:
        raise ValueError("Dollar sign was not present!")
    child_dict[child_diff].favorites["Clothes"] = [Child_favorite_things]
    print(child_dict[child_diff].favorites["Clothes"])
    Child_favorite_things = input("What is " + Child_name + "'s favorite shoes, and how much do they cost?")
    if not '$' in Child_favorite_things:
        raise ValueError("Dollar sign was not present!")
    child_dict[child_diff].favorites["Shoes"] = [Child_favorite_things]
    print(child_dict[child_diff].favorites["Shoes"])
    kidAmount -= 1
    child_diff += 1
print(child_dict)

Mally = Spouse('Mally', True)
Dally = Spouse("Dally", False)

spouse1 = Spouse('Mally', True)
child_dict["Ruby"] = Child('Ruby', 3, True)
child_dict["Vally"] = Child('Vally', 20, False)


#when the time comes, this will be appended to like this:
#do some calculations on how their finances are going, determine whether
#or not their credit limit and APR starts high or low,
#and write variables to be numbers in randint equation
# class Commands:
#     def __init__(self):
#         self.bank = {"call bank" : ["add card", "cancel card", "loans"]}
        # self.spouse = {"buy gift" : ["needs access to gift list"]}
        # self.child = {"buy toy" : ["needs access to gift list"]}
        # self.work = {}
        # self.house = {}
        
# user_guide = Commands()
# comms need work

player_card_list = {"Chase Credit Card (1)" : Credit_Card("Chase Bank", 2000, 1000, 0.9)}
Total_Debt = 0
total_money = 0
savings = 0
card_suffix = 0
total_weeks = 0
paycheck = random.randint(1000, 1200)
while Total_Debt < 15000:
    total_money += paycheck
    for kid in child_dict:
        print(child_dict[kid].allowance)
        child_dict[kid].allowance += 10
    for crd in spouse1.cards:
        print(spouse1.cards[crd].balance)
        spouse1.cards[crd].pay_card(random.randint(50, 200))
        print("TEMP PRINT STATEMENT BOGU$@FNO#@YBU@IL")
        print(spouse1.cards[crd].balance)
        sleep(2)
    Total_Debt = 0
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
    print("Week " + str(total_weeks))
    sleep(0.5)
    print()
    print("You just got your paycheck!")
    numbered_cards = []
    while total_money > 0:
        for index, crd in enumerate(player_card_list.keys(), start = 1):
            if (player_card_list[crd].balance == 0):
                string_to_print = f"{index}) {crd} (Balance at 0)"
            else:
                string_to_print = f"{index}) {crd}"
            numbered_cards.append(crd)
            print()
            print(string_to_print)
            print()
        input2 = input("Which Card will you pay off?\n(select a number)\nIf you would prefer, you can put your pay into savings by typing 'save'")
        try:
            if input2.lower() == 'save':
                savings += total_money
                total_money = 0
                print()
                sleep(0.3)
                print("You have $" + str(savings) + " in your savings.")
                sleep(0.3)
                print()
                break
        except:
            pass
        the_card = numbered_cards[int(input2) - 1]
        total_money -= (player_card_list[the_card].balance * -1)
        player_card_list[the_card].pay_card((player_card_list[the_card].balance * -1))
        
    s_or_k = random.randint(0, 100)
    categories = [i for i in spouse1.favorites.keys()]
    fav_cat = categories[random.randint(0, len(categories)-1)]
    if s_or_k > 50:
        last_exp = random_expense(last_exp, spouse1, 35, 70)
        new_gift_item = new_favorites(spouse1, fav_cat)
    else:
        child_list = [i for i in child_dict.keys()]
        cc = child_list[random.randint(0, len(child_list)-1)]
        last_exp = random_expense(last_exp, child_dict[cc], 35, 70)
        
    sleep(1.5)
    print()
    sleep(0.3)
    print()
    sleep(0.3)
    input_bank = input("Do you need to call the bank?")
    print()
    if input_bank.lower() == 'yes':
        inpout = input("Which bank will you call?")
        print()
        sleep(0.3)
        while input2.lower() != 'exit':
            print()
            sleep(0.1)
            input2 = input("Hello, " + inpout + ", how can I help you today?\nType 'options' for help.")
            if input2.lower() == "add card":
                print()
                sleep(0.1)
                input4 = input("what will this card's name be?")
                print()
                sleep(0.1)
                card_suffix = len(list(player_card_list.keys())) + 1
                new_card_name = input4 + '(' + str(card_suffix) + ')'
                card_cumulative = 0
                for crd in player_card_list.keys():
            #let's add up all the money they owe
                    card_cumulative += (player_card_list[crd].balance * -1)
                new_limit = round(random.randint(3000, 6000) - (card_cumulative /1.2), -2)
                new_APR = (5 + (card_cumulative/200))/100
                player_card_list[new_card_name] = Credit_Card(new_card_name, new_limit, 0, new_APR)
                print("We've added a new card for you!")
                print(player_card_list[new_card_name])
            elif input2.lower() == "transfer":
                
                for index, crd in enumerate(player_card_list.keys(), start = 1):
                    if (player_card_list[crd].balance == 0):
                        string_to_print = f"{index}) {crd} (Balance at 0)"
                    else:
                        string_to_print = f"{index}) {crd}"
                    numbered_cards.append(crd)
                    print()
                    print(string_to_print)
                    print()
                input2 = input("Which Card will you transfer money to?\n(select a number)")

                the_card = numbered_cards[int(input2) - 1]
                savings -= (player_card_list[the_card].balance * -1)
                player_card_list[the_card].pay_card((player_card_list[the_card].balance * -1))
            elif input2.lower() == 'options':
                print("Your options are\n\nadd card\n\ntransfer\n\noptions\n\nexit")
        print("Have a nice day!")


    for crd in player_card_list.keys():
#let's add up all the money they owe
        Total_Debt += (player_card_list[crd].balance * -1)
    total_weeks += 1
        
        



input("You owe too much! you can't sustain your living expenses anymore.")