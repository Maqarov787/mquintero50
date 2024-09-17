#Marco Quintero
#Ghidorah
#SoftDev
#K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#2024-09-16
#time spent: <0.1 hours>
def big_diff(nums):
  smallest = nums[0];
  largest = nums[0];
  for i in nums:
    if (i < smallest):
      smallest = i
    if (i > largest):
      largest = i
  return abs(smallest - largest)