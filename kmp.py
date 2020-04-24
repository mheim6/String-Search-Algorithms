####################################
#
# Monica Heim
# Driver Code
# Automata Algorithms and Complexity
# Assignment 3
####################################


def KMP(incl, string): 
    M = len(incl) 
    N = len(string)
    bounce = []
    oport = [0]*M
    j = 0   
    enumerate(incl, M, oport) 
    i = 0
    while i < N: 
        if incl[j] == string[i]: 
            i = i + 1
            j = j + 1
        if j == M:
            bounce.append(i-j)
            j = oport[j-1] 
        elif i < N and incl[j] != string[i]: 
            if j != 0: 
                j = oport[j-1] 
            else: 
                i = i + 1
    if not bounce:
        bounce.append(-1)
        print("SubString is not found: ")
        print(bounce)
    else:
        print("SubString is found at :")
        print(bounce)
  
def enumerate(incl, M, oport): 
    checks = 0 
    oport[0]  = 0 
    i = 1
    while i < M: 
        if incl[i] == incl[checks]: 
            checks = checks + 1
            oport[i] = checks
            i = i + 1
        else: 
            if checks != 0: 
                checks = oport[checks-1] 
            else: 
                oport[i] = 0
                i = i + 1
 