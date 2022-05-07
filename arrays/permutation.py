def check_permutation(small_word, big_word):
  for i in range(len(big_word) - len(small_word) + 1):
    current_string = list(big_word[i:i+len(small_word)])
    for j in range(len(small_word)):
      if small_word[j] in current_string:
        current_string.remove(small_word[j])
      if not current_string:
        return True

  return False

print(check_permutation("hello", "ooohhell"))
