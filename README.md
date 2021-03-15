# PyNuna
Nuna Language Interpreter Implemented with Python <br>
Original Details : [nunalang/nuna](https://github.com/nunalang/nuna)

## Download
```pip install nuna``` <br>
[View at Pypi](https://pypi.org/project/Nuna)

## Features
* Output 은 `sys.stdout._encoding = 'utf-8'` 를 시행한 뒤 print 함수를 이용합니다.
  <br> 정확히는 다음 함수를 이용합니다.
```Python
def stdout(*text, _sep=' ', _end='\n'):
  stdout._encoding = 'utf-8'
  print(*text, sep=_sep, end=_end, flush=True)
```
* 파이썬의 `float` 타입은 1e15 이상일 때 계산이 불안정하지만,
  <br>`int` 타입은 10\*\*100000 이상일 때도 정확한 계산이 가능하므로 메모리의 신뢰구간은 이론상 무한입니다.
* 파이썬 3의 `str` 타입은 기본적으로 유니코드이므로 특수문자 `💕`는 그냥 처리합니다.

## Example
```Python
from nuna.nuna import Nuna, generate

code = '''눈나..흐.....읏..나주..거....흐...읏...
누나..나...흐....읏..나주..거....💕
눈나.....나..흐...읏나.....주거...💕
누나..흐..읏나.......주..거......응읏..!

눈나..으흐읏
누나.....주..흐....읏나....응
누나.....나..주...읏나......응!'''
# Nuna code that prints '누나'

n = Nuna() # Nuna Executer
print(n.execute(code)) # Execute, and Print Last Memory Status

n.clear() # Clear Stack

code2 = generate('Hello, World!') # Generate code that prints 'Hello, World!'
n.execute(code2) # Execute
```
