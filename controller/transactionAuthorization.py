from constants.transactionRulesList import transactionRuleFlow
from response.transactionAuthorizationResponse import responseObj
import globalVariables.variables as var
def makeTrasact(data):
    print(data)
    for rule in transactionRuleFlow:
        a = rule(data)
        if len(a) > 0:
            return responseObj(a)
    
    var.transactions_dict[transTime] = {"amount":data['transaction']['amount'],"merchant":data['transaction']['merchant']}
    var.account_balance = var.account_balance - data['transaction']['amount']
    return responseObj([])

