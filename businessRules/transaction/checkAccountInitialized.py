import globalVariables.variables as accountVariable

def checkCardActiveStatus(reqData):
    if not accountVariable.active_card:
        return ['account-not-initialized']
    return []