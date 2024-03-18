class Stack(object):
  def __init__(self):
    self.storage = []
    
  def push(self, newValue):
    self.storage.append(newValue)
    
  def top(self):
    return self.storage[-1]
    
  def pop(self):
    result = self.top()
    self.storage.pop()
    return result
    
  def isEmpty(self):
    return len(self.storage) == 0


class CalculatorEngine(object):
  def __init__(self):
    self.dataStack = Stack()
    
  def pushOperand(self, value):
    self.dataStack.push(value)
    
  def currentOperand(self):
    return self.dataStack.top()
    
  def performBinaryOp(self, fun):
    right = self.dataStack.pop()
    left = self.dataStack.top()
    self.dataStack.push(fun(left, right))
    
  def doAddition(self):
    self.performBinaryOp(lambda x, y: x + y)

  def doSubtraction(self):
    self.performBinaryOp(lambda x, y: x - y)
    
  def doMultiplication(self):
    self.performBinaryOp(lambda x, y: x * y)
    
  def doDivision(self):
    try:
      self.performBinaryOp(lambda x, y: x / y)
    except ZeroDivisionError:
      print("division by 0!")
      exit(1)
      
  def doTextOp(self, op):
    if (op == '+'):
      self.doAddition()
    elif (op == '-'):
      self.doSubtraction()
    elif (op == '*'):
      self.doMultiplication()
    elif (op == '/'):
      self.doDivision()


class RPNCalculator(CalculatorEngine):
  def __init__(self):
    super().__init__()

  def doPower(self):
    self.performBinaryOp(lambda x, y: x ** y)
      
  def doTextOp(self, op):
    if (op == '+'):
      self.doAddition()
    elif (op == '-'):
      self.doSubtraction()
    elif (op == '*'):
      self.doMultiplication()
    elif (op == '/'):
      self.doDivision()
    elif (op == '^'):
      self.doPower()

    
  def eval(self, line):
    inputs = line.split()
    for input in inputs:
        if input.isdigit():
            self.pushOperand(int(input))
        else:
            self.doTextOp(input)
    return self.currentOperand()

