from constants.accountRulesList import accountCreationRuleFlow
from response.transactionAuthorizationResponse import responseObj
import globalVariables.variables as accountVariable

def accountCreate(data):
    for rule in accountCreationRuleFlow:
        a = rule(data)
        if len(a) > 0:
            return responseObj(a)
    
    accountVariable.account_balance = data['account']['available-limit']
    accountVariable.active_card = data['account']['active-card']
    accountVariable.account_created = True
    return responseObj([])