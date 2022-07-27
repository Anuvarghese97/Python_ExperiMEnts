from lib2to3.pygram import Symbols
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
Symbols = "[]{}()*;/,.-_"

psw = lower + upper + numbers + Symbols
length = int(input("Enter total number of characters required for your password: "))
password = "".join(random.sample(psw,length))
print("Your password is: ",password)