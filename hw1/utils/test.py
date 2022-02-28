

from plate_inferencer import *
from repeat_counter import *
from db_processor import *

from numpy import NaN


#################################
# test of plate_inferencer
#################################

plate_finder = PlateNumberFinder()
plate_finder.inference()
print(plate_finder.result)


#################################
# test of repeat_counter
#################################

input_str = 'Hello python hello java'
repeat_counter = RepeatCounter()
repeat_counter.split(input_str)
repeat_counter.count()

print(repeat_counter.result)


#################################
# test of db_processor
#################################

DB_DATA = [
    {'id':'a', 'animal':'cat', 'age':2.5, 'visits':1, 'priority':'yes'},
    {'id':'b', 'animal':'cat', 'age':3.0, 'visits':3, 'priority':'yes'},
    {'id':'c', 'animal':'snake', 'age':0.5, 'visits':2, 'priority':'no'},
    {'id':'d', 'animal':'dog', 'age':NaN, 'visits':3, 'priority':'yes'},
    {'id':'e', 'animal':'dog', 'age':5.0, 'visits':2, 'priority':'no'},
    {'id':'f', 'animal':'cat', 'age':2.0, 'visits':3, 'priority':'no'},
    {'id':'g', 'animal':'snake', 'age':4.5, 'visits':1, 'priority':'no'},
    {'id':'h', 'animal':'cat', 'age':NaN, 'visits':1, 'priority':'yes'},
    {'id':'i', 'animal':'dog', 'age':7.0, 'visits':2, 'priority':'no'},
    {'id':'j', 'animal':'dog', 'age':3.0, 'visits':1, 'priority':'no'}
]

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