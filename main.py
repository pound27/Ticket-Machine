import time
import sys
import random
from datetime import datetime
sold = 0
code = 0
password = "adm1n"

def prices(): #asks admin user if they with to update prices by showing current prices   
    try:
        with open("prices.txt", "r", encoding="utf-8") as f: #reads file to find current prices
            prices = []
            for i in f:
                prices.append(i)
            q = input("Would you like to update the current prices?\nChild - %s\nAdult - %s\nSenior - %s\nWristband - %s\n\n(y/n)" % (prices[0],prices[1],prices[2],prices[3])).lower()
    except:
        prices = [12,20,10,20]
        with open("prices.txt", "w", encoding="utf-8") as f: #if prices.txt doesnt have is corrupted for some reason this corrects sets the prices to defult
            for i in range(0,4):
                f.write(str(prices[i]))
        q = input("Would you like to update the current prices?\nChild - %s\nAdult - %s\nSenior - %s\nWristband - %s\n\n(y/n)" % (prices[0],prices[1],prices[2],prices[3])).lower()
    if q == "y" or q == "yes":#updates prices if user wants to
        verified = False
        for i in range(3):
            pass_in = input("\nPlease enter the correct password, you have "+(str(3-i))+" attempts remaining. >") #verifies the user with a password
            if pass_in == password: 
                verified = True
                break
        while verified: #if the password was right this loop is executed
            child = input("\nInput new child price>").strip("£")
            adult = input("Input new adult price>").strip("£")
            senior = input("Input new senior price>").strip("£")
            band = input("Input new wristband price>").strip("£")
            try:
                int(child)#type checks
                int(adult)
                int(senior)
                int(band)
                with open("prices.txt", "w", encoding="utf-8") as p:#writes new prices to file
                    p.write(child+"\n"+adult+"\n"+senior+"\n"+band)
                break
            except:
                print("\nPlease only enter numbers.\n")
        if verified != True:
            print("\nAn incorrect password 3 times, you have not been verified to change the ticket prices. The customer interface will now be displayed.")
            time.sleep(5)
    with open("prices.txt", "r", encoding="utf-8") as f:#opens prices file and copies them to a dictionary
        prices = []
        for i in f:
            prices.append(int(i.strip("\n")))
    final = {
        "child" : prices[0],
        "adult" : prices[1],
        "senior" : prices[2],
        "band" : prices[3]
    }
    print("\n"*9)
    return final #returns prices as a dictionary

def entrance(p): #shows user current prices
    print("""\nTicket prices:\n   
    Child - £"""+str(p["child"])+"""
    Adult - £"""+str(p["adult"])+"""
    Senior - £"""+str(p["senior"]))
    while True:
        child_ticket = input("\nDo you want child any tickets? (y/n) >").lower() #asks user if they want that ticket
        if child_ticket == "y" or child_ticket == "yes": 
            child_ticket = True
            break
        elif child_ticket == "n" or child_ticket == "no":
            child_ticket = False
            child_total = 0
            break
        else:
            print("\nPlease enter 'Y' or 'N'.", end="") #asks user to input valid data
    while child_ticket:
        child_total = input("How many child tickets do you want? >") #finds out how many of the ticket they want
        try:
            if int(child_total) < 0: #checks the input is a positive number and type checks
                print("\nPlease enter a positive number.")
            else:
                child_ticket = False
                break
        except:
            print("\nPlease enter a number.") #asks user to input valid data
    while True:
        adult_ticket = input("\nDo you want adult any tickets? (y/n) >").lower() #asks user if they want that ticket
        if adult_ticket == "y" or adult_ticket == "yes":
            adult_ticket = True
            break
        elif adult_ticket == "n" or adult_ticket == "no":
            adult_ticket = False
            adult_total = 0
            break
        else:
            print("\nPlease enter 'Y' or 'N'.", end="") #asks user to input valid data
    while adult_ticket:
        adult_total = input("How many adult tickets do you want? >") #finds out how many of the ticket they want
        try:
            if int(adult_total) < 0: #checks the input is a positive number and type checks
                print("\nPlease enter a positive number.")
            else:
                adult_ticket = False
                break
        except:
            print("\nPlease enter a number.") #asks user to input valid data
    while True:
        senior_ticket = input("\nDo you want senior any tickets? (y/n) >").lower() #asks user if they want that ticket
        if senior_ticket == "y" or senior_ticket == "yes":
            senior_ticket = True
            break
        elif senior_ticket == "n" or senior_ticket == "no":
            senior_ticket = False
            senior_total = 0
            break
        else:
            print("\nPlease enter 'Y' or 'N'.", end="") #asks user to input valid data
    while senior_ticket:
        senior_total = input("How many senior tickets do you want? >") #finds out how many of the ticket they want
        try:
            if int(senior_total) < 0: #checks the input is a positive number and type checks
                print("\nPlease enter a positive number.")
            else:
                senior_ticket = False
                break
        except:
            print("\nPlease enter a number.") #asks user to input valid data
    total = { #curates total amount of tickets into a dictionary
        "child" : child_total,
        "adult" : adult_total,
        "senior" : senior_total
    }
    return total #return the dictionary

