
class ConfigFile:
    def __init__(self, file):
        self.file = file
        self.list_vals = []

    def configure_file(self):
        with open(self.file, 'r+') as file:
            lines_read = file.readlines()
            for i, ele in enumerate(lines_read):
                line = ele.strip()
                self.list_vals.append(line.split(':'))

            for i, o_ele in enumerate(self.list_vals):
                change_option = input(f'{i+1}. Change {o_ele}: ')
                for i_ele in range(len(o_ele)):
                    o_ele[1] = change_option
        return self.list_vals

    def change_option(self):
        with open(self.file) as file:
            lines_read = file.readlines()
            line_1 = lines_read[0].split(': ')
            line_1[1] = input('Change to: ')

        with open(self.file, 'w') as file:
            for i, ele in enumerate(lines_read):
                change = ele.replace('ON', line_1[1])
                file.write(change)

        print('Change Successful')
        # return lines_read


