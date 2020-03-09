from utills.generalUtills import epochTime
import globalVariables.variables as var
from response.transactionAuthorizationResponse import responseObj

def accountCreate(data):    
    if var.account_created :
        return responseObj(["account-already-initialized"])
    var.account_balance = data['account']['available-limit']
    var.active_card = data['account']['active-card']
    var.account_created = True
    return responseObj([])