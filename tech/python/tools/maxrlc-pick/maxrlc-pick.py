from sys import argv

print ("Script Name        : ", argv[0])
print ("File to be splitted: ", argv[1])

# Keywords.
keyword = "MaxRlcRetransExceeded"

# Genarate output file name by 'input_filename' and 'keywords'.
input_filename = argv[1]
output_filename = argv[1] + ".csv"

def doParse(line):
    target_start = line.find("L2TupuDl/") + len("L2TupuDl/")
    target_end = line.find("/MAC")
    target = line[target_start:target_end]
    print (target)

    cStart = target.find('c')
    rStart = target.find('r')
    uStart = target.find('u')
    xStart = target.find('x')
    lStart = target.find('l')

    cellId  = int(target[cStart+1:rStart], 16)
    crnti   = int(target[rStart+1:uStart], 16)
    ueId    = int(target[uStart+1:xStart], 16)
    ueIndex = int(target[xStart+1:lStart], 16)
    lcid    = int(target[lStart+1:], 16)

    output_line = str(cellId) + "," + str(crnti) + "," + str(ueId) + "," + str(ueIndex) + "," + str(lcid) + "\n"
    print (output_line)
    return output_line

def main():
    output_fp = open(output_filename, 'w')
    with open(input_filename) as input_content:
        head_line = "cellId," + "crnti," + "ueId," + "ueIndex," + "lcid\n"
        output_fp.write(head_line)
        for line in input_content:
            if keyword in line:
                #print (line)
                output = doParse(line)
                output_fp.write(output)

    output_fp.close()

main()
