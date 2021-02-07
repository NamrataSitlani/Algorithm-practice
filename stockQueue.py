import copy


def stockQueue(snapS):
    snapshotCopy = copy.copy(snapS)
    tempCounter = {}
    for i, stock in enumerate(snapS):
        if stock['sym'] in tempCounter.keys():
            del snapshotCopy[tempCounter[stock['sym']]]
            tempCounter[stock['sym']] = i
        else:
            tempCounter[stock['sym']] = i
    print(tempCounter)
    return snapshotCopy
  
snapshot = [{'sym': 'GME', 'cost': 280}, {'sym': 'PYPL', 'cost': 234},
 {'sym': 'AMZN', 'cost': 3206},
 {'sym': 'AMZN', 'cost': 3213},
 {'sym': 'GME', 'cost': 325}]
  
print(stockQueue(snapshot))
