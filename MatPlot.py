from src.utils.Graphs.Task3GenerateGraphs import Task3GenerateGraphs
from src.utils.Graphs.Task6GenerateGraphs import Task6GenerateGraphs

def matPlot():
  print("Generating Graphs for Task 3")
  t3 = Task3GenerateGraphs()
  t3.time_task_1()
  t3.time_task_2()

  print("Generating Graphs for Task 6")
  t6 = Task6GenerateGraphs()
  t6.time_task_4()
  t6.time_task_5()

matPlot()