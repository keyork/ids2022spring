'''

'''

import pandas as pd

class RepeatCounter:

    def __init__(self):

        self.input_list = None
        self.result = {}


    def split(self, input_str):

        self.input_list = input_str.lower().split()

    def count(self):

        self.result = pd.value_counts(self.input_list)


# debug

if __name__ == '__main__':
    input_str = 'Hello python hello java'
    repeat_counter = RepeatCounter()
    repeat_counter.split(input_str)
    repeat_counter.count()

    print(repeat_counter.result)
