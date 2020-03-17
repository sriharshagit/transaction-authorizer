import globalVariables.variables as accountVariable
def checkAccountStatus(reqData):
    if accountVariable.account_created:
        return ["account-already-initialized"]
    return []