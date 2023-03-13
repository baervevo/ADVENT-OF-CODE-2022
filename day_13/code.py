with open('day_13.txt', 'r') as f:
    lines = f.read().split('\n')

lines = [eval(line) for line in lines if line != '']

indicies = []

def compare(a,b):
    for i, x in enumerate(a):
        result = None
        
        try:
            y = b[i]
        except IndexError:
            return False

        if type(x) == type(y):
            if type(x) == int:
                if x < y:
                    return True
                elif x > y:
                    return False
            elif type(x) == list:
                result = compare(x, y)
        elif type(x) != type(y):
            if type(x) == int and type(y) == list:
                result = compare([x], y)
            elif type(x) == list and type(y) == int:
                result = compare(x, [y])
            
        if result == True:
            return True
        elif result == 'Equal' or result == None:
            continue
        else:
            return False

    if len(a) == len(b):
        return 'Equal'
    else:
        return True

def sort(list):
    for i in range(len(list)):
        for m in range(0,len(list)-i-1):
            if compare(list[m], list[m+1]) == False:
                temp = list[m]
                list[m] = list[m+1]
                list[m+1] = temp

sort(lines)

print((lines.index([[2]])+1)*(lines.index([[6]])+1))