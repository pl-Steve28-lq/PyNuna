# PyNuna
Nuna Language Interpreter Implemented with Python <br>
Original Details : [nunalang/nuna](https://github.com/nunalang/nuna)

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

## Warning
누나 v0.3 에서 논의되는 "끝의 두 요소를 Pop 하고 둘의 차를 Push 하기" 명령이 '♥' 으로 구현되어 있습니다. <br>
이는 나중에 수정 될 수 있습니다.