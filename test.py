def apart(nr, x, y):
    if nr >= x and nr <= y:
        return True
    else:
        return False

def pozitie(i, j):
    if apart(i, 0, 2):
        if apart(j, 0, 2):
            return "Nord-Vest"
        if apart(j, 3, 5):
            return "Nord"
        if apart(j, 6, 8):
            return "Nord-Est"

    if apart(i, 3, 5):
        if apart(j, 0, 2):
            return "Vest"
        if apart(j, 3, 5):
            return "Middle"
        if apart(j, 6, 8):
            return "Est"

    if apart(i, 6, 8):
        if apart(j, 0, 2):
            return "Sud-Vest"
        if apart(j, 3, 5):
            return "Sud"
        if apart(j, 6, 8):
            return "Sud-Est"


print(pozitie(1, 2))
