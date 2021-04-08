#Register and Login
#To register: (First name, Last name, Email, Password)

#To login: (Email, Password)

#Bank Operations: Register, Login, Current Date and Time, Generate account number, Deposit, Withdraw, Check Balance, Buy airtime, Complaint, Logout.

#Welcome function: To initialize the transaction
#database for account profiles
database = {}

#to generate random number, import random
import random

#mask password
import stdiomask


def welcome():
  print('Welcome to LA Bank')
  ownAccount = int(input('Do you have an account with us? 1. (Yes) 2. (No) \n'))
  if(ownAccount == 1):
    login()
  elif(ownAccount == 2):
    register()  
  else:
    print('Invalid selection, please try again')
    welcome()  

def register():
  print('******* Register here: *******')
  firstName = input('What is your first name? \n')
  lastName = input('What is your last name? \n')
  email = input('What is your email address? \n')
  password = stdiomask.getpass()
  
  accountNumber = generateAccountNumber()

  database[accountNumber] = [ firstName, lastName, email, password ]

  print('Account Profile: Your account has been created')

  print(database)

  print('You can now login: ')

  login()
  

def login():
  print('Please enter your login details here')
  userAccountNumber = int(input('What is your account number? \n'))
  password = stdiomask.getpass()
  

  for accountNumber, userDetails in database.items():
    if(accountNumber == userAccountNumber):
      if(password == userDetails[3]):
        print('Welcome %s %s' % ( userDetails[0], userDetails[1] ))
        from datetime import datetime
        dateAndTime = datetime.now()
        currentDate = dateAndTime.strftime("%B %d, %Y. %H:%M:%S")
        print("Date and Time:", currentDate)

        bankOperations()
       
    else:
      print('Incorrect account number or password, please try again')

      login()    

        
  

def generateAccountNumber():
  return random.randrange(1111111,9999999)

def depositOperation():
  depositAmount = input('How much would you like to deposit? \n')

  print(depositAmount + ' naira has been deposited')

def withdrawalOperation():
  input('How much would you like to withdraw? \n')
  print('Please take your cash')

def buyAirtime():
  networkOption = int(input('What network do you use? 1. MTN, 2. AIRTEL, 3. GLO, 4. 9MOBILE'))

  if(networkOption == 1):
    mtnCard = input('Enter amount: ')
    print(mtnCard + ' airtime purchase successful')
  elif(networkOption == 2):
    airtelCard = input('Enter amount: ')
    print(airtelCard + 'airtime purchase successful')
  elif(networkOption == 3):
    gloCard = input('Enter amount: ')
    print(gloCard + ' airtime purchase successful')
  elif(networkOption == 4):
    nineCard = input('Enter amount: ')
    print(nineCard + ' airtime purchase successful')
  else:
    print('Invalid selection')
    buyAirtime()


def complaintOperation():
  input('What seems to be the problem? \n')
  print('We have recieved your complaint and we will work on it as soon as possible, thank you for banking with us.')      

def bankOperations():
  print('What would you like to do?')
  selectOption = int(input('1. (Deposit), 2. (Withdraw),3. (Buy Airtime), 4. (Make a complaint), 5. exit \n'))

  if(selectOption == 1):
    depositOperation()
  elif(selectOption == 2):
    withdrawalOperation()
  elif(selectOption == 3):
    buyAirtime()
  elif(selectOption == 4):
    complaintOperation()
  elif(selectOption == 5):
    exit()
  else:
    print('Invalid option selected')
    bankOperations()
  




### AUTOMATED BANKING SYSTEM ###

welcome()