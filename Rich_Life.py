#this project was inspired by the Netflix series, "How to Get Rich," by Ramit Sethi
#It features unique ideas on finances, where you spend lavishly on what you love, but ruthlessly cut expenses on
#things that don't matter to you, as opposed to age-old addages about saving every penny and so on
#Item was not able to be implimented in a timely manor
import sys
from time import sleep
import random

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
"makeup" : ["Thrive Foundation and Eyeliner kit<$>17.79", "Thrive Eyeshadow Kit<$>19.89", "Naked Mascera and lotions<$>35.75"]}


# (See Line 4)male_child_favorites = {"Food" : [], "games" : [], "clothes": [], "Toys" : []}
# (See Line 4)female_child_favorites = {"Food" : [], "games" : [], "clothes": [], "Toys" : []}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
savings = random.randint(0, 2500)
common_expenses = {"Player" : ["The garbage disposal bill came in<$>30", "It's one of your friends' birthday!<$>35"], 
    "Female Spouse" : [" wants to go to a gun show!<$>20", " wants to get a manicure!<$>30"],
"Male Spouse" : [" wants to go to the mall together!<$>", "wants to go to a gun show!<$>20"],
"Female Child" : [" wants a new toy!<$>18", " really wants to go see a movie with her friends!<$>15"],
"Male Child" : [" asked you to buy him a brand new bike!<$>150", " would like a new comic book<$>20"],
}
#because of our price average calc in r.e. function, gas prices will naturally fluctuate. It's marked for wholesale galons purchase
occasional_expenses = {"Player" : ["You're low on Gas! We've gotta fill up.<$>18", "You've run out of toilet paper! Oh no!<$>16"], 
"Female Spouse" : [" would like to get a manicure!<$>30", " Feels she needs to spend some time with you. Maybe go out to dinner?<$>25", 
    "Your wife needs her car's oil changed<$>35"],
"Male Spouse" : [" Wants to buy some flowers!<$>20", " wants to eat out at the buffet!<$>30"],
"Female Child" : [" has been complaining about not having any games to play, and she won't take no for an answer.<$>30", 
" got an infected ear and needs to see a doctor.<$>100"],
"Male Child" : [" needs to buy a new gym uniform<$>20", " needs to go to the doctor because he got sunburn<$>30"],
"Car" : ["You need to change your car's oil<$>35", "Your car's sideview mirror go broken off!<$>80"]
}

