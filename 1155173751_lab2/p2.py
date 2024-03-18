def roman_to_decimal(str):
  n = 0
  rule = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
  length = len(str)
  previous_value, value = 0, 0
  # str => str[i]
  for i in range(length):
    #value stands for the Roman value of str[i]
    value = rule[str[i]]
    #detect IV, XL, IX, XC first:
    if i > 0:
      #If the previous value is smaller, then AB = B-A
      previous_value = rule[str[i-1]]
      if previous_value < value:
        #n has already added the previous value, so -*2
        n += value - 2 * previous_value
      else:
        n += value
    else:
      n += value

  return n

def decimal_to_roman(n):
  str = ''
  #less complicated than roman_to_decimal
  rule = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC'}
  list = [90, 50, 40, 10, 9, 5, 4, 1]
  for i in list:
    while n >= i:
      str += rule[i]
      n -= i
  
  return str