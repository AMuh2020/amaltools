
#Number to words
def numberToText(number,with_dash):

    base = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    #special cases 11 12
    ten_base = {2:"twenty",3:"thirty",4:"forty",4:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
    teens_base = {1:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    big_base = {1:"thousand",2:"million",3:"billion",4:"trillion",5:"quadrillion",6:"quintrillion",7:"septillion",}
    str_number = str(number)
    str_number = str_number[::-1]
    triplets = [str_number[i:i+3] for i in range(0,len(str_number), 3)]
    # print(triplets)

    
    ans = []
    for i in range(len(triplets)):
        hold=[]
        for j in range(len(triplets[i])):
            num = triplets[i][j]
            # print(num)
            if num != "0":
                if j == 0:
                    transfer = base[int(num)]
                elif j == 1:
                        if i == 0 and num == "1":
                            comb = f"{num}{triplets[i][j-1]}"
                            # print(comb)
                            transfer = teens_base[int(comb)]
                            hold.pop(-1)
                        else:
                            transfer = ten_base[int(num)]
                elif j == 2:
                    transfer = f"{base[int(num)]} hundred"
                
                if j==1 and len(hold) == 1 and with_dash == True:
                    # print("LEN HOLD 2 here")
                    transfer = f"{transfer}-"
                elif (j==2 or j==0) and with_dash == True:
                    transfer = f"{transfer} "
                
                hold.append(transfer)
                # print(transfer)
                # print(hold)
            
        hold.reverse()
        if i == 0:
            pass
        else:
            hold.append(big_base[i])
        
        if with_dash == True:
            ans.append("".join(hold))
        else:
            ans.append(" ".join(hold))

    ans.reverse()
    # print(ans)
    # print(" ".join(ans))
    print(ans)
    return " ".join(ans)