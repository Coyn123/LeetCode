def majorityElement(nums: list[int]) -> int:
  freq = {}
  for num in nums:
    if num not in freq:
      freq[num] = 1
    else:
      freq[num] += 1
    maxCount = 0
    keyTracker = 0
  for key, value in freq.items():
    if value > maxCount:
      maxCount = value
      keyTracker = key
  return keyTracker
majorityElement(nums = [5,5,6,7,8,8,9,3,5,5,7,7,8,8,8])