def wristband(p,t):#parameters for prices and total
    print("\n\n")
    while True:
        wrist_question = input("""Would you like wristbands so you can go on any ride without a fee?\n
    Price:
    All - £"""+str(p["band"])+"""
    
    (y/n) >""").lower() #asks user if they want wristbands
        if wrist_question == "y" or wrist_question == "yes":
            wrist_question = True
            print("\n")
            break
        elif wrist_question == "n" or wrist_question == "no":
            wrist_question = False
            wrist_total = 0
            break
        else:
            print("\n\nPlease enter 'Y' or 'N'.") #asks user to input valid data
    while wrist_question:
        wrist_total = input("How many wristbands would you like? >")
        try:
            if int(wrist_total) < 0: #checks the input is a positive number and type checks
                print("\nPlease enter a positive number.")
            else:
                wrist_question = False
                break
        except:
            print("\nPlease enter a number.", end="") #asks user to input valid data
    t["band"] = wrist_total#adds wristband total to total
    return t #returns total

def surname(): #gets user's surname
    while True:
        lead_surname = input("\nWhat is the surname of the lead booker in your party? >").upper() #gets user to input their surname
        if len(lead_surname) >= 1: #checks data inputed is valid
            break
        else:
            print("\nPlease enter a name.", end="") #asks user to input valid data
    return lead_surname

def parking(): #asks user if they want carpass
    while True:
        parking_q = input("\nDo you require a FREE parking pass for the car park? (y/n) >").lower() #asks if user wants a parking pass
        if parking_q == "y" or parking_q == "yes":
            required = 1
            break
        elif parking_q == "n" or parking_q == "no":
            required = 0
            break
        else:
            print("\nPlease enter 'Y' or 'N'.", end="") #asks user to input valid data
    return required #returns 1 or 0

def collect_money(t,p,r):  #shows order summary, gets user to input money and gives back change
    if t["child"] != 0: #if customer has ordered this ticket it adds it to the recipt
        child = int(t["child"])*p["child"] #finds sum of quantity and price
        child_print = str(t["child"])+"x Child ticket " #creates line of recipt
    else:
        child = 0 #if ordered no tickets all values are 0
        child_print = "0"
    if t["adult"] != 0: #repeats for all ticket types
        adult = int(t["adult"])*p["adult"] 
        adult_print = str(t["adult"])+"x Adult ticket "
    else:
        adult = 0 
        adult_print = "0"
    if t["senior"] != 0: 
        senior = int(t["senior"])*p["senior"] 
        senior_print = str(t["senior"])+"x Senior ticket "
    else:
        senior = 0 
        senior_print = "0"
    if t["band"] != 0: 
        band = int(t["band"])*p["band"] 
        band_print = str(t["band"])+"x Wristband "
    else:
        band = 0 
        band_print = "0"
    due = int(child)+int(adult)+int(senior)+int(band) #total of everything
    if due < 0:
        print("Sorry there has been an issue with your order, please reenter what tickets you would like.\nSorry for the inconvenience.")
        correct = False
        positive = False
    elif due > 0:
        positive = True
    while positive:
        time.sleep(2)
        print("\n\n\n\n\nYour order summary:\n") #prints out order summary
        if child_print != "0":
            print(child_print+"£"+str(child))
        if adult_print != "0":
            print(adult_print+"£"+str(adult))
        if senior_print != "0":
            print(senior_print+"£"+str(senior))
        if band_print != "0":
            print(band_print+"£"+str(band)) 
        if r == 1: #adds parking pass on to recipt
            print("1x Parking pass £0")
        else:
            print("NO PARKING PASS")
        print("\nOrder total: £"+str(due)+"\n\n")
        correct = input("Is this correct? (y/n) >").lower() #asks if order is correct
        if correct == "y" or correct == "yes":
            correct = True
            break
        elif correct == "n" or correct == "no":
            correct = False
            break
        else:
            print("\nPlease enter 'Y' or 'N'.") #asks user to input valid data
    if correct == True and positive == True: #if order is correct and the total due is positive it asks for payment
        print("\nTime to pay.\nThis machine only accepts £10 or £20 notes.")
        time.sleep(0.5)
        print("\n£"+str(due)+" due.")
        while True: #asks user to input money until whats due is <=0
            entered = input("Please enter money here: (£10/£20) >").strip("£") #askes user to input money
            if entered == "10": #checks for £10 then removes the value from due
                due += -10
            elif entered == "20": #checks for £20 then removes the value from due
                due += -20
            else:
                print("\nPlease enter either a £10 or £20 note.\n")
                time.sleep(1)#if neither notes are inputed it iterates back
            if due > 0:
                print("\n£"+str(due)+" still due.") #checks for if due is >=0 and states payment fulfilled if so
            else:
                time.sleep(1)
                print("\n>>PAYMENT FULFILLED<<")
                break
        if due != 0: #if change is due it returns it to the user
            print("\nHere is your change> £"+str(abs(due)))
        paid = ["1",child_print,adult_print,senior_print,band_print]#returns if paid with what was brough
    else:
        paid = ["0"]#returns 0 if not paid
    return paid

