import globalVariables.variables as var
from utills.generalUtills import checkDifference
from utills.generalUtills import epochTime

alreadyExist = 0

def checkTimeWindow(reqData):

    transTime = epochTime(reqData['transaction']['time'])
    isTransactionPossible = isPossible(transTime)
    if isTransactionPossible:
        if alreadyExist:
            var.transList.append(transTime)
        return []
    else:
        if not alreadyExist:
            var.transList.remove(transTime)
        return ["high-frequency-small-interval"]
        
def isPossible(transTime):
    try:
        var.transList.index(transTime)
        alreadyExist = 1
    except:
        var.transList.append(transTime)
        var.transList.sort()
        alreadyExist = 0
    print(var.transList)
    if len(var.transList) <= 3 :
        return True
    index = var.transList.index(transTime)
    if index == 0: #to check if first transaction gets delayed
        if checkDifference(var.transList[3],var.transList[0]):
            return True
        else:
            return False # if first element gets delayed and not possible to fit in time window

    if index == len(var.transList) - 1 : # last element
        if checkDifference(transTime,var.transList[index - 3]):
            return True
        else:
            return False

    y = len(var.transList) - index - 1 # difference of index from last position
    if y > 1: # difference between 1st left and 1st and 2nd right
        if not checkDifference(var.transList[index + 2],var.transList[index - 1]):
            return False

    if index > 1: # difference between 1st right and 1st and 2nd left
        if not checkDifference(var.transList[index + 1],var.transList[index - 2]):
            return False

    if y > 2: # difference between element and 3rd right
        if not checkDifference(var.transList[index + 3],var.transList[index]):
            return False

    if index > 3:  # difference between element and 3rd left
        if not checkDifference(var.transList[index],var.transList[index - 3]):
            return False

    return True