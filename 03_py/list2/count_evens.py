def count_evens(nums):
  c = 0
  for i in nums:
    if (i % 2 == 0):
      c += 1
  return c
