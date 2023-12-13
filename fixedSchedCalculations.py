from datetime import datetime, timedelta
    
def getBillableFixed(actualIn, actualOut, scheduleIn, scheduleOut, setBillable, actualBreakDuration, scheduleBreakDuration, isBreakBillable): #str (time), str (time), str (time), str (time), seconds, seconds, seconds, boolean
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

def getBillableFullFlex(actualIn, actualOut, scheduleIn, scheduleOut, setBillable, actualBreakDuration, scheduleBreakDuration, isBreakBillable): #str (time), str (time), str (time), str (time), seconds, seconds, seconds, boolean
    #do something
    return 0

def getBillableSetFlex(actualIn, actualOut, scheduleIn, scheduleOut, setBillable, actualBreakDuration, scheduleBreakDuration, isBreakBillable): #str (time), str (time), str (time), str (time), seconds, seconds, seconds, boolean
    #do something
    return 0

def getDuration(start, end): #str (time), str (time)
    start_time = datetime.strptime(start, '%H:%M:%S')
    end_time = datetime.strptime(end, '%H:%M:%S')
    return (end_time - start_time).total_seconds()
    
def getLate(timeIn, actualIn): #str (time), str (time)
    timeIn_time = datetime.strptime(timeIn, '%H:%M:%S')
    actualIn_time = datetime.strptime(actualIn, '%H:%M:%S')
    
    if actualIn_time > timeIn_time:
        return int((actualIn_time - timeIn_time).total_seconds())
    else:
        return 0
    
def getUndertime(timeOut, actualOut):  #str (time), str (time)
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
    
def getExcess(actualIn, actualOut, schedIn, schedOut): #str (time), str (time), str (time), str (time)
    actualIn_time = datetime.strptime(actualIn, '%H:%M:%S')
    actualOut_time = datetime.strptime(actualOut, '%H:%M:%S')
    schedIn_time = datetime.strptime(schedIn, '%H:%M:%S')
    schedOut_time = datetime.strptime(schedOut, '%H:%M:%S')
    
    excess = max(0, (schedIn_time - actualIn_time).total_seconds()) + max(0, (actualOut_time - schedOut_time).total_seconds())
    
    return excess

def getOvertime(timeIn, timeOut, actualIn, actualOut): #WIP
    timeInObj = datetime.strptime(timeIn, '%H:%M:%S')
    timeOutObj = datetime.strptime(timeOut, '%H:%M:%S')
    #calculations
    return 0