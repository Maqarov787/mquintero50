#Marco Quintero
#Ghidorah
#SoftDev
#K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#2024-09-16
#time spent: <0.1 hours>
def has22(nums):
  for i in range(len(nums) - 1):
    if(nums[i] == 2 and nums[i + 1] == 2):
      return True
  return False