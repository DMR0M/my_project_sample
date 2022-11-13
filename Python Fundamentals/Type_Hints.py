def using_type_hints():
    name: str = 'RR'
    age: int = 23
    sample_list: list[list[int]] = [[23, 44],[19, 20, 46],[3]]
    sample_dict: dict[str, str] = {'RR': 'Rommel', 'JD': 'Joko'}
    sample_dict_1: dict[str, age] = {'RR': 23, 'Rudy': 62}

    for i, ele in enumerate(sample_dict):
        print(f'Data {i+1} = {ele}: {sample_dict[ele]}')

    for i, ele in enumerate(sample_dict_1):
        print(f'Age {i+1} = {ele}: {sample_dict_1[ele]}')
    return sample_dict_1


class Quiz:
    def __init__(self):
        self.quiz: dict[str: list[str]] = {'What is this programming language? ':
                                           ['A. Python', 'B. Java', 'C. C++'],
                                           'Who is the creator of Python? ':
                                           ['A. James Gosling', 'B. Bill Gates',
                                            'C. Guido Van Rossum'],
                                           'Can you slice a tuple? ':
                                           ['A. Yes, B. No'],
                                           'nums = [1, 1, 2, 3, 5, 8]\nWhat is the answer nums[nums[3]]':
                                           ['A. 3', 'B. 8', 'C. 1'],
                                           'It is a design pattern in Python that allows a user '
                                           'to add new functionality to'
                                           'an existing object without modifying its structure.':
                                           ['A. Generators', 'B. Interfaces', 'C. Decorators']}

        self.correct_answer: list[str] = ['A', 'C', 'A', 'B', 'C']
        # User Score
        self.score: int = 0

    def display_quiz(self):
        for i, ele in enumerate(self.quiz):
            print(f'{i+1}. {ele}:\n{self.quiz[ele]}')
            user_answer: str = input('Type your answer: ')
            print('\n')
            if user_answer == self.correct_answer[i]:
                self.score += 1
        print(f'\nYour total score is: {self.score}/'
              f'{len(self.correct_answer)}')


if __name__ == '__main__':
    # x = using_type_hints()
    # print(x)
    player_1 = Quiz()
    player_1.display_quiz()
