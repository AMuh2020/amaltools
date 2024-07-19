def binToDec(binary):
    try:
        value = int(binary, 2)
    except ValueError:
        return 'Please make sure your number contains 0s and 1s only.'
    binary = str(binary)
    decimal = 0
    for count, num in enumerate(reversed(binary)):
        if int(num) == 1:
            decimal += 2**count

    return decimal