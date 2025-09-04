class UnionFind:
  def __init__(self, size):
    self.list = list(range(size))

  def union(self, index, value):
    a_id = self.list[index]
    b_id = self.list[value]

    for i in range(len(self.list)):
      if self.list[i] == a_id:
        self.list[i] = b_id

  def connected(self, index, value):
    return self.list[index] == self.list[value]