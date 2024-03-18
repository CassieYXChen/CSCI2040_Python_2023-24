def quicksort(a):
  if len(a) < 2:
    return a
  else:
    pivot = a[0]
    #print (pivot, '\n')
    smaller = [i for i in a[1:] if i < pivot]
    equal = [i for i in a if i == pivot]
    larger = [i for i in a[1:] if i > pivot]
    return quicksort(larger) + equal + quicksort(smaller)