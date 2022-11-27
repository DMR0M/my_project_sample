class Quiz:
    memory = []
    """A Quiz Mini-game Class"""
    def __init__(self, name: str):
        self.name = name
        self.questions = ('2**5 is equals to: ', 'log3(81) is equals to: ', '550 / 225: ')
        self.ans = (32, 4, 2.4)
        self.score = 0
    
    def __repr__(self):
        return f'Welcome to PyQuiz {self.name}!'
    
    @property
    def conf_name(self):
        return self.name
    
    @conf_name.setter
    def conf_name(self, new_name):
        self.name = new_name    
    
    def play(self) -> None:
        try:
            for i, ele in enumerate(self.questions):
                print(f'\nQuestion {i+1}: \n{ele}', end = ' ')
                u_ans = float(input(''))
                self.score += 1 if u_ans == self.ans[i] else 0
            print(f'\nTotal Score: {self.score}/{len(self.questions)}')
        except ValueError:
            print('Invalid answer\nExited Quiz')
        
    def show(self):
        pass


if __name__ == '__main__':
    username = input('Type your username: ')
    q = Quiz(username)
    print(q)
    q.name = 'Rommel'
    print(q)
    q.play()
    
           