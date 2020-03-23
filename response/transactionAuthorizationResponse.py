import globalVariables.variables as accountVariable
def responseObj(violations):
    return {"account" : { "active-card" : accountVariable.active_card, " available-limit" : accountVariable.account_balance, "violations" :violations} }