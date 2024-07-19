#28/11/2022
# Converting binary to hexadecimal




def binToHex(number):
    #make sure the input is binary
    try:
        value = int(number, 2)
    except ValueError:
        return 'Please make sure your number contains digits 0-1 only.'
    hexadecimal_symbols = ['0','1','2','3','4','5','6','7','8','9','A','B', 'C','D','E','F']
    hexadecimal = []
    for i in range(len(number), -1,-4):
        nibble = number[i-4:i]
        if i-4 < 0:
            remainder = len(number) % 4
            nibble = number[i-remainder:i]
        nibble_den = 0

        for count, num in enumerate(reversed(nibble)):
            if int(num) == 1:
                nibble_den += 2**count

        hexadecimal.insert(0,hexadecimal_symbols[nibble_den])

    # remove leading zeros
    try:
        while hexadecimal[0] == "0":
            hexadecimal.pop(0)
    except IndexError:
        hexadecimal = ["0"]

    hexadecimal = "".join(hexadecimal)
    return hexadecimal
#import time
#start_time = time.time()
#print(binToHex("01010101001"))
#print("--- %s seconds ---" % (time.time() - start_time))