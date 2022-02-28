'''

'''

import pandas as pd
import numpy as np

class DBProcessor:

    def __init__(self, data):

        self.df_data = pd.DataFrame(data)
        self.example = None
        self.spec_cols = None
        self.spec_rows_cols = None
        self.age_gt_x = None
        self.age_nan = None
        self.age_bet_l_u = None


    def show_example(self, show_num):

        self.example = self.df_data[0:show_num]


    def get_spec_col(self, col_name):

        self.spec_cols = self.df_data.loc[:, col_name]


    def get_spec_row_col(self, row_idx, col_name):

        self.spec_rows_cols = self.df_data.loc[row_idx, col_name]


    def get_age_gt_x(self, l_bound):

        self.age_gt_x = self.df_data[self.df_data['age'] > l_bound]
        print(self.age_gt_x)


    def get_age_nan(self):

        self.age_nan = self.df_data[np.isnan(self.df_data['age'])]
        print(self.age_nan)


    def get_age_bet_l_u(self, l_bound, u_bound):

        self.age_bet_l_u = self.df_data[(self.df_data['age'] >= l_bound) & (self.df_data['age'] <= u_bound)]
        print(self.age_bet_l_u)


    def change_data(self, id, item, value):

        target_idx = self.df_data[self.df_data['id'] == id].index.tolist()[0]
        self.df_data.loc[target_idx, item] = value

