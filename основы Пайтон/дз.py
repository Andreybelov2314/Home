def  is_balanced(string):
    dct={'(':')', '[':']', '{':'}'}
    if len(string) < 1:
        return True
    else:
        if len(string) < 2:
            return False
        if string[0] in dct.keys():
            if dct.get(string[0]) == string[1]:
                return is_balanced(string[2:])
            else:
                return False
        else:
            return is_balanced(string[1:])