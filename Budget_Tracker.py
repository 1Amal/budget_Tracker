#Amal Kariyawasam, Version: 02/07/2022

"""
User Stories
    1. When I start up the application, I am given the following options:
        a. Add a new entry to the budget tracker
        b. Display the total account balance
        c. View all previous entries
    2. If I choose to add a new entry, I am asked to provide:
        a. A title describing the budget item
        b. Whether the budget item is Income or Expense
        c. The total amount of the budget item
        d. The date of the transaction in "MM-DD-YYYY" string format
    3. If I choose to display the total account balance:
        a. The program adds all income and subtracts all expense items to display the net balance
    4. If I choose to view all previous entries:
        a. The program prints all details of all previous entries in a human readable format

Technical Requirements
        Stores all entries in a .csv file
        Load the previously created entries when the user initializes the application

"""

# https://docs.python.org/3/library/csv.html

import csv

# When I start up the application, I am given the following options:
#    a. Add a new entry to the budget tracker
#    b. Display the total account balance
#    c. View all previous entries
# Use a conditional to respond to what the user has chosen by executing one of the functions defined below

print(
"""
     _                    _ _       ____            _            _     _____               _             
    / \   _ __ ___   __ _| ( )___  | __ ) _   _  __| | __ _  ___| |_  |_   _| __ __ _  ___| | _____ _ __ 
   / _ \ | '_ ` _ \ / _` | |// __| |  _ \| | | |/ _` |/ _` |/ _ \ __|   | || '__/ _` |/ __| |/ / _ \ '__|
  / ___ \| | | | | | (_| | | \__ \ | |_) | |_| | (_| | (_| |  __/ |_    | || | | (_| | (__|   <  __/ |   
 /_/   \_\_| |_| |_|\__,_|_| |___/ |____/ \__,_|\__,_|\__, |\___|\__|   |_||_|  \__,_|\___|_|\_\___|_|   
                                                      |___/                                              

"""
)

current_task = ""
def main_loop():
    current_task = ""
    while current_task != "q":
        print("Press [a] to add a transaction, [b] to view the account balance, [v] to view all transactions, or [q] to quit.")
        current_task = input("What would you like to do?")
        if current_task=="a":
            add_transaction()
        elif current_task=="b":
            view_account_balance()
        elif current_task=="v":
            view_all_transactions()
        elif current_task=="q":
            print("Thank you for using budgeter !")
        else:
            print("Invalid selection, please try again!")

# If I choose to add a new entry, I am asked to provide:
#    a. A title describing the budget item
#    b. Whether the budget item is Income or Expense
#    c. The total amount of the budget item
#    d. The date of the transaction in "MM-DD-YYYY" string format
# Request user input for each of the transaction properties:
# Use a similar loop to the main loop to ensure valid input
# Access the transactions.csv file and write a new row to it

def add_transaction():
#     current_task = ""
#     while current_task =="a":
        new_entry={"title":"","income_or_expense":"","item_income":"","item_expense":"","month":"","day":"","year":""}
        new_entry["title"]=input("Please enter title for budget item: ")
        print(f'Is budget item {new_entry["title"]} income or an expense ?')

        
        #Code to check whether it is income or expense and to capture the input
        expense_type=input("[i] for income, [e] for expense:")
        if expense_type=="i":
            new_entry["income_or_expense"]=expense_type
            print(f'Please enter total income for budget item {new_entry["title"]}')

#Below code will validate input for income and capture the value            
            while True:
                try:
                    new_entry["item_income"]=float(input("$")) 
                    new_entry["item_expense"]=0 
                except ValueError:
                    print("This is an unaccepted response, enter a valid value decimal value i.e 100")
                    continue
                else:
                    break

        elif expense_type=="e":
            new_entry["income_or_expense"]=expense_type
            print(f'Please enter total expense for budget item {new_entry["title"]}')
            
            #Below code will validate input for expense and capture the value            
            while True:
                try:
                    new_entry["item_expense"]=float(input("$"))
                    new_entry["item_income"]=0 
                except ValueError:
                    print("This is an unaccepted response, enter a valid value decimal value i.e 100")
                    continue
                else:
                    break

        else:
            print("Invalid input, Please try again!")
            add_transaction()
        
# Below code will capture dates and input validation        
        print("Please enter Date of transaction in format 'MM-DD-YYYY")

# Code for capturing Month and input validation
        while True:
            try:
                month_i=int(input("Please enter Month of transaction in MM: "))
            except ValueError:
                print("This is an unaccepted response, enter a valid value between 1 - 12")
                continue
            else:
                break
        if month_i>0 and month_i<13:
              new_entry["month"]=month_i
        else:
            print("This is an unaccepted response, enter a valid value between 1 - 12")
            add_transaction()

