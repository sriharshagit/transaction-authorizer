import globalVariables.variables as accountVariable
from utills.generalUtills import checkDifference
from utills.generalUtills import epochTime

def checkTimeWindow(reqData):

    transTime = epochTime(reqData['transaction']['time'])
    isTransactionPossible = isPossible(transTime)
    print(accountVariable.transList)
    accountVariable.transList.remove(transTime)
    if isTransactionPossible:
        return []
    else:
        return ["high-frequency-small-interval"]
        
def isPossible(transTime):
    accountVariable.transList.append(transTime)
    accountVariable.transList.sort()
    if len(accountVariable.transList) <= 3 :
        return True
    if len(accountVariable.transactions_dict[transTime]) > 3 :
        return False
    index = accountVariable.transList.index(transTime)
    if index == 0: #to check if first transaction gets delayed
        if checkDifference(accountVariable.transList[3],accountVariable.transList[0]):
            return True
        else:
            return False # if first element gets delayed and not possible to fit in time window

    if index == len(accountVariable.transList) - 1 : # last element
        if checkDifference(transTime,accountVariable.transList[index - 3]):
            return True
        else:
            return False

    y = len(accountVariable.transList) - index - 1 # difference of index from last position
    if y > 1 and not checkDifference(accountVariable.transList[index + 2],accountVariable.transList[index - 1]):
            return False

    if index > 1 and not checkDifference(accountVariable.transList[index + 1],accountVariable.transList[index - 2]):
            return False

    if y > 2 and not checkDifference(accountVariable.transList[index + 3],accountVariable.transList[index]):
            return False

    if index > 3 and not checkDifference(accountVariable.transList[index],accountVariable.transList[index - 3]):
            return False

    return True