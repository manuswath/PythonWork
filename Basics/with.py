# file handling 
  
# 1) without using with statement 
file = open('with.txt', 'w') 
file.write('hello world !') 
file.close() 
  
# 2) without using with statement 
file = open('wither.txt', 'w') 
try: 
    file.write('hello world.....With her') 
finally: 
    file.close() 

# 3) using with statement 
with open('withest.txt', 'w') as file: 
    file.write('hello world ! .... Withest withest') 