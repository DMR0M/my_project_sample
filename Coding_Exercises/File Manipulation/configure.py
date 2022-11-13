from config_class import ConfigFile


if __name__ == '__main__':
    while FileNotFoundError:
        try:
            choose_file = input('Enter the file you want to configure: ')
            conf = ConfigFile(choose_file)
            # print(conf.configure_file())
            conf.change_option()
            break
        except FileNotFoundError:
            print('File Not Found')
