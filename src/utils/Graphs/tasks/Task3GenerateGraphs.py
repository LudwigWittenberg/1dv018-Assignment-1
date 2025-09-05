import random
from src.tasks.task1 import Task1
from src.tasks.task2 import Task2
import timeit
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

class Task3GenerateGraphs:
  def __init__(self):
    self.sizes = [10_000, 30_000, 50_000, 70_000, 100_000]
    # Create figure and subplots at initialization
    self.fig = plt.figure(figsize=(8, 10))
    self.union_ax = self.fig.add_subplot(2, 1, 1)
    self.connected_ax = self.fig.add_subplot(2, 1, 2)

  def time_task_1(self):
    print("Testing Task 1: ")
    numbers_of_unions = self.get_random_numbers(10, 1)
    random_of_finds = self.get_random_numbers(10, 1)

    print("Numbers of unions:", numbers_of_unions)
    print("Number of finds:", random_of_finds)
    print("")

    sizes_list = []
    union_times = []
    connected_times = []

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

      sizes_list.append(size)
      union_times.append(time_per_union)
      connected_times.append(time_per_connected * 1000) # Convert to milliseconds

      self.print_to_console(size, time_per_union, time_per_connected)
      print("")

    # Plot Task1 results on shared figure
    self.union_ax.plot(sizes_list, union_times, marker='o', color='blue', label='QuickFind')
    self.connected_ax.plot(sizes_list, connected_times, marker='o', color='blue', label='QuickFind')

  def time_task_2(self):
    print("")
    print("Testing Task 2: ")
    numbers_of_unions = self.get_random_numbers(10, 1)
    random_of_finds = self.get_random_numbers(10, 1)

    print("Numbers of unions:", numbers_of_unions)
    print("Number of finds:", random_of_finds)
    print("")

    sizes_list = []
    union_times = []
    connected_times = []

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

      sizes_list.append(size)
      union_times.append(time_per_union)
      connected_times.append(time_per_connected * 1000) # Convert to milliseconds

      self.print_to_console(size, time_per_union, time_per_connected)
      print("")

    # Plot Task2 results on shared figure
    self.union_ax.plot(sizes_list, union_times, marker='o', color='orange', label='UnionFind')
    self.connected_ax.plot(sizes_list, connected_times, marker='o', color='orange', label='UnionFind')
    
    # Setup subplot formatting and save the figure
    self.union_ax.set_xlabel("n elements")
    self.union_ax.set_ylabel("union time (s)")
    self.union_ax.set_xticks([0, 20000, 40000, 60000, 80000, 100000])
    self.union_ax.grid(True)
    self.union_ax.legend()

    self.connected_ax.set_xlabel("n elements")
    self.connected_ax.set_ylabel("connected time (ms)")
    self.connected_ax.set_xticks([0, 20000, 40000, 60000, 80000, 100000])
    self.connected_ax.grid(True)
    self.connected_ax.legend()

    # Add a title for the entire figure
    plt.suptitle("Union and Connected Times for QuickFind and UnionFind", fontsize=16)
    plt.tight_layout()
    # Adjust layout to make room for the title
    plt.subplots_adjust(top=0.92)
    plt.savefig("graphs/task3_combined_graph.png")

  def get_random_numbers(self, size, amount):
    return [random.randint(1, size - 1) for _ in range(amount)]

  def time_connected(self, uf, size):
    num1, num2 = self.get_random_numbers(size, 2)

    elapsed_time = timeit.timeit(lambda: uf.is_connected(num1, num2), number=1000)

    return elapsed_time

  def time_union(self, uf, size):
    num1, num2 = self.get_random_numbers(size, 2)

    elapsed_time = timeit.timeit(lambda: uf.add_union(num1, num2), number=1000)

    return elapsed_time

  def print_to_console(self, size, total_time_union, total_time_connected):
    print("=============================")
    print(f"Results for size {size}:")
    print(f"Total time for unions: {total_time_union:0.6f} seconds. Iterations: 1000")
    print(f"Total time for connected: {total_time_connected:0.6f} seconds. Iterations: 1000")