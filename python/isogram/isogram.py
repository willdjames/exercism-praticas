def is_isogram(string):
    len_string = len(string)
    
    if len_string == 0:
        return True

    for i in range(0, len_string):
        for j in range(i+1, len_string):        
            if string[i].lower() == string[j].lower() and string[i] != '-' and not string[i].isspace():
                return False
    
    return True