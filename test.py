def summation(num_list):
  if len(num_list) == 0:
    return 0
  if num_list[-1] % 2 == 0:
   return num_list[-1] + summation(num_list[:-1])
  else:
    return summation(num_list[:-1])

a = summation([1,2,3,4,6, 10,11,121,1009])
print(a)