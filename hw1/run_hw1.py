'''

'''

from utils.plate_inferencer import PlateNumberFinder

def plate_num():
    plate_finder = PlateNumberFinder()
    plate_finder.inference()
    print(plate_finder.result)



if __name__ == '__main__':
    
    