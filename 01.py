with open('input', 'r') as f:
    content = f.read()
    l = content.splitlines()
    #part 1
    cl = 50
    s1 = 0
    for e in l:
        if(e[0] == 'R'):
            cl += int(e[1:]) 
                
        elif(e[0] == 'L'):
            cl -= int(e[1:])
    
        if cl %100 == 0:
            s1 += 1
    print(s1)
    
    #part 2
    cl = 50
    s2 = 0
    for e in l:
        if(e[0] == 'R'):
            for i in range(int(e[1:])):
                cl = (cl + 1)%100
                if cl == 0:
                    s2 += 1
        elif(e[0] == 'L'):
            for i in range(int(e[1:])):
                cl = (cl - 1)%100
                if cl == 0:
                    s2 += 1
    print(s2)