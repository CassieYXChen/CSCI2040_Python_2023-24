def check_sublist(list1, a, b, c):
  min = 0
  lista = []
  listb = []
  listc = []
  if a <= b and a <= c:
    min = a
  elif b <= a and b <= c:
    min = b
  else:
    min = c
  for x in list1:
    if x < min:
      lista.append(x)
    if x < a+b-c and x > a-b-c:
      listb.append(x)
    if x > a or x > b or x > c:
      listc.append(x)      
  
  return lista, listb, listc