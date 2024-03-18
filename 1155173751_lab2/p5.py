def count_digit(test_string):
  num = 0
  for x in test_string:
    if x.isdigit():
      num += 1
    else:
      continue
  return num

def check_isogram(test_string):
  #has duplicate letters => not an isogram => False
  check_string = set()
  for x in test_string:
    if x in check_string:
      return False
    else:
      check_string.add(x)
  return True

def join(original_string, inserted_list):
  new_string = original_string.join(inserted_list)
  return new_string

def search(test_string, sub):
  highest_index = -1
  index = -1
  while True:
      index = test_string.find(sub, index + 1)
      if index == -1:
          break
      highest_index = index
  return highest_index