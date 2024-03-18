def Fib(n):
  if n == 0:
    Fib_number = 0
  elif n == 1:
    Fib_number = 1
  else:
    Fib_number = Fib(n-1) + Fib(n-2)
    
  return Fib_number