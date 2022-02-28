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
