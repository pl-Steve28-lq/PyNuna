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
