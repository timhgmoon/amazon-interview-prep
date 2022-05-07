# using additional data structure, run time O(n)
def check_duplicates(word):
  letters = {}
  
  for letter in word:
    if letter in letters:
      letters[letter] = 1
    else:
      letters[letter] = 0
  
  if 1 in letters.values():
    return True
  return False

# without using additional data structures, run time O(n^2)
def check_dupes(word):
  for i in range(len(word)):
    for j in range(i+1, len(word)):
      if word[i] == word[j]:
        return True
  return False

print(check_duplicates("hello"))
print(check_dupes('helo'))