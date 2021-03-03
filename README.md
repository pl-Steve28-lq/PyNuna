# PyNuna
Nuna Language Interpreter Implemented with Python <br>
Original Details : [nunalang/nuna](https://github.com/nunalang/nuna)

## Example
```Python
from nuna import Nuna
n = Nuna()
code = '''눈나..나..주...나..........거나..........거....나..........거나..........거나....누........나.........♥
누나..나..나..거나..나.....나.....거...나..나.....거나..나.....주..눈나..........나..........♥!'''
print(n.execute(code))

'''
Result

누나
[45572, 45208]
'''
```

## Warning
누나 v0.3 에서 논의되는 "끝의 두 요소를 Pop 하고 요소의 차를 Push 하기" 명령이 '♥' 으로 구현되어 있습니다. <br>
이는 나중에 수정 될 수 있습니다.
