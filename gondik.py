##github.com/coderman0
from pip._vendor.colorama import Fore
import time
import os

os.system('cls')

banner = """
           /´¯¯/)
          /¯.../
         /..../
     /´¯/'..'/´¯¯`·¸
 /'/.../..../....../¨¯|
('(....´...´... ¯~/'..')
 \..............'...../
  \....\.........._.·´
   \..............(
    \..............|
"""
print(Fore.BLUE+banner)

print('Welcome to Website Kolonya Enjector')

print(Fore.WHITE+'['+Fore.MAGENTA+'1'+Fore.WHITE+'] '+Fore.WHITE+'Websitesi')
print(Fore.WHITE+'['+Fore.MAGENTA+'2'+Fore.WHITE+'] '+Fore.WHITE+'Elimize')

kolanya31 = input('Kolonya Seçin  #: ')
if kolanya31 == '1':
    print('WebColonya')
    kolanya = input('Write Url #: ')
    while True:
        print(Fore.GREEN+banner)
if kolanya31 == '2':
    kolonya = input('Sağ El #: ')
    while True:
        print(Fore.RED+banner)
