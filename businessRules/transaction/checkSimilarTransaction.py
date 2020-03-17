import globalVariables.variables as accountVariable
from utills.generalUtills import epochTime

def checkDoubledTransaction(reqData):

    transTime = epochTime(reqData['transaction']['time'])
    checkIndexList = [x for x in accountVariable.transList if abs(x - transTime) <= 120 ]
    for element in checkIndexList:
        for index in accountVariable.transactions_dict[element]:
            if accountVariable.transactions_dict[element][index]['merchant'] == data['transaction']['merchant'] and accountVariable.transactions_dict[element][index]['amount'] == data['transaction']['amount']:
                return ["doubled-transaction"]
    return []