import json, csv
from fixedSchedCalculations import *

jsonFile = open('config.json')
data = json.load(jsonFile)
jsonFile.close()

#Variables from config file--
dataFileName = data['dataFileName']
employeeID = data['employeeID']
attDate = data['attDate']

schedType = data['schedType']
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
    
    #handle file, create writer
    with open('testData/' + dataFileName, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        
        #check if breakStart is none. If no, run wBreak, if yes, run noBreak
        if breakStartVars[0] == "none":
            noBreak(csvwriter)
        else:
            wBreak(csvwriter)
   
#generate test date for no break scenarios    
def noBreak(csvwriter):
    global count
    for i in timeInVars:
        for j in timeOutVars:
            #get calculations
            late = getLate(schedIn, i)
            undertime = getUndertime(schedOut, j)
            deficit = getDeficit(late, undertime, 0, 0)
            excess = getExcess(i, j, schedIn, schedOut)
            
            if withOvertime: 
                overtime= getOvertime() #WIP
            else:
                overtime= 0
            
            #billable hours calculation differ with schedule type, although flex is still unavailable        
            match schedType:
                case 'fixed':
                    billable = getBillableFixed(i, j, schedIn, schedOut, schedBill, 0, breakDur, isBreakBillable)
                    
                case 'full flexible':
                    billable = getBillableFullFlex() #WIP
                    
                case 'set flexible':
                    billable = getBillableSetFlex() #WIP
                    
                case _ :
                    billable = 0
            
            #write to csv file     
            row = [count, employeeID, attDate, i, j, breakId, '-', '-', billable, late, undertime, deficit, excess, overtime]
            csvwriter.writerow(row)
            count += 1
       
#generate test date for no break scenarios               
def wBreak(csvwriter):
    global count
    for i in timeInVars:
        for j in timeOutVars:
            for k in breakStartVars:
                for l in breakEndVars:
                    #get calculations
                    late = getLate(schedIn, i)
                    undertime = getUndertime(schedOut, j)
                    actualBreakDuration = getDuration(k, l)
                    deficit = getDeficit(late, undertime, actualBreakDuration, breakDur)
                    excess = getExcess(i, j, schedIn, schedOut)
                    
                    if withOvertime: 
                        overtime= getOvertime() #WIP
                    else:
                        overtime= 0
                    
                    #billable hours calculation differ with schedule type, although flex is still unavailable    
                    match schedType:
                        case 'fixed':
                            billable = getBillableFixed(i, j, schedIn, schedOut, schedBill, actualBreakDuration, breakDur, isBreakBillable)
                            
                        case 'full flexible':
                            billable = getBillableFullFlex() #WIP
                            
                        case 'set flexible':
                            billable = getBillableSetFlex() #WIP
                            
                        case _ :
                            billable = 0
                    
                    #write to csv file    
                    row = [count, employeeID, attDate, i, j, breakId, k, l, billable, late, undertime, deficit, excess, overtime]
                    csvwriter.writerow(row)
                    count += 1
              
if __name__ == '__main__':
    main()