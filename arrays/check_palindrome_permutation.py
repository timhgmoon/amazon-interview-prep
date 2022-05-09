def check_palindrome(word):
  word_dict = {}
  amount_of_single_letter = 0
  word = word.replace(" ", "")
  for i in range(len(word)):
    letter = word[i].lower()
    if letter in word_dict:
      word_dict[letter] += 1
    else:
      word_dict[letter] = 0

  for key in word_dict:
    if word_dict[key] == 0:
      amount_of_single_letter += 1

  if amount_of_single_letter > 1:
    return False
  return True

print(check_palindrome("Tact Coa"))
print(check_palindrome("hellololeh"))
