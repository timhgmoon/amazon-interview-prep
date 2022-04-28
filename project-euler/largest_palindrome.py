#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def isPalindrome(number):
  if str(number) == str(number)[::-1]:
    return True
  return False

def largest_palindrome():
  max = -1
  for i in range(999, 100, -1):
    for j in range(999, i, -1):
      product = i * j
      if max < product and isPalindrome(product):
        max = product

  if max != -1:
    return max

print(largest_palindrome())