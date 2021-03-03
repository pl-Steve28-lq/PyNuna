from nuna import Nuna, generate

code = '''눈나..나..주...나..........거나..........거....나..........거나..........거나....누........나.........♥
누나..나..나..거나..나.....나.....거...나..나.....거나..나.....주..눈나..........나..........♥!'''
# Code that prints "누나" in Nunalang
n = Nuna()
print(n.execute(code))

n.clear() # Clear stack

code = generate("Hello, World!") # Generate code that prints "Hello, World!" in Nunalang
print(code)
print(n.execute(code))