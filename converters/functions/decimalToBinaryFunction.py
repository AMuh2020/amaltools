def index_of_a_one(num):
    i=0
    while True:
        if num / (2**i) < 1:
            return num - (2**(i-1)), i
        else:
            i += 1

def decToBin(number):
    number= int(number)
    if number != 0:
        l_index = []
        while number != 0:
            number, n_index = index_of_a_one(number)
            l_index.append(n_index)

        binary = ["0" for x in range(l_index[0])]
        for i in range(len(l_index)):
            binary[l_index[i]-1] = "1"

        binary.reverse()
        binary = ''.join(binary)
        return binary
    else:
        return 0