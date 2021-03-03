from sys import stdin, stdout

def stdout(*text, _sep=' ', _end='\n'):
  stdout._encoding = 'utf-8'
  print(*text, sep=_sep, end=_end, flush=True)

def stdin():
  res = stdin.readline()
  return res[:-1] if res[-1] == '\n' else res