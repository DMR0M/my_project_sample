# Read and Write to files in Python
from dataclasses import dataclass


class FileManipulation:
    def __init__(self, text1, text2):
        self.MAIN_FILE = 'write_file_using_python.txt'
        self.notification = 'Successful'
        self.text1 = text1
        self.text2 = text2

    # Context Manager
    def read_file(self):
        with open(self.MAIN_FILE, 'r') as file:
            print(file.read())

    def write_files(self):
        with open(self.MAIN_FILE, 'a') as text_sample:
            text_sample.write(f'\n{text1}')
            text_sample.write(f'\n{text2}')
        print(self.notification)


@dataclass()
class FindContacts:
    find: str = 'rommeldm87@gmail.com'

    @staticmethod
    def find_specified():
        with open('contacts.txt', 'r') as contact_info:
            contact_info = contact_info.readlines()

        for i, contact in enumerate(contact_info):
            if FindContacts.find in contact:
                # Removes White Spaces for each iteration
                a: str = contact.strip()
                print(f'Found {a} at line {i+1}')


if __name__ == '__main__':
    text1: str = input('Type text 1 to append: ')
    text2: str = input('Type text 2 to append: ')
    file_append = FileManipulation(text1, text2)
    file_append.write_files()
