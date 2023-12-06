from datetime import datetime, timedelta
    
def getBillable(actualIn, actualOut, setBillable): #datetime, datetime, seconds
    workHours = (actualOut - actualIn).total_seconds()
    
    return int(min(workHours, setBillable))
    
def getLate(timeIn, actualIn): #datetime, datetime
    if actualIn > timeIn:
        return int((actualIn - timeIn).total_seconds())
    else:
        return 0
    
def getUndertime(timeOut, actualOut):  #datetime, datetime
    if actualOut < timeOut:
        return int((timeOut - actualOut).total_seconds())
    else:
        return 0
    
def getDeficit(late, undertime): #seconds, seconds
    return int(late + undertime)
    
def getExcess(actualIn, actualOut, setBillable): #datetime, datetime, seconds
    if (actualOut - actualIn).total_seconds() > setBillable:
        return int((actualOut - actualIn).total_seconds())
    else:
        return 0
    
def getOvertime(timeIn, timeOut, actualIn, actualOut): #in progress
    timeInObj = datetime.strptime(timeIn, '%H:%M:%S')
    timeOutObj = datetime.strptime(timeOut, '%H:%M:%S')
    #calculations
    
#Methods below for calculations concerning schedules with unbillable breaks
#WIP
def getBillable_UB():
    return 0
    
def getDeficit_UB():
    return 0
    
def getExcess_UB():
    return 0