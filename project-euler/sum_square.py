def sum_of_square(num):
  sum = 0
  for i in range(1, num+1):
    sum += (i ** 2)
  return sum

def square_of_sum(num):
  sum = 0
  for i in range(1, num+1):
    sum += i
  return sum ** 2
print(square_of_sum(100) - sum_of_square(100))
