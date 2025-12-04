def check(c):
    return c == '@'

with open('input', 'r') as f:
    content = f.read()
    map = content.splitlines()
    
    #padding
    for i in range(len(map)):
        map[i] = '.'+map[i]+'.'
    map.append('.'*len(map[0]))
    map.insert(0, '.'*len(map[0]))
    
    #part 1
    s1 = 0
    for i in range(len(map)):
        for j in range(len(map[i])):  
            num = 0
            if(check(map[i][j])):
                num = check(map[i+1][j]) + check(map[i-1][j]) + check(map[i][j+1]) + check(map[i][j-1]) + check(map[i+1][j+1]) + check(map[i+1][j-1]) + check(map[i-1][j+1]) + check(map[i-1][j-1])
                if(num < 4):
                    s1 += 1    
    print(s1)
    #part 2
    s2 = 0
    copy_map = []
    while copy_map != map:
        copy_map = map[:]
        for i in range(len(map)):
            for j in range(len(map[i])):  
                num = 0
                if(check(map[i][j])):
                    num = check(map[i+1][j]) + check(map[i-1][j]) + check(map[i][j+1]) + check(map[i][j-1]) + check(map[i+1][j+1]) + check(map[i+1][j-1]) + check(map[i-1][j+1]) + check(map[i-1][j-1])
                    if(num < 4):
                        s2 += 1
                        map[i] = map[i][:j] + '.' + map[i][j+1:]
        
    for e in map:
        print(e)
    print(s2)
