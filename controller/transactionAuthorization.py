from utills.generalUtills import epochTime
from utills.checkTimeWindow import isPossible
from utills.checkSimilarTransaction import checkSimilar
from response.transactionAuthorizationResponse import responseObj
import globalVariables.variables as var
def makeTrasact(data):
    print(data)
    if not var.active_card:
        return  responseObj(['account-not-initialized'])
    if data['transaction']['amount'] > var.account_balance:
        return responseObj(['insufficient-limit'])
        
    transTime = epochTime(data['transaction']['time'])
    
    for key in var.transactions_dict.keys():
        if key == transTime:
            return responseObj(['transaction-already-done-in-ths-timestamp'])
    
    isTransactionPossible = isPossible(transTime)
    
    if isTransactionPossible:
        isNotSimilar = checkSimilar(data,transTime)
        if isNotSimilar:
            
            var.transactions_dict[transTime] = {"amount":data['transaction']['amount'],"merchant":data['transaction']['merchant']}
            var.account_balance = var.account_balance - data['transaction']['amount']
            return responseObj([])
        else:
            return responseObj(["doubled-transaction"])
    else:
        return responseObj(["high-frequency-samll-interval"])