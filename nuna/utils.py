from sys import stdin, stdout
from random import randint, choices

def stdout(*text, _sep=' ', _end='\n'):
  stdout._encoding = 'utf-8'
  print(*text, sep=_sep, end=_end, flush=True)

def stdin():
  stdin._encoding = 'utf-8'
  res = stdin.readline()
  return res[:-1] if res[-1] == '\n' else res

def sign(x):
  return 1-2*(x < 0)

def choice(a): return choices(a)[0]
def rand(a,b): return randint(a,b)

class Stream:
  def __init__(self, s):
    self.s = s
    self.L = len(s)
    self.i = 0
  
  def isEOF(self):
    return self.i >= self.L

  def get(self, s=''):
    if self.isEOF(): return
    it = self.s[self.i]
    if s:
      if it in s:
        self.i += 1
        return it
      return
    self.i += 1
    return it

# Factorization of number
def Factorize(n):
  i = 2
  res = {}
  while n%i == 0:
    res[i] = res.get(i, 0) + 1
    n //= i
  i += 1
  while n > 1:
    while n%i == 0:
      res[i] = res.get(i, 0) + 1
      n //= i
    i += 2
  return res