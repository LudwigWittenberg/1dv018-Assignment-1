from src.tasks.task1 import Task1
from src.tasks.task2 import Task2
from src.tasks.task3 import Task3
from src.tasks.task4 import Task4
from src.tasks.task5 import Task5
from src.tasks.task6 import Task6
from src.utils.GetRadomNumbers import get_random_numbers

def main():
  # print("----------- Task 1 -----------")

  # t1 = Task1(10)

  # print(t1.get_list())

  # t1.add_union(1, 2)
  # t1.add_union(2, 3)

  # print(t1.get_list())
  # print("Is 1 connected to 3?", t1.is_connected(1, 3))

  # print("")
  # print("----------- Task 2 -----------")

  # t2 = Task2(50)

  # print(t2.get_list())

  # t2.add_union(1, 2)
  # t2.add_union(2, 3)
  # t2.add_union(33, 40)
  # t2.add_union(20, 45)

  # print(t2.get_list())
  # print("Is 1 connected to 3?", t2.is_connected(1, 3))
  # print("Is 33 connected to 34?", t2.is_connected(33, 34))
  # print("Is 22 connected to 4?", t2.is_connected(22, 4))

  # print("")
  # print("----------- Task 3 -----------")

  # t3 = Task3()

  # t3.time_task_1()
  # t3.time_task_2()

  print("")
  print("----------- Task 4 -----------")

  array = get_random_numbers(4)
  t4 = Task4(array)
  nums, result = t4.run()
  print("Random Numbers:", nums)
  print("Three Sum Combinations:", result)

  print("")
  print("----------- Task 5 -----------")

  array = get_random_numbers(4)
  t5 = Task5(array)
  nums, result = t5.run()
  print("Random Numbers:", nums)
  print("Three Sum Combinations:", result)

  print("")
  print("----------- Task 6 -----------")

  t6 = Task6()

  t6.time_task_4()
  t6.time_task_5()

main()