
"""
working on object car
types
method: details(bukunmi)
method: drive(pelumi)
method: drift(boluwatife)
method: park(ayodele)
method: reverse(toluwanimi)
method: ignition(maimunat)
"""
# class Cars():
#     tyre=4
#     engine=1
#     bonnet=1
#     brake=1
#     accelerator=1
#     def __init__(self, color, make, model,year, price, engin_type):
#         self.color=color
#         self.maker=make
#         self.model=model
#         self.year=year
#         self.price=price
#         self.engin_type=engin_type



# Maimunat just joined..😊✌️
# The prices are in dollars....
from colorama import init,Fore,Back,Style
init()
def carlist():   
    Vehicles = [
        ('TESLA',1200000),
        ('MERCEDES BENZ',300000),
        ('TOYOTA CAMRY',150000),
        ('ROLLS ROYCE',79000),
        ('AUDI',120000),
        ('MITSUBISHI',90000),
        ('TOYOTA COROLLA',70000),
        ('HONDA',60000),
        ('HYUNDIA',30000),
        ('LEXUS',80000)
            ]
    
    global models
    global prices
    

    models = []
    prices = []
    for model,price in Vehicles:
         models.append(model)
         print(model)
         prices.append(price)        

    intro()
def intro():
    user = input('You are about to make payment now,kindly input the name of the vehicle purchased:  ').strip().upper()
    if user in models:
         _index = models.index(user)
         global _status1
         _status1 = prices[_index]
        #  order.append(_status1)
         print('It costs $',_status1)
         option = input(' 1.Full payment\n 2.Half payment\n Input a payment option: ')
         if option.strip() == '1':
              payment_plan()
         elif option.strip() == '2':
              payment_plan()
         else:
              prices(Fore.RED + 'Invalid choice.Please try again.')
              print(Style.RESET_ALL)
              exit()
              
              
    else:
         print(Fore.RED + 'Kindly input the correct name of the vehicle purchased!!') 
         print(Style.RESET_ALL)
         intro()

def payment_plan():
     met = input(' 1.Bank Payment\n 2. Cash payment\n Enter your preferred payment method: ')
     if met.strip() == '1':
           bank_payment()
     elif met.strip() == '2':
          cash_payment()
     else:
          prices(Fore.RED + 'Invalid choice.Please try again.')
          print(Style.RESET_ALL)
          payment_plan()
     
def bank_payment():
     print('Bank payment selected.')
     card_no = int(input('Enter your card number: '))            
     ccv = int(input('Enter your cvv: ') )           
     card_pin = int(input('Enter your four digit pin: ')) 
     amount =float(input('Enter payment amount: '))
     print(Fore.GREEN + f'Payment successful. ${amount} deducted from your account.\n Thanks for your patronage..😊')
     print(Style.RESET_ALL)

def cash_payment():
     print('Cash payment selected')
     amount =float(input('Enter payment amount: '))
     print(Fore.GREEN + f' Payment successful. Kindly hand over the cash to the Cashier .\n Thanks for your patronage..😊')
     print(Style.RESET_ALL)

carlist()
   

      

