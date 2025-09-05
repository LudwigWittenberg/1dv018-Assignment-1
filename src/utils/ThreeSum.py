class ThreeSum:
    def find_three_sum(self, nums):
      res = []

      for i, vi in enumerate(nums):
        for j, vj in enumerate(nums):
          for k, vk in enumerate(nums):
            if i == j or i == k or j == k:
              continue
            tripplets = sorted([vi, vj, vk])
            if vi + vj + vk == 0 and tripplets not in res:
              res.append(tripplets)

      return res