# Code for capturing Day and input validation
        while True:
            try:
                day_i=int(input("Please enter Day of transaction in DD: "))
            except ValueError:
                print("This is an unaccepted response, enter a valid value between 1 - 31")
                continue
            else:
                break
        if day_i>0 and day_i<32:
              new_entry["day"]=day_i
        else:
            print("This is an unaccepted response, enter a valid value between 1 - 31")
            add_transaction()

# Code for capturing Year and input validation
        while True:
            try:
                year_i=int(input("Please enter Year of transaction in YYYY: "))
            except ValueError:
                print("This is an unaccepted response, enter a valid value between 2000 - 2100")
                continue
            else:
                break
        if year_i>1999 and year_i<2101:
              new_entry["year"]=year_i
        else:
            print("This is an unaccepted response, enter a valid value between 2000 - 2100")        

#Below code will write to the CSV file
        with open("transactions.csv", "a+") as file:
            file.write(f'{new_entry["title"]},{new_entry["income_or_expense"]},{new_entry["item_income"]},{new_entry["item_expense"]},{new_entry["month"]},{new_entry["day"]},{new_entry["year"]}\n')

        return main_loop() #This will return back to the main program input


    
# If I choose to display the total account balance:
#      a. The program adds all income and subtracts all expense items to display the net balance
# Print the value of the account balance

def view_account_balance():

    print(
"""
 ______        _                          
(____  \      | |                         
 ____)  )_____| | _____ ____   ____ _____ 
|  __  ((____ | |(____ |  _ \ / ___) ___ |
| |__)  ) ___ | |/ ___ | | | ( (___| ____|
|______/\_____|\_)_____|_| |_|\____)_____)
""")

    
    # Code to open the transactions CSV file and read income and expense details
    with open("transactions.csv", "r") as transactions_csv_file:
        total_income=[]
        total_expense=[]
        read_income_expense = csv.DictReader(transactions_csv_file)
        # Code below will add the value to two lists
        for row in list(read_income_expense):
            total_income.append(row["item_income"])
            total_expense.append(row["item_expense"])

    # Data from the spreadsheet comes as strings so to convert it to intger following code is used and the totals are calculated 
    
    total_income_convert_to_int = [float(i) for i in total_income] 

    total_income=sum(total_income_convert_to_int)
#     print(total_income)
    
    total_expense_convert_to_int = [float(i) for i in total_expense] 

#     total_expense_convert_to_int = [int(i) for i in total_expense]
    total_expense=sum(total_expense_convert_to_int)
#     print(total_expense)
    
    account_balance=total_income-total_expense
    return(print(f"Your current account balance is $:{account_balance}\n"))

# If I choose to view all previous entries:
#      a. The program prints all details of all previous entries in a human readable format
    # Access the transactions.csv file
    # Loop through each csv entry and print relevant details
    
def view_all_transactions():
    print(
"""

/$$$$$$$$                                                           /$$     /$$                              
|__  $$__/                                                          | $$    |__/                              
   | $$  /$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$$
   | $$ /$$__  $$|____  $$| $$__  $$ /$$_____/ |____  $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$ /$$_____/
   | $$| $$  \__/ /$$$$$$$| $$  \ $$|  $$$$$$   /$$$$$$$| $$        | $$    | $$| $$  \ $$| $$  \ $$|  $$$$$$ 
   | $$| $$      /$$__  $$| $$  | $$ \____  $$ /$$__  $$| $$        | $$ /$$| $$| $$  | $$| $$  | $$ \____  $$
   | $$| $$     |  $$$$$$$| $$  | $$ /$$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$ /$$$$$$$/
   |__/|__/      \_______/|__/  |__/|_______/  \_______/ \_______/   \___/  |__/ \______/ |__/  |__/|_______/ 
                                                                                                              
""")

    
    print("Please see all the transactions\n")

        # Code to open the transactions CSV file and read income and expense details
    with open("transactions.csv", "r") as transactions_csv_file:
        total_income=[]
        total_expense=[]
        read_income_expense = csv.DictReader(transactions_csv_file)
        # Code below will add the value to two lists
        for row in list(read_income_expense):
            print(f'Description:{row["title"]}')
            print(f'Income [i] or expense [e]: {row["income_or_expense"]}')
            print(f'Income:${row["item_income"]}')
            print(f'Expense:${row["item_expense"]}')
            print(f'Date in [MM-DD-YYYY] format: {row["month"]}-{row["day"]}-{row["year"]}\n')
            
        view_account_balance()
        print("End of transaction statement\n")

            
#Test Code to test the function of the program  
main_loop()
# add_transaction()  
# view_account_balance()
# view_all_transactions()
