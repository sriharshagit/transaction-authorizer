import dateutil.parser as dp
def epochTime(isoTime):
    return dp.parse(isoTime).timestamp()
