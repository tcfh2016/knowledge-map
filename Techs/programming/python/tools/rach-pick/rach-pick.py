from sys import argv

print ("Script Name        : ", argv[0])
print ("File to be splitted: ", argv[1])

# Genarate output file name by 'input_filename' and 'keywords'.
input_filename = argv[1]
output_filename = argv[1] + ".csv"

def parseUeId(line):
    fileds = line.split(":")
    return fileds[len(fileds)-1]

def pickDisconnectionUe():
    fp = open(output_filename, 'w')
    key = "addDrxUeData"
    with open(input_filename) as input_content:
        for line in input_content:
            if key in line:
                l = line.find("<")
                r = line.find(">")
                timestamp = line[l+12:r-4]
                r = line.find("rnti")
                rnti = line[r+5:]

                s = timestamp.split(':')
                h = s[0]
                m = s[1]
                s = s[2].split('.')
                str = h + ',' + m + ',' + s[0] + ',' + s[1] + ',' + rnti
                fp.write(str)
    fp.close()

def main():
    pickDisconnectionUe()

    #output_fp = open(output_filename, 'w')
    #output_fp.close()

main()
