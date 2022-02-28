'''

'''

from math import sqrt

class PlateNumberFinder:

    def __init__(self):
        
        self.first_num = None
        self.last_num = None
        self.result = None

    def inference(self):

        for self.first_num in range(1, 10):
            for self.second_num in range(1, 10):
                if self.second_num == self.first_num:
                    continue
                inference_num = self.first_num*(1000+100) + self.second_num*(10+1)
                if sqrt(inference_num) == int(sqrt(inference_num)):
                    self.result = inference_num
                    break


# debug

if __name__ == '__main__':

    plate_finder = PlateNumberFinder()
    plate_finder.inference()
    print(plate_finder.result)
    