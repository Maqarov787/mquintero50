#Marco Quintero
#Ghidorah
#SoftDev
#K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#2024-09-16
#time spent: <0.1 hours>
def sum13(nums):
  sum = 0
  i = 0
  while(i < len(nums)):
    if (nums[i] == 13):
      i += 1
    else:
      sum += nums[i]
    i += 1
  return sum