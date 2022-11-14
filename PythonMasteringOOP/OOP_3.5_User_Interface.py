from OOP_3_Banking_Class import Account
# class Bank:
#     def __init__(self):
#         self.account_dict = {}
#         self.account_num = 0
#
#     def create_account(self, name, amount, password):
#         user_account = Account(name, amount, password)
#         account_i = self.account_num
#         self.account_dict[account_i] = user_account
#         self.account_num += self.account_num
#         return account_i
#
#     def open_account(self):
#         user_acct_num = input('Register Username: ')


if __name__ == '__main__':
    def display_options() -> None:
        print('\nPress q to quit\n'
              'Press d to deposit\n'
              'Press w to withdraw\n'
              'Press e to display current balance\n'
              'Press s to display account details\n')

    def transaction(option, account) -> None:
        invalid_input = True
        while invalid_input:
            if option == 'q':
                exit()
            elif option == 'd':
                deposit_val = int(input('Enter amount to deposit: '))
                validation = input('Input account password: ')
                account.deposit(deposit_val, validation)
                break
            elif option == 'w':
                withdraw_val = int(input('Enter amount to withdraw: '))
                validation = input('Input account password: ')
                account.withdraw(withdraw_val, validation)
                break
            elif option == 'e':
                validation = input('Input account password: ')
                account.get_balance(validation)
                break
            elif option == 's':
                validation = input('Input account password: ')
                account.show_acct_details(validation)
                break
            else:
                invalid_input = False
                print('INVALID INPUT OPTION')

    does_not_match = True
    bank_accounts: list[dict] = []
    print('\n*** PyBANK ***\n')
    acct1_input_name = input('Register Username: ')
    while does_not_match:
        acct1_input_password = input('Create Password: ')
        acct1_input_confirm = input('Confirm Password: ')
        if acct1_input_password != acct1_input_confirm:
            print('Password does not match\nPlease try again')
        else:
            does_not_match = False
            acct1_input_balance = int(input('Deposit Balance: '))
            print('\nAccount Successfully Created!')
            print(f'You have deposited {acct1_input_balance} pesos to created account!\n')

            # Instantiate
            acct1 = Account(acct1_input_name, acct1_input_balance, acct1_input_password)

            # Then store user data to bank accounts list
            user_data = {'Username ': acct1.username, 'Password ': acct1.password,
                         'Initial Deposit ': acct1.balance}
            bank_accounts.append(user_data)

            # Store user account object to text file
            with open('User_Bank_Accounts.txt', 'a') as users_data_file:
                for ele_x in bank_accounts:
                    users_data_file.write(f'\nUser: \n')
                    for j, ele_y in enumerate(ele_x):
                        users_data_file.write(f'\t{ele_y} : {ele_x[ele_y]}\n')

                        
            while True:
                # Access to bank transactions
                display_options()
                user_option = input('Enter Transaction: ')
                transaction(user_option.lower(), acct1)

                try_again_input = input('\nDo you want to make another transaction: '
                                        '\npress [q] to quit\npress [e] to make another transaction\n')

                if try_again_input.lower() == 'q':
                    exit()
                elif try_again_input.lower() == 'e':
                    continue
                else:
                    print('INVALID INPUT\nPlease try again')
                    continue
