from functools import reduce

def gcd(num1, num2):
  while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp
  return num1

def lcm(num1, num2):
  return num1 * num2 // gcd(num1, num2)

print(reduce(lcm, range(1, 20)))