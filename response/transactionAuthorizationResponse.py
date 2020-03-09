import globalVariables.variables as var
def responseObj(voitations):
    return {"account" : { "active-card" : var.active_card, " available-limit" : var.account_balance, "violations" :voitations} }