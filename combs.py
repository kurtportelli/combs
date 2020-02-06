def combs(comb1, comb2):
    short, long = sorted((comb1, comb2), key=len)
    length_diff = len(long) - len(short)
    
    #if they fit perfectly in each other, return the length of the longest comb
    if length_diff >= 2:
        for i in range(1, length_diff):
            fit_perfect = True
            for l, s in zip(long[i:i+len(short)], short):
                if l == '*' and s == '*':
                    fit_perfect = False
                    break
            if fit_perfect == True:
                return len(long)
    
    #next shift the short comb to the left of the long one
    for i in range(1, len(short) - 1):
        fit_left = True
        for l, s in zip(long[:len(short)-i], short[i:]):
            if l == '*' and s == '*':
                fit_left = False
                break
        if fit_left == True:
            left = len(long) + i
            break
    if fit_left == False:
        left = len(long) + len(short)
    
    #now shift the short comb to the right of the long one
    for i in range(1, len(short) - 1):
        fit_right = True
        for l, s in zip(long[length_diff+i:], short[:-i]):
            if l == '*' and s == '*':
                fit_right = False
                break
        if fit_right == True:
            right = len(long) + i
            break
    if fit_right == False:
        right = len(long) + len(short)
    
    #return the minimum length
    return min(left, right)
