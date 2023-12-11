from datetime import datetime, timedelta
    
def getBillable(actualIn, actualOut, scheduleIn, scheduleOut, setBillable, actualBreakDuration, scheduleBreakDuration, isBreakBillable): #str, str, str, str, seconds, seconds, seconds, boolean
    actualIn_time = datetime.strptime(actualIn, '%H:%M:%S')
    actualOut_time = datetime.strptime(actualOut, '%H:%M:%S')
    scheduleIn_time = datetime.strptime(scheduleIn, '%H:%M:%S')
    scheduleOut_time = datetime.strptime(scheduleOut, '%H:%M:%S')
    
    workHours = (min(actualOut_time, scheduleOut_time) - max(actualIn_time, scheduleIn_time)).total_seconds()
    
    if isBreakBillable:
        workHours = workHours - min(0, (actualBreakDuration - scheduleBreakDuration))
    else:
        workHours = workHours - actualBreakDuration
    
    return int(min(workHours, setBillable))

def getDuration(start, end): #str, str
    start_time = datetime.strptime(start, '%H:%M:%S')
    end_time = datetime.strptime(end, '%H:%M:%S')
    return (end_time - start_time).total_seconds()
    
def getLate(timeIn, actualIn): #str, str
    timeIn_time = datetime.strptime(timeIn, '%H:%M:%S')
    actualIn_time = datetime.strptime(actualIn, '%H:%M:%S')
    
    if actualIn_time > timeIn_time:
        return int((actualIn_time - timeIn_time).total_seconds())
    else:
        return 0
    
def getUndertime(timeOut, actualOut):  #str, str
    actualOut_time = datetime.strptime(actualOut, '%H:%M:%S')
    timeOut_time = datetime.strptime(timeOut, '%H:%M:%S')
    
    if actualOut_time < timeOut_time:
        return int((timeOut_time - actualOut_time).total_seconds())
    else:
        return 0
    
def getDeficit(late, undertime, actualBreakDur, schedBreakDur): #seconds, seconds, seconds, seconds
    #if actualBreakDur > schedBreakDur, deficit
    deficit = late + undertime + max(0, (schedBreakDur - actualBreakDur))
        
    return deficit
    
def getExcess(actualIn, actualOut, schedIn, schedOut, schedBillable, actualBreakDur, schedBreakDur, isBreakBillable): #str, str, str, str, seconds, seconds, seconds, boolean
    actualIn_time = datetime.strptime(actualIn, '%H:%M:%S')
    actualOut_time = datetime.strptime(actualOut, '%H:%M:%S')
    schedIn_time = datetime.strptime(schedIn, '%H:%M:%S')
    schedOut_time = datetime.strptime(schedOut, '%H:%M:%S')
    
    excess = max(0, (schedIn_time - actualIn_time).total_seconds()) + max(0, (actualOut_time - schedOut_time).total_seconds())
    
    if (not isBreakBillable) and (schedBreakDur > actualBreakDur):
        totalWorkHours = (min(actualOut_time, schedOut_time) - max(actualIn_time, schedIn_time)).total_seconds()
        excess = excess + max(0, (totalWorkHours - schedBillable) - actualBreakDur)
    
    return excess

def getOvertime(timeIn, timeOut, actualIn, actualOut): #in progress
    timeInObj = datetime.strptime(timeIn, '%H:%M:%S')
    timeOutObj = datetime.strptime(timeOut, '%H:%M:%S')
    #calculations
    return 0
    
#Methods below for calculations concerning schedules with unbillable breaks
#WIP
def getBillable_Break():
    return 0
    
def getDeficit_Break():
    return 0
    
def getExcess_Break():
    return 0