from sys import argv

print ("Script Name        : ", argv[0])
print ("File to be splitted: ", argv[1])

# Genarate output file name by 'input_filename' and 'keywords'.
input_filename = argv[1]
output_filename = argv[1] + ".result"

def parseUeId(line):
    fileds = line.split(":")
    return fileds[len(fileds)-1]

def pickDisconnectionUe():
    fp = open("disconnection-ue.txt", 'w')
    key = "DISCONNECTION"
    with open(input_filename) as input_content:
        for line in input_content:
            if key in line:
                ueId = parseUeId(line)
                print(ueId)
                fp.write(ueId)
    fp.close()

def main():
    pickDisconnectionUe()

    #output_fp = open(output_filename, 'w')
    #output_fp.close()

main()
