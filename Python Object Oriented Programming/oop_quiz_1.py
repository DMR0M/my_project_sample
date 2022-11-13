class Restaurant:
    def __init__(self, name):
        self.name = name
        self.flavors = ['Mint', 'Matcha', 'Chocolate', 'Bubblegum', 'Cookies & Cream',
                        'Pistachio', 'Strawberry']


class IceCreamStand(Restaurant):
    def show(self):
        print(f'Hello there {self.name} these are the flavors: ')
        for i, flavor in enumerate(self.flavors):
            print(f'Flavor {i+1} : {flavor}')


vendor = IceCreamStand('RR')
vendor.show()
