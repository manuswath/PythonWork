import platform
#use a method in the platform module named system that shows the OS
x = platform.system()
print(x)
#next show a list of methods that can be used in the platform module
x = dir(platform)
print(x)