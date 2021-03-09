# PyNuna
Nuna Language Interpreter Implemented with Python <br>
Original Details : [nunalang/nuna](https://github.com/nunalang/nuna)

## Warning
누나 v0.3 을 구현하는 도중 실행에 오류가 있는데 왜 났는지 모르겠습니다.
지금 레포에 있는 코드는 v0.2 구현체 입니다.

## Download
```pip install nuna``` <br>
[View at Pypi](https://pypi.org/project/Nuna/)

## Example
```Python
from nuna import Nuna, generate

code = '''눈나..나..주...나..........거나..........거....나..........거나..........거나....누........나.........♥
누나..나..나..거나..나.....나.....거...나..나.....거나..나.....주..눈나..........나..........♥!'''
# Code that prints "누나" in Nunalang
n = Nuna()
print(n.execute(code))

print()
n.clear() # Clear stack

code = generate("Hello, World!") # Generate code that prints "Hello, World!" in Nunalang
print(code)
print(n.execute(code))

'''
Result

누나
[45572, 45208]

누나..나..나..나...나...주거!
눈나..나..나.......주.거..💕!
눈나..나...주.거..💕!
!눈나...주거💕!
누나..나...나...........주.거..♥!
눈나..나..나...주거♥!
누나.....나...........주거💕!
눈나..나..나..나...주거💕!
누나...주거💕!
눈나..나...주거♥!
누나..나...주..거....♥!
누나..나...나...........주.거..♥!

Hello, World!
[33]
'''
```
