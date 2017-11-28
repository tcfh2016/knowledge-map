from sys import argv

print ("Script Name        : ", argv[0])
print ("File to be splitted: ", argv[1])

# Keywords.
keyword = "User statistics"

# Genarate output file name by 'input_filename' and 'keywords'.
input_filename = argv[1]
output_filename = argv[1] + ".csv"

def parseCpuInfo(line):
    start = line.find("FSP")
    end = line.find("<")
    return line[start:end]

def parseTimestamp(line):
    start = line.find("<")
    end = line.find(">")
    return line[start+1:end]

def parseUserInfo(line):
    start = line.find("totalNumUser")
    target = line[start:]
    words = target.split(',')

    pair = words[0].split(':')
    totalNumUser = pair[1]
    pair = words[1].split(':')
    cellId = pair[1]
    pair = words[2].split(':')
    numUserCell = pair[1]
    pair = words[3].split(':')
    PCellPool = pair[1]
    pair = words[4].split(':')
    DataPool = pair[1]
    pair = words[5].split(':')
    numUserData = pair[1]
    pair = words[6].split(':')
    ueGroup = pair[1]

    return (totalNumUser + "," + cellId + "," + numUserCell + "," + PCellPool + "," + DataPool + "," + numUserData + "," + ueGroup)

#FSP-124A-Disp_3 <2017-11-27T12:26:36.540850Z> 3B INF/LTE L2/L2Manager/cB4F1r1FA9uF7Ex2E7lF/User statistics: totalNumUser:1840,cellId:46321,numUserCell:545,PCellPool:1,DataPool:1,numUserData:1838,ueGroup:3
def doParse(line):
    cpuInfo = parseCpuInfo(line)
    timestamp = parseTimestamp(line)
    userInfo = parseUserInfo(line)

    statisticLine = cpuInfo + "," + timestamp + "," + userInfo
    print (statisticLine)
    return statisticLine

def main():
    output_fp = open(output_filename, 'w')
    with open(input_filename) as input_content:
        head_line = "cpuinfo,"+ "timestamp,"+ "totalNumUser,"+ "cellId," + "numUserCell," + "PCellPool," + "DataPool," + "numUserData," + "ueGroup\n"
        output_fp.write(head_line)
        for line in input_content:
            if keyword in line:
                #print (line)
                output = doParse(line)
                output_fp.write(output)

    output_fp.close()

main()
