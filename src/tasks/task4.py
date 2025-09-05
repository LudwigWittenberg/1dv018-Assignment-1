import random
from src.utils.ThreeSum import ThreeSum
from src.utils.GetRadomNumbers import get_random_numbers

class Task4:
  def __init__(self, array):
    self.array = array
    self.three_sum = ThreeSum()

  def run(self):
    # Get the correct number of random numbers
    result = self.three_sum.find_three_sum(self.array)
    return self.array, result
