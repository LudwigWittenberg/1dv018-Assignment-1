import random
from src.tasks.task1 import Task1
from src.tasks.task2 import Task2
import timeit
import time

class Task3:
  def __init__(self):
    self.sizes = [1_000, 100_000, 1_000_000]

  def time_task_1(self):
    print("Testing Task 1: ")
    numbers_of_unions = self.get_random_numbers(10, 1)
    random_of_finds = self.get_random_numbers(10, 1)

    print("Numbers of unions:", numbers_of_unions)
    print("Random of finds:", random_of_finds)
    print("")

    for size in self.sizes:
      t1 = Task1(size)
      total_time_union = 0
      total_time_connected = 0

      for _ in range(numbers_of_unions[0]):
        total_time_union += self.time_union(t1, size)

      for _ in range(random_of_finds[0]):
        total_time_connected += self.time_connected(t1, size)

      time_per_union = total_time_union / numbers_of_unions[0]
      time_per_connected = total_time_connected / random_of_finds[0]

      self.print_to_console(size, time_per_union, time_per_connected)
      print("")

  def time_task_2(self):
    numbers_of_unions = self.get_random_numbers(10, 1)

    for _ in range(random_of_finds[0]):
        self.time_connected(t1, size)

  def time_task_2(self):
    print("")
    print("Testing Task 2: ")
    numbers_of_unions = self.get_random_numbers(10, 1)
    random_of_finds = self.get_random_numbers(10, 1)

    print("Numbers of unions:", numbers_of_unions)
    print("Random of finds:", random_of_finds)
    print("")

    for size in self.sizes:
      t2 = Task2(size)
      total_time_union = 0
      total_time_connected = 0

      for _ in range(numbers_of_unions[0]):
        total_time_union += self.time_union(t2, size)

      for _ in range(random_of_finds[0]):
        total_time_connected += self.time_connected(t2, size)

      time_per_union = total_time_union / numbers_of_unions[0]
      time_per_connected = total_time_connected / random_of_finds[0]

      self.print_to_console(size, time_per_union, time_per_connected)
      print("")

  def get_random_numbers(self, size, amount):
    return [random.randint(1, size - 1) for _ in range(amount)]

  def time_connected(self, uf, size):
    num1, num2 = self.get_random_numbers(size, 2)

    elapsed_time = timeit.timeit(lambda: uf.is_connected(num1, num2), number=100)

    return elapsed_time

  def time_union(self, uf, size):
    num1, num2 = self.get_random_numbers(size, 2)

    elapsed_time = timeit.timeit(lambda: uf.add_union(num1, num2), number=100)

    return elapsed_time

  def print_to_console(self, size, total_time_union, total_time_connected):
    print("=============================")
    print(f"Results for size {size}:")
    print(f"Total time for unions: {total_time_union:0.6f} seconds. Iterations: 100")
    print(f"Total time for connected: {total_time_connected:0.6f} seconds. Iterations: 100")