#let's just keep this simple: s1.name + the expense(like first female dmage expense)
Damage_expenses = {"Player" : ["you broke your arm!<$>1200", "You need a kidney stone removed!<$>280"], 
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

last_exp = ""
# last_random_expense = ''
def random_expense(last_random_expense, s1=None, num=80, dam_num = 100):
    print(".")
    optional = True
    ex_pre = last_random_expense
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
        random_chance -= 10
        damage_expense -= 15
    if random_chance >= 30:
        return False
    if random_chance < 15:# occasional
        
        if damage_expense < 33:#damages, obviously
            optional = False
            if car_EX > 50:
                expense_list = Damage_expenses[target]
            else:
                target = " "
                expense_list = Damage_expenses["Car"]
        else:#normal occasion
            optional = False
            expense_list = occasional_expenses[target]
    elif random_chance < 30: #common
        expense_list = common_expenses[target]
    else:
        return False

    while ex_pre == last_random_expense:
        sleep(0.056)
        ex_pre = expense_list[random.randint(0, len(expense_list)-1)]
        the_expense = ex_pre.split("<$>")[0]
        expense_cost = float(ex_pre.split("<$>")[-1])
    inc_or_dec = random.randint(0, 100)
    if inc_or_dec < 50:
        numb = random.randint(50, 99)#target min/max is x0.5, x2, range is between 0.5 and 2
        amount = round((expense_cost * (numb / 100)), 2)
    else:
        numb = random.randint(100, 200)
        amount = round((expense_cost * (numb / 100)), 2)
    print()
    if target == "Player" or "car" in the_expense:
        print(the_expense)
    else:
        print(s1.name + the_expense)
    print()
    print()
    sleep(0.3)
    print("It will cost $" + str(amount))
    print()
    sleep(0.6)
    fam_afford = True
    sleep(1)
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
            
    while (amount > 0) and (damage_expense < 33 or random_chance < 30):
        print("Amount currently Owed: " + str(amount))
        if optional == True:
            damage_expense = 100
            random_chance = 100
        if target == "Player" or 'car' in the_expense:
            pass
            input2 = 'yes'
        elif fam_afford == False:
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
            try:
                the_card = numbered_cards[int(input2) - 1]
            except:
                print("Picking Random Card")
                the_card = numbered_cards[random.randint(0, len(numbered_cards)-1)]
            input3 = input("How much will you pay on this card?(press 'ENTER' if paying the full amount)")
            if input3 == '':
                message = player_card_list[the_card].charge(amount, amount)
            else:
                try:
                    # the_card = numbered_cards[int(input2) - 1]
                    message = player_card_list[the_card].charge(float(input3), amount)
                except:
                    # the_card = numbered_cards[int(input2) - 1]
                    message = player_card_list[the_card].charge(amount, amount)
            if input3.lower() != '':
                try:
                    amount -= float(input3)
                    print()
                    print("You payed " + input3 + " of the full amount due.")
                    print()
                    sleep(1.3)
                except:
                    if message == "Transaction Success!":
                        print("You pay " + str(amount) + " for the item(s)")
                    else:
                        print("Oops! Something went wrong, try again.")
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
                sleep(3.5)
                    
                
        elif input2.lower() == 'no':
            if 'Spouse' in target:
                message = a_card.charge(amount, amount)
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
                    sleep(3)
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
                    sleep(3)
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
    
    if new_fav_chance < 30:
        listed = target.get(item_type, "304<$>1")
        old_spouse_list = s1.favorites.get(item_type, "305<$>2")
        stopper = 200
        while True:
            if listed == []:
                rando_fav = None
                break
            stopper -= 1
            sleep(0.03)
            ran_num = [num for num in range(0, len(listed))]
            rando_fav = listed[random.randint(0, len(listed)-1)]
            if rando_fav in s1.favorites[item_type]:
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

    
        
# (See Line 4)def monthly_expenses(): #rent/electric and water bills, mortgage, car insurance
#     (See Line 4)pass
class Credit_Card:
    def __init__(self, bank_name, card_name, credit_limit, balance, APR=0.1):
        self.APR = APR # % annual interest rate, 10% = 0.1   5% = 0.05
        self.bank = bank_name
        self.name = card_name + " Card"
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
            name=self.name, bank=self.bank, bal=self.balance*-1, lim=self.limit*-1, apr=str(self.APR * 100))
    def charge(self, chrg, full):
        if chrg < 0:
            chrg = chrg * -1
        if full < 0:
            full = full * -1
        
        if (chrg < full) and ((self.balance - chrg) > self.limit):
            pass
        elif (self.balance - chrg) < self.limit:
            return "Card was declined: Insufficient funds!"
        self.balance -= chrg
        self.balance = round(self.balance, 2)
        return "Transaction Success!"
    def pay_card(self, dol):
        self.balance = self.balance + dol


spouse_balance = random.randint(0, 1000)
class Spouse:
    def __init__(self, name, gender=False):
        self.name = name
        self.cards = {"Express Credit Card": Credit_Card("Express Bank", "Express", 2300, spouse_balance, 0.075),
                      "Chase Card 1": Credit_Card("Chase Bank", "Chase", 1500, spouse_balance, 0.25)}
        self.favorites = {"food" : [], "games" : [], "clothes": [], "shoes" : []}
        self.old_games = []
        self.love = 5
        if gender == True:
            self.gender = "Woman"
            self.favorites["makeup"] = []
        else:
            self.gender = "Man"
    def __repr__(self):
        return "Name {name}\nGender {gen}\n".format(name=self.name, gen=self.gender)
    

class Child:
    def __init__(self, name, gender, allowance=30, age=7):
        self.name = name
        self.allowance = allowance
        self.age = age
        # (See Line 4)self.toy = favorite_toy
        # self.favorites = {"Food" : [], "Games" : [], "Clothes": [], "Shoes" : []}
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

sleep(2)
print("Welcome to 'Rich Life!' ")
sleep(1.5)
print()
sleep(0.6)
print("Let's get some info!")
sleep(0.3)
while True:
    sleep(0.5)
    spouse_gender = input("Do you have a wife, a husband, or neither?")
    if spouse_gender.lower() == "neither":
        spouse1 = None
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
kidB = False
while kidB != True:
    try:
        kidAmount = int(kidA)
        kidB = True
    except:
        print("You need to specify a number! Please try again.")
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
    kidAmount -= 1
    child_diff += 1

# Mally = Spouse('Mally', True)
# Dally = Spouse("Dally", False)

# spouse1 = Spouse('Mally', True)
# child_dict["Ruby"] = Child('Ruby',True, 3)
# child_dict["Vally"] = Child('Vally', False, 20)


