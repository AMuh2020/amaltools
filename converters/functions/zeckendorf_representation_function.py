def zeckendorf_representation(positive_integer,seperator):
    #idea from bio q1
    #original code for question one bio 2023 round 1 (small modifications)
    def find(num):
        fibonacci = [0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309]
        for i in range(len(fibonacci)):
            if fibonacci[i] > num:
                
                return fibonacci[i-1]
            elif fibonacci[i] == num:
                return num

    try:
        value = int(positive_integer)
    except :
        return "please enter a positive integer"
    if value < 0:
        return f"{positive_integer} is less than 0"
    zeckendorf_representation = []

    while value > 0:
        takeaway = find(value)
        value = value - takeaway
        zeckendorf_representation.append(takeaway)
    
    return f"{seperator}".join(str(i) for i in zeckendorf_representation)