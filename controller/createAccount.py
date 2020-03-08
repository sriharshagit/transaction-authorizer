from utills.generalUtills import epochTime
import globalVariables.variables as var

def accountCreate(data):    
    if(var.account_created):
        return "account already created"
    var.account_balance = data['account']['available-limit']
    var.active_card = data['account']['active-card']
    var.account_created = True
    return "account created"