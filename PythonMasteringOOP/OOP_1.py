class LightSwitch:
    """A Light Switch class that turns ON and OFF the light
       and adjusts its brightness level if the light is ON"""
    def __init__(self):
        self.isOn = 'OFF'
        self.brightness_level = 0

    def __str__(self) -> str:
        return 'This is an object it is an instance of a class'

    def turn_on(self):
        if self.isOn == 'OFF':
            self.isOn = 'ON'
            self.brightness_level = 6

    def turn_off(self):
        self.isOn = 'OFF'
        self.brightness_level = 0

    def raise_brightness(self):
        if self.isOn != 'OFF':
            if self.brightness_level < 10:
                self.brightness_level += 1
            else:
                print('Max Brightness Level\n')
        else:
            print('LIGHT SWITCH IS TURNED OFF '
                  'CANNOT RAISE LEVEL')

    def lower_brightness(self):
        if self.isOn != 'OFF':
            if self.brightness_level > 1:
                self.brightness_level -= 1
            else:
                print('Minimum Brightness Level\n')
        else:
            print('LIGHT SWITCH IS TURNED OFF '
                  'CANNOT LOWER LEVEL')

    def show(self):
        print(f'Light switch is {self.isOn}\n'
              f'Brightness level : {self.brightness_level}\n')


if __name__ == '__main__':
    # lett = 'Hum'
    # num = 5
    # dec = 6.0
    # type_list = []

    # When Light Switch is Turned Off Brightness level will be set to 0
    # When Light Switch is Turned On
    oswitch1 = LightSwitch()
    # print(oswitch1)
    oswitch1.turn_on()
    oswitch1.lower_brightness()
    oswitch1.lower_brightness()
    oswitch1.lower_brightness()
    oswitch1.raise_brightness()
    oswitch1.lower_brightness()
    oswitch1.lower_brightness()
    oswitch1.lower_brightness()
    # oswitch1.lower_brightness()
    oswitch1.turn_on()
    oswitch1.lower_brightness()
    oswitch1.turn_on()
    oswitch1.show()

    # print(type(oswitch1.isOn))

    oswitch2 = LightSwitch()
    # print(oswitch2)
    oswitch2.turn_on()
    oswitch2.raise_brightness()
    oswitch2.raise_brightness()
    oswitch2.raise_brightness()
    oswitch2.raise_brightness()
    oswitch2.lower_brightness()
    oswitch2.turn_on()
    oswitch2.show()

    # print(f'Light Bulb 2 is {oswitch2.turn_off()}')
    # my_list = ['Bacon', False, 56.0, 'C', oswitch1, 44, 8, oswitch2]
    # for i, ele in enumerate(my_list):
    #     print(type(ele))
    #     type_list.append(ele)
    # for i, ele in enumerate(type_list):
    #     print(f'{i} : {ele} | ', end=' ')
