with open('input', 'r') as f:
    content = f.read()
    list = content.split(',')
    #part 1
    s1 = 0
    for e in list:
        l,r = e.split('-')
        for i in range(int(l),int(r)+1):
            word = str(i)
            if(word[0:len(word)//2] == word[len(word)//2:]):
                s1 += i
    print(s1)
        
    #part 2
    s2 = 0
    for e in list:
        l,r = e.split('-')
        for i in range(int(l),int(r)+1):
            word = str(i)
            cycle_len = 1
            while(cycle_len <= len(word)//2):
                if(len(word)%cycle_len != 0):
                    cycle_len += 1
                    continue   
                idx = 0
                wrong_id = True
                while idx+2*cycle_len <= len(word):
                    if(word[idx:(idx+cycle_len)] != word[(idx+cycle_len):(idx+2*cycle_len)]):
                        wrong_id = False
                        break
                    idx += cycle_len
                if(wrong_id):
                    print(word,cycle_len)
                    s2 += i
                    break
                cycle_len += 1
    print(s2)    