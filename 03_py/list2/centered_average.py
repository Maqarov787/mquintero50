#Marco Quintero
#Ghidorah
#SoftDev
#K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#2024-09-16
#time spent: <0.1 hours>
def centered_average(nums):
  sum = 0
  count = 0
  nums.sort()
  for i in range(1, len(nums) - 1):
      sum += nums[i]
      count += 1
  if (count == 0):
    return sum
  return sum / count