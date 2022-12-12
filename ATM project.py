#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd  
import time
from datetime import datetime
from datetime import date
import os

class WrongPinException(Exception):
    def __init__(self):
        print("PLEASE ENTER VALID PIN")

class Bank:
    customers_info = []
        
    def create_account(self):
        
        ''' As there is validation in ATM is based on the atm card it is not possible to specify who are going to use atm machine 
         currently so im taking only one user data here '''
        
        # Here im creating account by  calling constructor of cusotmer account
        customer = Customer("12345678","sasidhar","21/09/2003","9876543210","483210345645","savings",2000,"4752998413","1234","798")
        Bank.customers_info.append(customer)
        
class Customer(Bank):
    def __init__(self,cust_id,cust_name,dob,contact_no,accNo,acc_type,balance,card_no,card_pin,cvv):
        self.__cust_id = cust_id
        self.__cust_name = cust_name
        self.__dob = dob
        self.__contact_no = contact_no
        self.__accNo = accNo
        self.__acc_type = acc_type
        self.__balance = balance
        self.__card_no = card_no
        self.__card_pin = card_pin
        self.__cvv = cvv
        
        # whenver a new customer object is instantiated the customer data will diretly stored into a csv file 
        if f'{self.__cust_id}.csv' not in os.listdir():
            with open(f'{cust_id}.csv','w') as customer_data:
                data = f'''Customer Id,Customer_name,Dob,contact_info,Account number,Account type,Account balance,Card number,Card pin,CVV\n{cust_id},{cust_name},{dob},{contact_no},{accNo},{acc_type},{balance},{card_no},{card_pin},{cvv}'''

                customer_data.write(data)
        else:
            print("User already Exist")
            

class ATM:
    
    def __init__(self):
        
        # So it will read csv file and return data in pandas DataFrame format and that pandas Data frame will be assigned to a attribute
        # named user
        try :
            self.user = pd.read_csv('12345678.csv')
        except Exception:
            print("There is an problem with our server please try again")
        
    def update_info(self):
            # Updating file data after transaction
            # Here we are saving data based on customer id
            customer_id = f"{self.user['Customer Id'][0]}.csv"
            self.user.to_csv(customer_id)
    
    def print_mini_statement(self):
        customer_id = self.user['Customer Id'][0]
        try:
            with open(f'{customer_id}_trans.txt','r') as file:
                data = file.read().split("\n")
                for i in data:
                    print(i)
        except Exception:
            print("No transcations recorded until now")
            
    
    def update_transactions(self,info):
        customer_id = self.user['Customer Id'][0]
        # based on customer id we are saving the transcation
        with open(f"{customer_id}_trans.txt",'a') as file:
            file.write("\n"+info+"\n")
        
    def fetch_balance(self):
        
        user_details = self.user
        
        print("Current Balance is ",user_details['Account balance'][0])
        
    def withdraw(self):
        
        withdraw_amount = float(input("Enter amount to withdraw :"))
        
        balance = self.user['Account balance'].values
        
        if withdraw_amount <= balance:
            balance = balance - withdraw_amount
            self.user['Account balance'] = balance
            print(f"Amount {withdraw_amount} is debited from your account")
            print(f"Remaining Balance is {balance}")
            
            # Updating customer data after changing it
            self.update_info()
            
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
        
            today = date.today()
            
            transction_info = f"Amount of {withdraw_amount} is debited from account on {current_time} {today}"
            self.update_transactions(transction_info)

            
        else:
            print("Insufficient Balance")
    
    def change_pin(self):
        choice = input("Do you want to change pin (Y/N)")
        
        if choice == 'Y':
            phone_number = input("Enter your mobile number :")
            registerd_number = self.user['contact_info'][0]
            print(registerd_number)
            if registerd_number == int(phone_number):
                    print(f"OTP sent to your registered {phone_number}")
                    
                    new_pin = input("Enter pin")
                    re_enter = input("Re enter your pin")
                    
                    if new_pin == re_enter:
                        self.user['Card pin'] = int(new_pin)
                        # Updating new data into csv file
                        self.update_info()
                        
                        print("You are successfully changed your pin")
                    else:
                        print("Please check the pin")
            else:
                print("This number is not registerd with your account")
              

            
            

bank.create_account()
atm = ATM()              
                        
            
def menu():
        choice = int(input("CHOOSE AN OPTION:"))
        if choice == 1:
            atm.withdraw()
        elif choice == 2:
            atm.fetch_balance()
        elif choice == 3:
            atm.print_mini_statement()
        elif choice == 4:
            atm.change_pin()
        else:
            print("Enter an valid option")

        ch = input("\nDo you want to make another transaction (Y/N)")
        if ch == 'Y':
            menu()
        else:
            print("Thank you for using our services visit again \n")
            return
                    
        
    


                   

print("===================================== WELCOME TO ATM ==========================================================")
print("\n\t\t\t\tPlease insert your card")
time.sleep(1)
print("\n\t\t\t\t\tvalidating",end='')
for _ in range(6):
    print(".",end='')
    time.sleep(1)
entered_pin = input("\nEnter your 4 digit pin \n")

if atm.user['Card pin'][0] == int(entered_pin):
    
    print("\n=====================================================================================================================================\n")
    print(f"\n\t\t\t\t\t\tHello Mr.{atm.user['Customer_name'][0]}")
    print("======================================================================================================================================")
    print("\n\n\t\t\t\t1.WITHDRAWL\t\t\t2.BALANCE INQUIRY")
    print("\n\n\n\t\t\t\t3.MINI STATEMENT\t\t4.CHANGE PIN")
    print("\n\n======================================================================================================================================")
    menu()
    
else:
    raise WrongPinException()
  


# 

# In[28]:


atm.print_mini_statement()
bank.customers_info
    


# In[23]:


atm.user


# 

# In[ ]:





# In[25]:


atm.withdraw()


# In[165]:


atm.user['Account balance'][0]


# In[ ]:





# In[185]:


atm.update_transactions()


# In[26]:


atm.print_mini_statement()


# In[ ]:




