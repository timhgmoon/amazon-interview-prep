def check_one_away(first_word, second_word):
  number_edits = 0
  main_word = ""
  len_first = len(first_word)
  len_second = len(second_word)

  if abs(len_first - len_second) > 1:
    return False
  if len_first < len_second:
    main_word += first_word
  elif len_first > len_second:
    main_word += second_word
  else:
    main_word = second_word
  
  for i in range(len(main_word)):
    if first_word[i] != second_word[i]:
      number_edits += 1
  
  if number_edits <= 1:
    return True
    
  return False
    