def issue_ticket(paid,l): #generates ticket for user
    global ticket
    ticket = []
    print("\n\n>>>PRINTING TICKET<<<\n\n")
    time.sleep(2)
    while True:
        global code
        num = random.randint(1,99999999) #generates random customer number
        code = "0"*(8-len(str(num)))+str(num)
        with open("customer_num.txt", "r", encoding="utf-8") as f: #appends all past customer numbers to list
            customer_nums = []
            for i in f:
                customer_nums.append(str(i))
        if code not in customer_nums: #checks the code isn't in the list, if so it regenrates a number
            with open("customer_num.txt", "a", encoding="utf-8") as f:
                f.write("\n"+code)
            break
    print("Ticket for "+str(l)+"\nTicket No: "+code+"\n")#gives the ticket a random identifyer
    ticket.append("Ticket for "+str(l)+"\nTicket No: "+code+"\n")
    if paid[1] != "0": #prints out all tickets purchesed to a ticket
        print(paid[1])
        ticket.append("\n"+paid[1])#appends what was printed to list to write to file
    if paid[2] != "0":
        print(paid[2])
        ticket.append("\n"+paid[2])
    if paid[3] != "0":
        print(paid[3])
        ticket.append("\n"+paid[3])
    if paid[4] != "0":
        print(paid[4])
        ticket.append("\n"+paid[4])
    date = datetime.today().strftime('%d-%m-%Y')
    print("\nDate of purchase: "+date) #prints out date on ticket
    ticket.append("\n\nDate of purchase: "+date)

def carpass(r,l): #creates and prints carpass to user
    if r == 1:
        date = datetime.today().strftime('%d-%m-%Y')
        code = l+"-"+str(random.randint(1111111,9999999))+"-"+date
        print("\n\n-------------------------------------\n\nCarpass: "+code)
        ticket.append("\n\n-------------------------------------\n\nCarpass: "+code)

def read_ticket():
    tick_num = input("\nWhat is your exact ticket number? >") #inputs user's ticket number
    try:
        with open("tickets\_ticket_"+tick_num+".txt", "r", encoding="utf-8") as f: #searches for and opens the file with the user's ticket
            print("\n\n\n>>>PRINTING TICKET<<<\n\n\n")
            time.sleep(1.5)
            for i in f:
                print(i.strip("\n")) #prints out the file
            input("\n\n\n>>Press enter to exit<<")
    except:
        print("Ticket not found, please try again.") #if ticket not found it asks user to input it again
        time.sleep(3)
def main(): #the main sequence of the program to be iteratied
    paid = ["0"]
    while paid[0] == "0":
        end = input("\n\n\n\n\n\n\n\n\n\nWelcome to Copington Adventure Theme Park!\nYou can buy your tickets here!\n\n >>Press enter to continue<<").lower()
        if end == "end": #allows admin to end the program
            sys.exit()
        option = input("\nWould you like to:\na) Purchase tickets\nor\nb) Review ticket\n\n(a/b)>").lower() #asks if user wants to buy or view tickets
        if option == "a": #allows customer to purchase tickets
            total = entrance(price)
            total = wristband(price,total)
            sale = int(total["child"]) + int(total["adult"]) + int(total["senior"]) #finds the total amount of tickets sold and returns it
            if (sold+sale) <= 500:
                lead_surname = surname()
                required = parking()
                paid = collect_money(total,price,required)
            else:
                print("\n\nYou have added too many tickets, there are only "+str(500-sold)+" tickets remaining for today. Please try again and select less tickets") # cancels user's order if they add more tickets than are avadiable
                time.sleep(5)
        elif option == "b":
            read_ticket()
    time.sleep(1)
    issue_ticket(paid,lead_surname)
    time.sleep(1)
    carpass(required,lead_surname)
    time.sleep(0.5)
    file = "tickets\_ticket_"+str(code)+".txt" #creates file name for the ticket
    with open(file, "w", encoding="utf-8") as t:
        for i in ticket: #writes the ticket to a file
            t.write(i)
    print("\n-------------------------------------\n\nThank you for coming to Copington Adventure Theme Park! We hope you enjoy your day!\n") #thank you message for user
    time.sleep(2)
    input(">>Press enter to finish<<")
    return sale

price = prices() 
while sold < 499: #loops the program until over 500 tickets are sold
    sold += main() #loops main until 500 tickets have been sold
print(str("\n"*10)+"No more tickets are avadiable for today, sorry for the inconvenience.\nPlease come back another day!\n") #exits program when no more tickets are avadiable
sys.exit