player_card_list = {"Chase Credit Card (1)" : Credit_Card("Chase Bank", "Chase", 800, 50, 0.09), 
    "USAA Card (2)" : Credit_Card("USAA Bank", "USAA", 500, 100, 0.09), 
    "Key Bank Card (3)" : Credit_Card("Key Bank", "Key Bank", 500, 0, 0.09), 
    "USAA Card (4)" : Credit_Card("USAA Bank", "USAA", 500, 0, 0.09)
}
Total_Debt = 0
total_money = 0
savings = 0
card_suffix = 0
total_weeks = 0
paycheck = random.randint(500, 700)

sleep(0.2)
print()
print()
sleep(0.2)
print()
print()
sleep(0.2)
print("                                       This is:")
sleep(1.2)
print()
print()
print("                                               Your                  ")
sleep(0.4)
print()
sleep(0.4)
print("      #######     #######        ######       #      #||   #     #####   ####   #####")
sleep(0.4)
print("      ##     #       #         ##      ##     #      #||   #       #     #      #")
sleep(0.4)
print("      #      ##      #        ##              #      #||   #       #     ###    #")
sleep(0.4)
print("      #      ##      #       ##               #      #||   #       #     #      ####")
sleep(0.4)
print("      #   ##         #       ##               ########||   #       #     #      #")
sleep(0.4)
print("      # ##           #        ##              #      #||   #       #     #      #")
sleep(0.4)
print("      #    ##        #         ##      ##     #      #||   #       #     #      #")
sleep(0.4)
print("      #      ##   #######        ######       #      #||   ####  #####   #      #####")
sleep(0.4)
print()
sleep(2.4)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while Total_Debt < 15000:
    total_money += paycheck
    if child_dict != {}:
        for kid in child_dict:
            child_dict[kid].allowance += 10
    if spouse1 != None:
        for crd in spouse1.cards:
            spouse1.cards[crd].pay_card(random.randint(50, 200))
            sleep(0.3)
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
    sleep(1.5)
    print()
    print("You just got your paycheck!")
    numbered_cards = []
    while total_money > 0:
        for index, crd in enumerate(player_card_list.keys(), start = 1):
            if (player_card_list[crd].balance == 0):
                string_to_print = f"{index}) {crd} (Balance at 0)"
            else:
                string_to_print = f"{index}) {crd} [" + str(player_card_list[crd].balance*-1) + "]"
            numbered_cards.append(crd)
            print()
            print(string_to_print)
            print()
        input2 = input("Which Card will you pay off?\n(select a number)\nIf you would prefer, you can put your pay into savings by typing 'save'")
        try:
            if 'save' in input2.lower():
                savings += total_money
                total_money = 0
                if savings > 40000:
                    savings = 40000
                    input4 = input("Your savings were maxxed out! You cannot exceed 40000")
                    print("You have $" + str(savings) + " in your savings.")
                    sleep(2)
                    break
                print()
                sleep(0.3)
                print("You have $" + str(savings) + " in your savings.")
                sleep(0.3)
                print()
                print()
                print()
                print()
                sleep(0.3)
                print()
                print()
                print()
                sleep(0.7)
                print()
                break
        except:
            pass
        try:
            the_card = numbered_cards[int(input2) - 1]
            total_money -= (player_card_list[the_card].balance * -1)
            player_card_list[the_card].pay_card((player_card_list[the_card].balance * -1))
        except:
            print("Sorry Something went wrong! Please try again!")
            sleep(2.5)
        

    s_or_k = random.randint(0, 100)
    if spouse1 != None:
        s_or_k -= 10
        categories = [i for i in spouse1.favorites.keys()]
        fav_cat = categories[random.randint(0, len(categories)-1)]
    elif (spouse1 == None) and (child_dict == {}):
        print("643 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        last_exp = random_expense(last_exp, 40, 60)
    if s_or_k <= 40:
        try:
            last_exp = random_expense(last_exp, spouse1, 50, 70)
            new_gift_item = new_favorites(spouse1, fav_cat)#make expense of favorites
        except:
            pass
    else:
        try:
            child_list = [i for i in child_dict.keys()]
            cc = child_list[random.randint(0, len(child_list)-1)]
            last_exp = random_expense(last_exp, child_dict[cc], 50, 70)
        except:
            pass
                 
    sleep(1)
    print()
    sleep(0.3)
    print()
    sleep(0.3)
    input_bank = input("Do you need to call the bank?")
    print()
    if 'yes' in input_bank.lower():
        inbank = input("Which bank will you call?")
        print()
        sleep(0.3)
        while input2.lower() != 'exit':
            print()
            sleep(0.1)
            input2 = input("Hello, " + inbank + ", how can I help you today?\nType 'options' for help.")
            if input2.lower() == "add card":
                print()
                sleep(0.1)
                input4 = input("what will this card's name be?")
                print()
                sleep(0.1)
                card_suffix = len(list(player_card_list.keys())) + 1
                new_card_name = inbank + " " + input4 + '(' + str(card_suffix) + ')'
                card_cumulative = 0
                average_pre = 0
                average_pre2 = 0
                for crd in player_card_list.keys():
            #let's add up all the money they owe
                    card_cumulative += (player_card_list[crd].balance * -1)
                    average_pre += (player_card_list[crd].limit * -1)
                    average_pre2 += 1
                average = (average_pre / average_pre2) + random.randint(111, 333)
                new_limit = round(average + (card_cumulative *1.4)/4, -1)
                new_APR = (5 + (card_cumulative/200))/100
                player_card_list[new_card_name] = Credit_Card(inbank, new_card_name, new_limit, 0, new_APR)
                print()
                print("We've added a new card for you!")
                print()
                print(player_card_list[new_card_name])
            elif input2.lower() == "transfer":
                
                for index, crd in enumerate(player_card_list.keys(), start = 1):
                    if (player_card_list[crd].balance == 0):
                        string_to_print = f"{index}) {crd} (Balance at 0)"
                    else:
                        string_to_print = f"{index}) {crd} [" + str(player_card_list[crd].balance*-1) + "]"
                    numbered_cards.append(crd)
                    print()
                    print(string_to_print)
                    print()
                input2 = input("Which Card will you transfer money to?\n(select a number)")
                try:
                    int(input2)
                except:
                    print("Oops! Something went wrong, try again.")
                    continue

                the_card = numbered_cards[int(input2) - 1]
                if savings - (player_card_list[the_card].balance * -1) < 0:
                    print(savings)
                    input4 = input("We're sorry! You have no savings left! You'll need to save more money")
                    sleep(2)
                else:
                    savings -= (player_card_list[the_card].balance * -1)
                    player_card_list[the_card].pay_card((player_card_list[the_card].balance * -1))
            elif input2.lower() == 'options':
                print("Your options are\n\nadd card\n\ntransfer\n\noptions\n\nexit")
        print("Have a nice day!")
        sleep(3)


    for crd in player_card_list.keys():
#let's add up all the money they owe
        Total_Debt += (player_card_list[crd].balance * -1)
    total_weeks += 1
    print("Debt: " + str(Total_Debt))
    
    sleep(0.78)
    buy_favorite = random.randint(0, 100)
    if spouse1 == None:
        continue
    if buy_favorite <= 45:
        favorite_lst = spouse1.favorites.get(fav_cat, ["Empty_List"])
        if favorite_lst == []:
            print("ERR 760")
            continue
        fav_item = favorite_lst[random.randint(0, len(favorite_lst)-1)]
        the_expense = fav_item.split("<$>")[0]
        try:
            expense_cost = float(fav_item.split("<$>")[-1])
        except:
            print(fav_item)
            sleep(3)
            continue
        if buy_favorite < 20:
            lst = [crd for crd in player_card_list.keys()]
            for crd in lst:
                if ((player_card_list[crd].balance - float(expense_cost)) < player_card_list[crd].limit):
                    print("ERR 774")
                    continue
                else:
                    player_card_list[crd].charge(expense_cost, expense_cost)
                    break
            # lst_i = lst[random.randint(0, len(lst)-1)]
            # player_card_list[lst_i].charge(expense_cost, expense_cost)
            string1 = spouse1.name + """ borrowed your credit card when she went out shopping.\n
            She bought: """ + the_expense + ' !'
            if spouse1.gender == "Man":
                string1 = spouse1.name + """ borrowed your credit card when he went out shopping.\n
                He bought: """ + the_expense + ' !'
            print(string1)
            sleep(1.5)
            #player pays
        else:
            lst = [crd for crd in spouse1.cards.keys()]
            fam_afford = False
            for crd in lst:
                if ((spouse1.cards[crd].balance - float(expense_cost)) < spouse1.cards[crd].limit):
                    print("ERR 794")
                    continue
                else:
                    fam_afford = True
                    spouse1.cards[crd].charge(expense_cost, expense_cost)
                    break
            # lst_i = lst[random.randint(0, len(lst)-1)]
            # spouse1.cards[lst_i].charge(expense_cost, expense_cost)
            if fam_afford == True:
                string1 = spouse1.name + """ bought herself something when she went out shopping.\n
                She bought: """ + the_expense + ' !'
                if spouse1.gender == "Man":
                    string1 = spouse1.name + """ bought himself something when he went out shopping.\n
                    He bought: """ + the_expense + ' !'
                print(string1)
                sleep(1.5)
                #spouse pays
    elif buy_favorite > 45:
        print()
        print("CT 813")
        print()
    sleep(1.5)
        
        



input("You owe too much! you can't sustain your living expenses anymore.")
sleep(3)