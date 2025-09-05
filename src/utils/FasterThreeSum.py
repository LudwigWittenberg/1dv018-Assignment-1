class FasterThreeSum:
  def find_three_sum(self, nums):
    nums.sort()
    res = []
    n = len(nums)

    for index in range(n -2):
      if index > 0 and nums[index] == nums[index - 1]:
        continue

      left, right = index + 1, n - 1
      while left < right:
        total = nums[index] + nums[left] + nums[right]

        print(left, right, total)
        
        if total == 0:
          res.append([nums[index], nums[left], nums[right]])

          while left < right and nums[left] == nums[left + 1]:
            left += 1

          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1

        elif total < 0:
          left += 1
        else:
          right -= 1

    return res