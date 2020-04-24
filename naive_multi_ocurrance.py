####################################
#
# Monica Heim
# Driver Code
# Automata Algorithms and Complexity
# Assignment 3
####################################

def finder(initial,stack):
    len1 = len(initial)
    len2 = len(stack)
    
    start = 0
    position = []
    while start <= (len2):
        substr = stack[start:(start + len1)]
        if(substr == initial):
            position.append(start)
            start = start + len1
        else:
            start = start + 1
    if not position:
        print("substring not found:")
        position.append(-1)
        return position
    else:
        print("substring found at :")
        return position

