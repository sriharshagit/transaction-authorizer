import globalVariables.variables as accountVariable
from constants.transactionRulesList import transactionRuleFlow
from response.transactionAuthorizationResponse import responseObj
from utills.generalUtills import epochTime

def makeTrasact(data):
    print(data)
    for rule in transactionRuleFlow:
        a = rule(data)
        if len(a) > 0:
            return responseObj(a)

    transTime = epochTime(data['transaction']['time'])
    accountVariable.transactions_dict[transTime].append({"amount":data['transaction']['amount'],"merchant":data['transaction']['merchant']})
    accountVariable.account_balance = accountVariable.account_balance - data['transaction']['amount']
    accountVariable.transList.append(transTime)
    return responseObj([])