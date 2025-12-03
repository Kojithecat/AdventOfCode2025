with open('input', 'r') as f:
    content = f.read()
    list = content.splitlines()
    
    #part 1
    s1 = 0
    for bank in list:
        bank_nums_list = [int(x) for x in bank]
        n1 = max(bank_nums_list[0:-1])
        idx_n1 = bank_nums_list.index(n1)
        n2 = max(bank_nums_list[idx_n1+1:])
        s1 += int(str(n1)+str(n2))
    print(s1)  
    
    #part 2
    s2 = 0
    for bank in list:
        bank_nums_list = [int(x) for x in bank]
        word = ''
        prev_idx = 0
        count = 0
        while count < 12:
            if count == 11: # Wierd case that breaks the smooth solution (count == 11 implies bank_nums_list[prev_idx:0]) which breaks the code.
                n = max(bank_nums_list[prev_idx:])
                word += str(n)
                break
            n = max(bank_nums_list[prev_idx:-(12-count-1)])
            idx_n = bank_nums_list[prev_idx:-(12-count-1)].index(n)
            count += 1
            prev_idx += idx_n +1
            word += str(n)
        s2 += int(word)
    print(s2)