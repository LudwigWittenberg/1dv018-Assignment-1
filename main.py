from src.tasks.task1 import Task1
from src.tasks.task2 import Task2
from src.tasks.task3 import Task3
from src.tasks.task4 import Task4
from src.tasks.task5 import Task5

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

  t4 = Task4(4)
  t4.run()

  print("")
  print("----------- Task 5 -----------")

  t5 = Task5(4)
  t5.run()

main()