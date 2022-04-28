#The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def largest_prime(num):
  prime_factors = []
  i = 2
  while num >= 2:
    while num % i == 0:
      prime_factors.append(i)
      num /= i
    i += 1
  return prime_factors[len(prime_factors)-1]


print(largest_prime(600851475143))