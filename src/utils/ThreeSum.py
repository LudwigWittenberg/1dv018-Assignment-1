class ThreeSum:
    def find_three_sum(self, nums):
      res = []

      for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
          for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
              if i == j or j == k or i == k:
                continue
              
              tripplets = tuple(sorted([nums[i], nums[j], nums[k]]))
              if tripplets not in res:
                res.append(tripplets)

      return res
