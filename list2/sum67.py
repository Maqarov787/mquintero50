#Marco Quintero
#Ghidorah
#SoftDev
#K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#2024-09-16
#time spent: <0.1 hours>
def sum67(nums):
  sum = 0
  i = 0
  while(i < len(nums)):
    if (nums[i] == 6):
      j = 1
      tempi = i
      while(j + tempi < len(nums)):
        if (nums[j + tempi] == 7):
          tempi += len(nums)
        else:
          j += 1
      i += j
    else:
      sum += nums[i]
    i += 1
  return sum