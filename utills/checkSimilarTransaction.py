import globalVariables.variables as var
def checkSimilar(data,transTime):
    checkIndexList = [x for x in var.transList if x != transTime and abs(x - transTime) <= 120 ]
    for element in checkIndexList:
        if var.transactions_dict[element]['merchant'] == data['transaction']['merchant'] and var.transactions_dict[element]['amount'] == data['transaction']['amount']:
            return False
    return True
    