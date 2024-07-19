#arithmetic
#an=a1+(n-1)d

def arthimetic_sequence(sequence):
    sequence = [int(val) for val in sequence]
    #nums = [-35,-51,-67,-83]
    for i in range(len(sequence)-1):
        d = sequence[i+1] - sequence[i]
        if i == 0:
            prev_d = d
        
        if d != prev_d:
            print("not arithmetic sequence")
            break
        prev_d = d
        print(i)


    formula2 = f"An={first_term}+{d}(n-1)"
    print(f"{d}")
    constant = sequence[0] + d * -1
    if constant<0:
        formula = f"{d}n{constant}"
    else:
        formula = f"{d}n+{constant}"


    print(formula)
    print(f"equation is {formula2}")
