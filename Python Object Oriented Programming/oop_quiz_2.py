from Privileges import ListPrivileges, Configurations


class User(ListPrivileges):
    def __init__(self):
        self.name: str = 'RR'

    def modify_func(self):
        print('I can modify')


class Admin(User):
    def __init__(self):
        # Super keyword followed by __init__ inherits the methods of a parent class
        super().__init__()
        self.privileges: list = [ListPrivileges._privilege_1,
                                 ListPrivileges._privilege_2,
                                 ListPrivileges._privilege_3]


class DisplayPrivileges(Admin):
    def __init__(self):
        super().__init__()

    def show_admin_privileges(self):
        print(f'Hello there admin {self.name} these are the privileges: ')
        for i, privilege in enumerate(self.privileges):
            print(f'{i+1} {privilege}')


if __name__ == '__main__':
    admin_1 = DisplayPrivileges()
    admin_1.show_admin_privileges()
    admin_1.modify_func()
