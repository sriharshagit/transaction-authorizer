from constants.accountRulesList import accountCreationRuleFlow
from response.transactionAuthorizationResponse import responseObj
import globalVariables.variables as var

def accountCreate(data):
    for rule in accountCreationRuleFlow:
        a = rule(data)
        if len(a) > 0:
            return responseObj(a)
    
    var.account_balance = data['account']['available-limit']
    var.active_card = data['account']['active-card']
    var.account_created = True
    return responseObj([])