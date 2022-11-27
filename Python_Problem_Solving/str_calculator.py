class WordCalculator:
    """A class that performs arithmetics based on word input"""
    def __init__(self, num_1: str='', num_2: str=''):
        self.x = num_1
        self.y = num_2
        self.uniq = ['one', 'two', 'three', 'four', 'five', 'six',
                     'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
        self.teens = ['thirteen', 'fourteen', 'fifteen', 'sixteen',
                      'seventeen', 'eighteen', 'nineteen']
        self.tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty',
                     'sixty', 'seventy', 'eighty', 'ninety']
        self.hundreds = ['hundred']
        self.thousands = ['thousand']
        
    def create_num(self) -> int:
        try:
            nums_uniq = [n for n in range(1, 13)]
            nums_teens = [n for n in range(13, 20)]
            nums_tens = [n for n in range(20, 100, 10)]
            str_num = self.x.split('-')
            count = 0
            print(str_num)
            for i, s_num in enumerate(str_num):
                if s_num == 'hundred':
                    for num in nums_uniq:
                        count = num * 100
                        return count
                for str_n, num in zip(self.uniq, nums_uniq):
                    if s_num == str_n:
                        count += num
            return count
        
                # if num in self.teens:
                #     for i, ele in enumerate(nums_teens):
                #         if num == ele:
                #             return ele
                # if num in nums_tens:
                #     for i, ele in enumerate(nums_tens):
                #         if num == ele:
                #             return ele
            
        except ValueError:
            return f'Invalid Input\nInput must be string'
    
    def add(self):
        pass
        
    def subtract(self):
        pass
        
    def multiply(self):
        pass
        
    def division(self):
        pass
    

if __name__ == '__main__':
    a = input('Type 1st n: ')
    b = input('Type 2nd n: ')
    
    wc = WordCalculator(a, b)
    print(wc.create_num())
    # help(divmod)