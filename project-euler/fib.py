#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib(num):
  ans_list = [1, 2]
  index = 1
  even_sum = 0
  while ans_list[index] <= num:
    index += 1
    first = ans_list[index-2]
    second = ans_list[index-1]
    ans_list.append(first + second)

  for i in range(len(ans_list)):
    if ans_list[i] % 2 == 0:
      even_sum += ans_list[i]
  
  return even_sum
print(fib(4000000))