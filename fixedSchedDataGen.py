import json, csv
from fixedSchedCalculations import *

jsonFile = open('config.json')
data = json.load(jsonFile)
jsonFile.close()

#Variables from config file--
dataFileName = data['dataFileName']
email = data['email']
password = data['password']
employeeID = data['employeeID']
attDate = data['attDate']

schedIn = data['schedIn']
schedOut = data['schedOut']
timeInVars = data['timeInVars']
timeOutVars = data['timeOutVars']
schedBill = data['schedBill']

breakId = data['breakId']
breakDur = data['breakDur']
breakStartVars = data['breakStartVars']
breakEndVars = data['breakEndVars']
isBreakBillable = data['isBreakBillable']

withOvertime = data['withOvertime']
otRange = data['otRange']

#global variables
count = 1

def main():
    fields = ['testID', 'employeeId', 'attDate', 'timeIn', 'timeOut', 'breakId', 'breakStart', 'breakEnd', 'billable', 'late', 'undertime', 'deficit', 'excess', 'overtime']
    
    with open(dataFileName, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        
        #check if breakStart is none. If no, run wBreak, if yes, run noBreak
        if breakStartVars[0] == "none":
            noBreak(csvwriter)
        else:
            wBreak(csvwriter)
    
def noBreak(csvwriter):
    global count
    for i in timeInVars:
        for j in timeOutVars:
            if withOvertime: 
                otVal = getOvertime()
            else:
                otVal = 0
                
            lateVal = getLate(schedIn, i)
            utVal = getUndertime(schedOut, j)
            row = [count, employeeID, attDate, i, j, breakId, '-', '-', getBillable(i, j, schedIn, schedOut, schedBill, 0, breakDur, isBreakBillable), lateVal, utVal, getDeficit(lateVal, utVal, 0, 0), getExcess(i, j, schedIn, schedOut, schedBill, 0, breakDur, isBreakBillable), otVal]
            csvwriter.writerow(row)
            count += 1
            
def wBreak(csvwriter):
    global count
    for i in timeInVars:
        for j in timeOutVars:
            for k in breakStartVars:
                for l in breakEndVars:
                    if withOvertime: 
                        otVal = getOvertime()
                    else:
                        otVal = 0
                        
                    lateVal = getLate(schedIn, i)
                    utVal = getUndertime(schedOut, j)
                    actualBreakDuration = getDuration(k, l)
                    row = [count, employeeID, attDate, i, j, breakId, k, l, getBillable(i, j, schedIn, schedOut, schedBill, actualBreakDuration, breakDur, isBreakBillable), lateVal, utVal, getDeficit(lateVal, utVal, actualBreakDuration, breakDur), getExcess(i, j, schedIn, schedOut, schedBill, actualBreakDuration, breakDur, isBreakBillable), otVal]
                    csvwriter.writerow(row)
                    count += 1
              
if __name__ == '__main__':
    main()