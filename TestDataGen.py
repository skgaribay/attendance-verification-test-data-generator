import json, csv
from calculations import *

jsonFile = open('config.json')
data = json.load(jsonFile)
jsonFile.close()

#Variables from config file
email = data['email']
password = data['password']
employeeID = data['employeeID']
schedIn = data['schedIn']
schedOut = data['schedOut']
schedBill = data['schedBill']
attDate = data['attDate']
breakDur = data['breakDur']
timeInVars = data['timeInVars']
timeOutVars = data['timeOutVars']
breakStartVars = data['breakStartVars']
breakEndVars = data['breakEndVars']
isBreakBillable = data['isBreakBillable']

count = 1

# Parse config.json variables and create global variables from them

def main():
    fields = ['testID', 'employeeID', 'attDate', 'timeIn', 'timeOut', 'breakStart', 'breakEnd', 'billable', 'late', 'undertime', 'deficit', 'excess', 'overtime']
    
    with open('testData.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        
        #check if breakStart is none. If no, run wBreak, if yes, run noBreak
        if breakStartVars[0] == "none":
            print("No Break")
            # noBreak(csvwriter)
        else:
            print("With Break")
            # wBreak(csvwriter)
    
def noBreak(csvwriter):
    global count
    for i in timeInVars:
        for j in timeOutVars:
            row = [count, employeeID, attDate, i, j, '-', '-']
            csvwriter.writerow(row)
            count += 1
            
def wBreak(file):
    global count
    for i in timeInVars:
        for j in timeOutVars:
            for k in breakStartVars:
                for l in breakEndVars:
                    file.write(str(count) + "," + i + ',' + j + ',' + k + ',' + l + '\n')
                    count += 1
              
if __name__ == '__main__':
    main()