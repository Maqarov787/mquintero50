def big_diff(nums):
  smallest = nums[0];
  largest = nums[0];
  for i in nums:
    if (i < smallest):
      smallest = i
    if (i > largest):
      largest = i
  return abs(smallest - largest)
