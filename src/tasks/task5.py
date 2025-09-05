import random
from src.utils.FasterThreeSum import FasterThreeSum
from src.utils.GetRadomNumbers import get_random_numbers

class Task5:
  def __init__(self, array):
    self.array = array
    self.faster_three_sum = FasterThreeSum()

  def run(self):
    # Get the correct number of random numbers
    result = self.faster_three_sum.find_three_sum(self.array)
    return self.array, result
