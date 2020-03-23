import globalVariables.variables as accountVariable

def checkAccountBalance(reqData):
    if reqData['transaction']['amount'] > accountVariable.account_balance:
        return ['insufficient-limit']
    return []