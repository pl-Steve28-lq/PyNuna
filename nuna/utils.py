from sys import stdin, stdout
from random import choices

def stdout(*text, _sep=' ', _end='\n'):
  stdout._encoding = 'utf-8'
  print(*text, sep=_sep, end=_end, flush=True)

def stdin():
  res = stdin.readline()
  return res[:-1] if res[-1] == '\n' else res

def sign(x):
  return 1-2*(x < 0)

def choice(a): return choices(a)[0]

# Prime Check Function
def isPrime(n):
  if n == 1: return False
  for k in range(2, int(n**0.5)):
    if n%k == 0: return False
  return True

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