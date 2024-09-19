def larger_sum(lst1, lst2):
  lst1_sum = 0
  lst2_sum = 0
  for number in lst1:
    lst1_sum += number
  for number in lst2:
    lst2_sum += number
  if lst1_sum >= lst2_sum:
    return lst1
  else:
    return lst2
  
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2
  
def always_false(num):
  if num < 0 and num > 0:
    return True
  return False

def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

print(larger_sum([5, 1, 7, 3], [8, 2, 9, 1]))
#print(more_frequent_item([2, 3, 2, 3, 3, 2, 3, 2, 2, 2, 3, 2, 3, 3], 2, 3))
#print(always_false(12))
#print(max_num(8.010, 8.001, 8.100))
#print(divisible_by_ten([30, 35, 40, 5, 10, 50, 65, 100,000]))