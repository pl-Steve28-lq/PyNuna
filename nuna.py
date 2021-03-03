from utils import *

class Nuna:
  def __init__(self, error=True):
    self.error = error
    self.stack = []

  def tokenize(self, code):
    com = '눈누나주거!💕♥'
    res = []
    prev = ''
    cnt = idx = column = lineno = 0
    for i in code+'!':
      if i in com:
        if prev: res.append([prev, cnt+(not cnt)])
        prev = i; cnt = 0
      elif i == '.': cnt += 1
      elif i == '\n': lineno += 1; column = 0
      elif self.error:
        raise Exception(f'Invalid character "{i}" found. '
        '(Line {lineno+1} Column {column+1}, Char {idx})')
      idx += 1; column += 1
    return res
  
  def execute(self, code):
    self.stack = []
    result = ''
    tok = self.tokenize(code)
    for i in tok:
      com, cnt = i
      if com in '눈누': self.stack.append(cnt)
      if com == '나': self.push(self.getLast()*cnt)
      if com == '주': self.push(self.getLast()-cnt)
      if com == '거': self.push(self.getLast()+cnt)
      # Warning : Unofficial Command (♥)
      if com in '💕♥': 
        p = self.stack.pop()
        q = self.stack.pop()
        self.stack.append(q+(2*(com == '💕')-1)*p)
      # Warning : Unofficial Command (♥)
      if com == '!':
        for i in self.stack:
          result += chr(i)
    stdout(result)
    return self.stack
  
  def getLast(self):
    if self.stack:
      return self.stack.pop()
    raise Exception('Operate with empty stack')
  
  def push(self, item):
    self.stack.append(item)

code = '''눈나..나..주...나..........거나..........거....나..........거나..........거나....누........나.........♥
누나..나..나..거나..나.....나.....거...나..나.....거나..나.....주..눈나..........나..........♥!'''
n = Nuna()
print(n.execute(code))