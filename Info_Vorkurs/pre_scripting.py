



def checker(inputString):
    chronology = []
    opening = ["{","[","("]
    closing = ["}","]",")"]
    for i in inputString:
        if i in closing or i in opening:
            if i in opening:
                chronology.append(i)


            if i in closing and chronology:

                if opening[closing.index(i)] == chronology[-1]:
                    del chronology[-1]
                else:
                    return False

    if chronology:
        return False
    return True


print(checker(input("was willst du testen ?")))



