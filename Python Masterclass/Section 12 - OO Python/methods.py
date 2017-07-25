# METHODS
'''
Encapsulation: the objects contain the data and the methods that work on that data but doesnt expose the implementation
                to the outsid world
                OOP is not the only way to have encapsulation. The programming lang Modular 2, does this by provding
                modules
                Modular approch - ptyz

Class Constructor -> __new__() and after that __init__() is execued
'''

import datetime
import pytz


class Accounts:
    """ Simple Account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow() # we store the utc time of current location
        return pytz.utc.localize(utc_time)    # but we display the local time to the users

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance # variables with _ (single underscore are meant to be used for internal purposes only)
        self.transaction_list = [(Accounts._current_time(), balance)] # takes care of the inital balance, the balance with which the account was opened
        print("Account created for {}".format(self._name))
        self.showBalance()
    

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        self.showBalance()
        self.transaction_list.append((Accounts._current_time(), amount)) # appending a tuple of time and amount and thus used extra () inside append 
    
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self.transaction_list.append((Accounts._current_time(), -amount))
        else:
            print("The amount must be greater than zero and less than your existing balance {}".format(self.__balance))
        self.showBalance()
        
    
    def showBalance(self):
        print('Balance is {}'.format(self.__balance))
    

    def show_transactions(self):
        # unpacking the tuples stored in the list while iterating
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = 'deposited'
            else:
                trans_type = "withdrawn" # it also checks in the list the amount (if negative or not)
                amount *= -1
            
            print('{:6} {} on {} (local time was {})'.format(amount, trans_type, date, date.astimezone()))
    

if __name__ == '__main__':
    aditya = Accounts('Aditya', 0)
    aditya.showBalance()

    aditya.deposit(1000)
    aditya.withdraw(200)
    aditya.withdraw(900)
    aditya.show_transactions()
    
    # print(aditya.transaction_list) -> shows -200 in the tuple
    print('-----------------------------')
    rajni = Accounts('Rajni', 2000) # giving the initial balance of 2000
    
    # rajni.balance = 10000000000, we can easily change these varibale, but we dont want this
    
    rajni.__balance = 100 # NO EFFECT ON BALANCE 
    
    rajni.deposit(200)
    rajni.withdraw(300)
    rajni.show_transactions()

    print(rajni.__dict__)




'''
Signature: it is the defination of the name and the parameters of the function as well as any return value
we can change the way the methods are implemented as long as we dont change the way thier signature

names starting with _ are non-public, even though there is no such thing in python as this. This is a convention

_ makes it clear it is not intended to be used outside the class, though it can be called outside

though we can call static methods on instances, but performance suffers

attributes whose name starts with a  _ (1 underscore) is for internal purpose only
names are mangled only if the start with __ (2) and not if they are only ended with __
python mangles the name of the attributes whose name start with __ (2)

python mangles the name with __ by prefixing _ClassName with that __variable, so that even if it
is accessed outside the class object.__variable, it's value isnt altered. This way, python hides certain variables (makes them private)

'''