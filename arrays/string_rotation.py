def is_rotated(word1, word2):
  if len(word1) != len(word2):
    return False
    
  extended_word1 = word1 + word1
  if word2 in extended_word1:
    return True
  return False

print(is_rotated("helloworld", "lloworldhe"))
