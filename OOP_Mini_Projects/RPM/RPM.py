from random import choice
from colorama import Fore, Style


class RPSGame:
    def __init__(self, username):
        self.username = username

        self.rpm = ['Rock', 'Paper', 'Scissors']
        self.ai_choice = choice(self.rpm)
        self.score = 0
        self.games = 3

    def __str__(self):
        return f'You are user {self.username}\n'

    def display(self):
        return f'Welcome to RPM Game {self.username}!\n'

    def play(self):
        n = 0
        WIN = f'{Fore.GREEN} You Win'
        LOSE = f'{Fore.RED} You Lose'
        DRAW = f'{Fore.CYAN} Draw'

        while n < self.games:
            self.ai_choice = choice(self.rpm)
            user_choice = input(f'{self.rpm}\nType your choice: ')
            if user_choice not in self.rpm:
                print('Invalid choice')
                break
            print(f'Your choice is: {user_choice}\nAI choice is: {self.ai_choice}')
            # If User is rock and AI is scissors
            if user_choice == self.rpm[0].lower and self.ai_choice == self.rpm[2]:
                print(WIN)
                print(Style.RESET_ALL)
                self.score += 1
                n += 1
            # If User is rock and AI is paper
            elif user_choice == self.rpm[0] and self.ai_choice == self.rpm[1]:
                print(LOSE)
                print(Style.RESET_ALL)
                n += 1
            # If User is rock and AI is rock
            elif user_choice == self.rpm[0] and self.ai_choice == self.rpm[0]:
                print(DRAW)
                print(Style.RESET_ALL)
                continue
            # If User is paper and AI is scissors
            elif user_choice == self.rpm[1] and self.ai_choice == self.rpm[2]:
                print(LOSE)
                print(Style.RESET_ALL)
                n += 1
            # If User is paper and AI is paper
            elif user_choice == self.rpm[1] and self.ai_choice == self.rpm[1]:
                print(DRAW)
                print(Style.RESET_ALL)
                continue
            # If User is paper and AI is rock
            elif user_choice == self.rpm[1] and self.ai_choice == self.rpm[0]:
                print(WIN)
                print(Style.RESET_ALL)
                self.score += 1
                n += 1
            # If User is scissors and AI is scissors
            elif user_choice == self.rpm[2] and self.ai_choice == self.rpm[2]:
                print(DRAW)
                print(Style.RESET_ALL)
                continue
            # If User is scissors and AI is paper
            elif user_choice == self.rpm[2] and self.ai_choice == self.rpm[1]:
                print(WIN)
                self.score += 1
                print(Style.RESET_ALL)
                n += 1
            # If User is scissors and AI is rock
            elif user_choice == self.rpm[2] and self.ai_choice == self.rpm[0]:
                print(LOSE)
                print(Style.RESET_ALL)
                n += 1
        return f'Your final score is {self.score} out of {self.games}'


if __name__ == '__main__':
    rps = RPSGame('RR')
    print(rps)
    print(rps.display())
    print(rps.play())
