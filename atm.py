#This Real time ATM software with Database is coded by KINFE MICHAEL TARIKU!
import atmdb
from atmdb import Database
from colorama import init
import pyttsx3 
import datetime 
from termcolor import colored 
init() 
from lazyme.string import color_print
from colorit import *
import sys
import re
import getpass
claimed = False
db = Database("atmdb.db")

from time import sleep
now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")
print('\v')
print(f'\t\t\t The current time is: {time} \v')
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]    "]
def animate(purpose):
    for i in range(len(animation)):
        sleep(0.3)
        sys.stdout.write("\r" + purpose + animation[i % len(animation)])
        sys.stdout.flush()

# def bankUsers():
#     for i in db.fetch():
#         return i
global balance 
global withdraw 
global deposit
withdraw = 0
balance = 0
isTrue = True
engine = pyttsx3.init()

def saybot(string):
    engine.say(string)
    engine.runAndWait()
    
engine.setProperty("rate" ,140 )
while isTrue: 
    # saybot("WELCOME TO KINFISH ATM SERVICE..Here are the main menu to get started!")
    print("\t\t\t\t**********************************")
    print("\t\t\t\t*  ||||||||||||||||||||||||||||| *")
    print("\t\t\t\t*  . . . . . . . . . . . .  . .  *")
    print(colored("\t\t\t\t* WELCOME TO KINFISH ATM SERVICE *" , 'red' ))
    print(colored("\t\t\t\t*        1.CREATE ACCOUNT        *" , 'green'))
    print(colored("\t\t\t\t*        2.LOGIN                 *" , 'yellow'))
    print(colored("\t\t\t\t*        3.ABOUT US              *", 'blue'))
    print(colored("\t\t\t\t*        4.EXIT                  *" , 'white'))
    print("\t\t\t\t**********************************")
    option = int(input("Enter the options: "))
    if option == 1:
    
        print(colored("\t\t\t\t|--- WELCOME TO ACCOUNT CREATING PAGE ---|" , 'yellow'))
        saybot("Welcome to the KINFISH ATM SERVICE Account creating page...There are some fields that you should have to fill neatly...Because those All are sensitive information THANK YOU..BE SAFE ")
     
        
        username_login = input("Enter a username: ")
        
        for i in db.fetch():
            if username_login in i:
                while username_login in i: 
                    saybot("The Usersname has already taken by another...")
                    print(colored("The name is already taken...Try another" , 'red'))
                    
                
                    username_login = input("Enter a username: ")
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        email_login = input("Enter a email address: ")
        tested = re.search(regex , email_login)
        value = tested
        if value:
            pass
        
        else:
            while not value:
                
                email_login = input("Enter a valid email address: ")
                tested = re.search(regex , email_login)
                if tested: 
                    break
                else:
                    saybot("Invalid Email address")
        # email_login =input("Enter your email: ")
        pin_login = getpass.getpass("Enter a pin: ")

        pin_login_con = getpass.getpass("Enter the pin again: ")
        saybot("You are almost done...Next Enter how much that you want to deposit initially")
        deposit = int(input("How much money that you want to intially deposit: "))
        balance += deposit
        
        if pin_login == pin_login_con:
            db.insert(username_login , email_login , pin_login, deposit )
            saybot("We are creating an account for You!")
            animate("Creating an account....")
            
            print(colored("You have successfully created an account!\n" , 'yellow'))
            saybot("You have successfully created an account!")
            
            print(colored("Please You can go to the option 2 for login!\n" , 'red'))
                            
                            
                        
                        
                  
        
                    
                
       
        else:
            saybot("You have entered incorrect info for login!")
            print("You have entered incorrect info for login!")
    elif option == 2:
        saybot("You have choose logging in to Your account...Enter the appropriate name and passcode unless You account get permanently blocked!")
        
        username_forlogin = input("Enter username: ")
        passcode_forlogin = getpass.getpass("Enter pin: ")
        for i in db.fetch():
            if username_forlogin in i:
                if passcode_forlogin in i:
                    isOn = True 
                    animate(f"Logging to {username_forlogin}\'s account!")
                    coded = colored("CODED BY: KINFE MICHAEL TARIKU" , "red", "on_yellow")
                    saybot("Welcome to KINFISH TECH ATM DASHBOARD MENU..here You can a perform transaction based on the Guideline that we mentioned!")
                    print(colored(f"\n\n\t\tHELLO {username_forlogin.upper()} WELCOME TO KINFISH TECH ATM SERVICE USING PYTHON!" , "green"))
                    print(colored(f'''
                            \t\t\t\nThe current time zone is: {time} \v\n\n
                                -->WELCOME TO KINFISH ATM!!<--         
                                    1.BALANCE                          
                                    2.DEPOSIT                              
                                    3.WITHDRAW
                                    4.TRANSFER
                                    5.CLAIM BONUS!
                                    6.ACCOUNT STATUS 
                                    7.ABOUT THE DEVELOPER
                                    8.CHANGE PASSWORD
                                    9.EXIT 
                                    10.GIVE US RATING
                                    11.TO DISPLAY THE MENU!                       {coded}    
                                ''' , 'green'))
                    # def res():
                    #     for i in db.balancefetch():
                    #         var = list(i)
                            
                                
                    #     return var
                    # for i in res():
                    #     pass
                   
                    def returnindex():
                        for i in db.fetch():
                            if username_forlogin in i:
                                return i[0]
                    val = returnindex()   
                    def modify(values):
                        for i in db.fetch():
                            if username_forlogin in i:
                                db.update_balance(val,values) 
                    def fetchingbalance():      
                        for i in db.fetch():
                            if username_forlogin in i:
                                return db.balancefetch(val)
            
                    result = fetchingbalance()
                    def fetching():
                        for i in result:
                            converter = list(i)
                            for i in converter:
                                return i
                    i = fetching()
                    def modify_passcode(values):
                        for i in db.fetch():
                            if username_forlogin in i:
                                db.update_pin(val,values)
                    
                    def fetchingpasscode():      
                        for i in db.fetch():
                            if username_forlogin in i:
                                return db.passcodefetch(val)
                        
                    result = fetchingpasscode()
                    def fetching_passcode():
                        for i in result:
                            converter = list(i)
                            for i in converter:
                                return i
        
                      
                                                                
                    
                    while isOn:
                         
                        
                        op =int(input("Enter the option: "))
                        if op == 1:
                            animate("Checking a balance...")
                            saybot(f"Your current balance is {i} $")
                            print(colored(f"Your current balance is: ${i}" , 'green'))
                            
                            
                        elif op == 2:
                            deposit = int(input("Enter how much do you want to deposit: "))
                            i+=deposit
                            modify(i)
                            animate(f"Depositing ${deposit}...")
                            saybot(f"You have successfully deposited ${deposit} in your account!")
                            print(colored(f"You have successfully deposited ${deposit} in your account!" , 'green'))
                            
                        elif op == 3:
                            withdraw = int(input("Enter how much money you want to withdraw: "))
                            if withdraw > i:
                                    saybot("You cant withdraw with your current balance")
                                    print(colored("You cant withdraw with your current balance" , 'red'))
                            else:
                                i-= withdraw
                                modify(i)
                                animate(f"Withdrawing ${withdraw}....")
                                saybot(f"You have successfully withdraw {withdraw}$ from your account")
                                print(colored(f"You have successfully withdraw ${withdraw} from your account" , 'green'))
                        elif op == 5:
                            if claimed:
                                saybot(f'Hey {username_forlogin}..,You have already Claimed the bonus offered by Us!')
                                print(colored(f'Hey {username_forlogin}..,You have already Claimed the bonus offered by Us!', 'yellow'))
                            else:
                                
                                claimed = True
                                animate(f'Claiming the bonus....')
                                i+=20
                                modify(i)
                                
                                saybot("Congratulation , You claimed the $20 Bonus offered by Us")
                                print(colored(f'\vCongratulation {username_forlogin}, You claimed the $20 Bonus offered by Us!..\nIf you want more offer from us..Website: ' , 'yellow')) 
                        elif op == 4:
                            bank_acc = int(input("Enter the bank account to whom you want to transfer: "))
                            bank_acc = str(bank_acc)
                            if len(bank_acc) == 6:
                                transfer = int(input("How much money that you want to transfer:  "))
                                if transfer > i:
                                    saybot("You cant transfer with your current balance")
                                    print(colored("You cant transfer with your current balance" , 'red'))
                                else:
                                    animate(f"Transfering ${transfer} money to {bank_acc}...")
                                    i-=transfer
                                    modify(i)
                                    print(colored(f"You have successfully transfer ${transfer} to account number {bank_acc}", 'green'))
                            else:
                                saybot("The account number is not valid...It should have to be 6 length number")
                                print(colored("The account number is not valid...It should have to be 6 length number" , 'red'))
                                
                        
                        
                        elif op == 6:
                            animate("Getting to account status menu...")
                            print(f"\nUsername: {username_forlogin}")
                            print(f"Passcode: {passcode_forlogin}")
                        elif op == 7:
                            animate("Getting to about the developer menu...")
                            saybot("THIS SOFTWARE IS DEVELOPED and coded BY KINFE MICHAEL TARIKU...And i am also developed by him!")
                            print(colored(f'''\vHey ...This software is coded and developed by KINFE MICHAEL TARIKU
                                        If any one want to contact me here the link that i can be found\v
                                                        Facebook name --> kin fish
                                                        Twitter username --> kinfishtech
                                                        Github username --> Kinfe123
                                                        Docker username --> Kinfe123
                                                        Instagram username --> umkinfe
                                                        Phone number--> +251919866517
                                                        website --> https://bit.ly/KINFISHTECH
                                        ----->I just wanna to say that age doesnt matter to be a software developer...
                                        Because the only thing that you should have to have is INSPIRATION...Be inspired 
                                        for every thing that you want to make it real..not only for software developer!!
                                        ------->Be humble PROGRAMMER
                                        ------->We build a tools that change the way we live in UNIVERSE!..Because It belong to US!''', 'yellow'))
                        elif op == 8:
                            pinAsk = input("Enter the old pin: ")
                            if pinAsk == passcode_forlogin:
                                pinNew = input("Enter the new pin: ")
                                pinNewCon = input("Enter the new pin again: ")
                                if pinNew == pinNewCon:
                                    passcode_forlogin = pinNewCon
                                    modify_passcode(pinNewCon)
                                    animate("Setting up your passcode....")
                                    print("You have successfully updated your passcode!")
                                else:
                                    print("You have entered incorrect new passcode confirmation!")
                            else:
                                print("You have entered incorrect old pin")
                        elif op == 10:
                            
                            animate("Getting in to rating console...")
                            saybot(" welcome to the rating menu  THE ALLOWED RATING ARE  BAD VGOOD EXCELLENT GOOD")
                            print(colored("\n\t\tALLOWED RATING --> |BAD| |VGOOD| |EXCELLENT| |GOOD|" , "red"))
                            rating = input("Enter the rating from above alternatives: ").upper()
                            if rating == "VGOOD" or rating == "EXCELLENT" or rating == "GOOD" or rating == "BAD":
                                saybot("THANKS FOR RATING ")
                                print(colored("THANKS FOR YOUR RATING!!" , "yellow"))
                            else:
                                saybot("Invalid rating")
                                print(colored("Invalid Rating from the above alternatives!" , "red"))  
                        elif op == 11:
                            print(colored(f'''
                            \t\t\t\nThe current time zone is: {time} \v\n\n
                                -->WELCOME TO KINFISH ATM!!<--         
                                    1.BALANCE                          
                                    2.DEPOSIT                              
                                    3.WITHDRAW
                                    4.TRANSFER
                                    5.CLAIM BONUS!
                                    6.ACCOUNT STATUS 
                                    7.ABOUT THE DEVELOPER
                                    8.CHANGE PASSWORD
                                    9.EXIT 
                                    10.GIVE US RATING
                                    11.DISPLAY THE MENU AGAIN                     {coded}    
                                ''' , 'green'))
                            
                        elif op == 9:
                            saybot("I hope you have enjoyed by our service!...Have a smile day!")
                            print(colored("THANKS FOR USING KINFISH TECH ATM SERVICE" , 'yellow'))
                            isOn = False
                        else:
                            saybot("You are entering unknown command Please try to choose from 1 up to 11")
                            print(colored("You are choosing unknown command from the menu try to choose from 1 - 11" , 'red'))
                else:
                    saybot("The passcode that you have entered is incrrect!")
                    print("The passcode that you have entered is incorrect!")
            else:
                pass
    elif option == 3:
        saybot("THIS SOFTWARE IS DEVELOPED and coded BY KINFE MICHAEL TARIKU...And i am also developed by him!")
        print(colored(f'''\vHey ...This software is coded and developed by KINFE MICHAEL TARIKU
                If any one want to contact me here the link that i can be found\v
                                Facebook name --> kin fish
                                Twitter username --> KINFE MICHAEL TARIKU
                                Github username --> Kinfe123
                                Docker username --> Kinfe123
                                Instagram username --> umkinfe
                                Phone number--> +251919866517
                                website --> https://bit.ly/KINFISHTECH
                ----->I just wanna to say that age doesnt matter to be a software developer...
                Because the only thing that you should have to have is INSPIRATION...Be inspired 
                for every thing that you want to make it real..not only for software developer!!
                ------->Be humble PROGRAMMER
                ------->We build a tools that change the way we live in UNIVERSE!..Because It belong to US!''', 'yellow'))
        
        
    elif option == 4:
        saybot("Thanks For Visiting KINFISH TECH ATM !")
        print(colored(f"Thanks For Visiting KINFISH TECH ATM !" , 'green'))
        isTrue = False
    else:
        saybot("You are entering unknown command Please try to choose from  1 up to 4")
        print(colored("You are entering unknown command Please try to choose from 1- 4", 'red'))
            
                
                
           
               
            