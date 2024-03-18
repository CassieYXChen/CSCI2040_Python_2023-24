def unique(list):
  result = []
  compare = set()
  for item in list:
    if item not in compare:
      result.append(item)
      compare.add(item)
  return result