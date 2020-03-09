import dateutil.parser as dp
def epochTime(isoTime):
    return dp.parse(isoTime).timestamp()

def checkDifference(a,b):
    difference = a-b
    if difference > 120:
        return True
    else:
        return False
