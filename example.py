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
