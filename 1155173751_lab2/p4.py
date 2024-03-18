import math


def check_invalid(triangle):
  a, b, c = triangle
  if a > 0 and b > 0 and c > 0 and a+b > c and b+c > a and a+c > b:
    return False
  else:
    return True

def tangent_radius(triangle):
  a, b, c = triangle
  #Heron's formula
  s = (a + b + c) / 2
  #T is the area of the triangle
  T = math.sqrt((s * (s - a) * (s - b) * (s - c)))
  r = 2 * T / (a + b + c)
  return r

def outer_radius(triangle):
  a, b, c = triangle
  s = (a + b + c) / 2
  T = math.sqrt((s * (s - a) * (s - b) * (s - c)))
  R = a * b * c / (4 * T)
  return R