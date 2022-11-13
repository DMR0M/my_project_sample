class Account:
    """A Bank class that creates a bank account for a user object
       User transactions include:
            1) Deposit
            2) Withdraw
            3) Show Balance
            4) Show Account Info
       Limitations:
            1) User validation password for each transactions
            2) Cannot log in to an existing bank account
            3) Data inputted only stored in a text file
            4) No GUI yet                       """

    def __init__(self, name, balance, password):
        self.username = name
        self.balance = balance
        self.password = password

    def deposit(self, amount, password):
        try:
            if password == self.password:
                if amount >= 500:
                    self.balance += amount
                    print(f'\nYou have deposited {amount} pesos\n')
                else:
                    print('\nCannot deposit below 500')
            else:
                print('Authentication Failure')
        except ValueError:
            print('\nInvalid Input')
            raise exit()

    def withdraw(self, amount, password):
        try:
            if password == self.password:
                if amount >= 500:
                    self.balance -= amount
                    print(f'\nYou have withdrawn {amount} pesos')
                else:
                    print('\nCannot withdraw below 500')
            else:
                print('Authentication Failure')
        except ValueError:
            print('\nInvalid Input')
            raise exit()

    def get_balance(self, password):
        if password == self.password:
            print(f'Your account balance is {self.balance}')
        else:
            print('Authentication Failure')

    def show_acct_details(self, password):
        if password == self.password:
            print(f'\nYour account name: {self.username}\n'
                  f'Your account balance: {self.balance}\n'
                  f'Your account password: {self.password}\n')
        else:
            print('Authentication Failure')


# class AbortTransaction(Exception):
#     """Custom Exception"""
#     pass

