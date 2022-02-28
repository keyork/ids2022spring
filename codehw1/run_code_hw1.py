'''

'''

from utils.plate_inferencer import PlateNumberFinder
from utils.repeat_counter import RepeatCounter
from utils.db_processor import DBProcessor

from data.base_data import *

def plate_num():

    plate_finder = PlateNumberFinder()
    plate_finder.inference()
    print(plate_finder.result)


def count_repeat():

    input_str = INPUT_STR
    repeat_counter = RepeatCounter()
    repeat_counter.split(input_str)
    repeat_counter.count()
    print(repeat_counter.result)


def process_db():

    data_processor = DBProcessor(DB_DATA)

    print(data_processor.df_data)
    data_processor.show_example(3)
    data_processor.get_spec_col(['animal', 'age'])
    data_processor.get_spec_row_col([2,3,7], ['animal', 'age'])
    data_processor.get_age_gt_x(3)
    data_processor.get_age_nan()
    data_processor.get_age_bet_l_u(2, 4)
    data_processor.change_data('f', 'age', 1.5)
    print(data_processor.df_data)

if __name__ == '__main__':
    
    plate_num()
    count_repeat()
    process_db()