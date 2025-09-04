class PrintHelper:
  def __init__(self):
    pass

  def new_task(self, task_id):
    print("")
    print("------------ Task", task_id, "------------")

    
# # PRINT HELPERS

# def print_connected(uf, num1, num2):
#   # Calculate time for operation
#   # tic = time.perf_counter()
#   is_connected = uf.connected(num1, num2)
#   # toc = time.perf_counter()

#   print("Is", num1, "connected to", num2, "?", is_connected)
#   print(f"Connected operation took {toc - tic:0.4f} seconds")
#   print("")

# def print_union(uf, num1, num2):
#   print(num1, "unioned with", num2)

#   # Calculate time for operation
#   # tic = time.perf_counter()
#   uf.union(num1, num2)
#   # toc = time.perf_counter()

#   print(f"Union operation took {toc - tic:0.4f} seconds")
#   print("")