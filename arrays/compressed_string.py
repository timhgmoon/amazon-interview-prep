def compress_string(word):
  letters = {}
  ans = ""
  for i in range(len(word)):
    letter = word[i]
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1
      
  length_of_single = 0
  
  for key in letters:
    if letters[key] == 1:
      length_of_single += 1
    ans += key + str(letters[key])
    
  if length_of_single == len(word):
    return word
    
  return ans

print(compress_string("abcdf"))
print(compress_string("aabbcccdff"))
