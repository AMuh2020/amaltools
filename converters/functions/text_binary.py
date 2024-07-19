from . import decimalToBinaryFunction
from . import binaryToDecimalFunction

def textToBin(inp):
    inp = str(inp)
    ascii = [ord(let) for let in inp]
    binary = [decimalToBinaryFunction.decToBin(num) for num in ascii]
    return " ".join(binary)

# import time
# start_time = time.time()
# print(textToBin("Wow it actually workst"))
# print("--- %s seconds ---" % (time.time() - start_time))

def binToText(inp):
    inp = inp.split()
    ascii = [binaryToDecimalFunction.binToDec(num) for num in inp]
    letters = [chr(num) for num in ascii]
    return "".join(letters)
    
