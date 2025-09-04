from src.utils.QuickFind import QuickFind
import time

class Task1:
  def __init__(self, num):
    self.uf = QuickFind(num)

  def add_union(self, num1, num2):
    self.uf.union(num1, num2)

  def is_connected(self, num1, num2):
    is_connected = self.uf.connected(num1, num2)

    return is_connected

  def get_list(self):
    return self.uf.get_list()