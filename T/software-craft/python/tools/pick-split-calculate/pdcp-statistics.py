from sys import argv

print ("Script Name        : ", argv[0])
print ("File to be splitted: ", argv[1])
print ("Keyword: ", argv[2])

# Keywords.
keyword = argv[2]
line_count_DataPdu = 0
line_count_DrbS1 = 0


# INF/PDCP/STATS/DL: DRB S1: 0 0 0 X2: 0 0 0 inBytes: 0 0 0 toRLC: 0 0 0 inBytes: 0 0 0 ACK: 0 0 0 NACK: 0 0 0
# INF/PDCP/STATS/UL: DataPDU: 16 7 9 SR: 0 RoHCF: 0 toSGW: 14 14 9 Fwd: 0 0 0 BuffPkt: 8 8 8 BuffData: 416 416 416

# Genarate output file name by 'input_filename' and 'keywords'.
input_filename = argv[1]
output_filename = argv[1] + keyword + ".csv"

# for DataPDU statistics.
dataPdu1 = []
dataPdu2 = []
dataPdu3 = []
sr = []
roHcf = []
toSgw1 = []
toSgw2 = []
toSgw3 = []
fwd1 = []
fwd2 = []
fwd3 = []
buffPkt1 = []
buffPkt2 = []
buffPkt3 = []
buffData1 = []
buffData2 = []
buffData3 = []

# for DRB S1.
s1 = []
s2 = []
s3 = []
x1 = []
x2 = []
x3 = []
inBytes1 = []
inBytes2 = []
inBytes3 = []
toRLC1 = []
toRLC2 = []
toRLC3 = []
ack1 = []
ack2 = []
ack3 = []
nack1 = []
nack2 = []
nack3 = []

def parseTimestamp(line):
    start = line.find("<")
    end = line.find(">")
    return line[start+1:end]

def clearDataPdu():
    dataPdu1.clear()
    dataPdu2.clear()
    dataPdu3.clear()
    sr.clear()
    roHcf.clear()
    toSgw1.clear()
    toSgw2.clear()
    toSgw3.clear()
    fwd1.clear()
    fwd2.clear()
    fwd3.clear()
    buffPkt1.clear()
    buffPkt2.clear()
    buffPkt3.clear()
    buffData1.clear()
    buffData2.clear()
    buffData3.clear()

def clearDrbS1():
    s1.clear()
    s2.clear()
    s3.clear()
    x1.clear()
    x2.clear()
    x3.clear()
    inBytes1.clear()
    inBytes2.clear()
    inBytes3.clear()
    toRLC1.clear()
    toRLC2.clear()
    toRLC3.clear()
    ack1.clear()
    ack2.clear()
    ack3.clear()
    nack1.clear()
    nack2.clear()
    nack3.clear()

def doDrbS1Parse(line):
    global line_count_DrbS1
    line_count_DrbS1 += 1

    # S1.
    s_start = line.find("S1")
    s_end = line.find("X2")
    s_str = line[s_start:s_end]
    pair = s_str.split(' ')

    s1.append(int(pair[1]))
    s2.append(int(pair[2]))
    s3.append(int(pair[3]))

    # X2.
    x_start = line.find("X2")
    x_end = line.find("inBytes")
    x_str = line[x_start:x_end]
    pair = x_str.split(' ')

    x1.append(int(pair[1]))
    x2.append(int(pair[2]))
    x3.append(int(pair[3]))

    # inBytes.
    inBytes_start = line.find("inBytes")
    inBytes_end = line.find("toRLC")
    inBytes_str = line[inBytes_start:inBytes_end]
    pair = inBytes_str.split(' ')

    inBytes1.append(int(pair[1]))
    inBytes2.append(int(pair[2]))
    inBytes3.append(int(pair[3]))

    # toRLC.
    toRlc_start = line.find("toRLC")
    temp = line[toRlc_start:]
    toRlc_end = temp.find("inBytes")
    toRlc_str = temp[:toRlc_end]
    pair = toRlc_str.split(' ')

    toRLC1.append(int(pair[1]))
    toRLC2.append(int(pair[2]))
    toRLC3.append(int(pair[3]))

    # ACK.
    ack_start = line.find("ACK")
    ack_end = line.find("NACK")
    ack_str = line[ack_start:ack_end]
    pair = ack_str.split(' ')

    ack1.append(int(pair[1]))
    ack2.append(int(pair[2]))
    ack3.append(int(pair[3]))

    # BuffPkt.
    nack_start = line.find("NACK")
    nack_str = line[nack_start:]
    pair = nack_str.split(' ')

    nack1.append(int(pair[1]))
    nack2.append(int(pair[2]))
    nack3.append(int(pair[3]))

    #print (pair[1] + " " + pair[2] + " " + pair[3])
    dataDrbS1Line = ''

    if (line_count_DrbS1 % 4 == 0):
        timestamp = parseTimestamp(line)
        _s = "," + str(sum(s1)) + "," + str(sum(s2)) + "," + str(sum(s3))
        _x = "," + str(sum(x1)) + "," + str(sum(x2)) + "," + str(sum(x3))
        _inBytes =  "," + str(sum(inBytes1)) + "," + str(sum(inBytes2)) + "," + str(sum(inBytes3))
        _toRLC = "," + str(sum(toRLC1)) + "," + str(sum(toRLC2)) + "," + str(sum(toRLC3))
        _ack =  "," + str(sum(ack1)) + "," + str(sum(ack2)) + "," + str(sum(ack3))
        _nack =  "," + str(sum(nack1)) + "," + str(sum(nack2)) + "," + str(sum(nack3))
        dataDrbS1Line = timestamp + _s + _x + _inBytes + _toRLC + _ack + _nack + "\n"
        clearDrbS1()
    return dataDrbS1Line

def doDataPduParse(line):
    global line_count_DataPdu
    line_count_DataPdu += 1

    # DataPdu.
    dataPdu_start = line.find("DataPDU")
    dataPdu_end = line.find("SR")
    dataPdu_str = line[dataPdu_start:dataPdu_end]
    pair = dataPdu_str.split(' ')

    dataPdu1.append(int(pair[1]))
    dataPdu2.append(int(pair[2]))
    dataPdu3.append(int(pair[3]))

    # SR.
    sr_start = line.find("SR")
    sr_end = line.find("RoHCF")
    sr_str = line[sr_start:sr_end]
    pair = sr_str.split(' ')

    sr.append(int(pair[1]))

    # RoHCF
    roHcf_start = line.find("RoHCF")
    roHcf_end = line.find("toSGW")
    roHcf_str = line[roHcf_start:roHcf_end]
    pair = roHcf_str.split(' ')

    roHcf.append(int(pair[1]))

    # toSGW.
    toSgw_start = line.find("toSGW")
    toSgw_end = line.find("Fwd")
    toSgw_str = line[toSgw_start:toSgw_end]
    pair = toSgw_str.split(' ')

    toSgw1.append(int(pair[1]))
    toSgw2.append(int(pair[2]))
    toSgw3.append(int(pair[3]))

    # Fwd.
    fwd_start = line.find("Fwd")
    fwd_end = line.find("BuffPkt")
    fwd_str = line[fwd_start:fwd_end]
    pair = fwd_str.split(' ')

    fwd1.append(int(pair[1]))
    fwd2.append(int(pair[2]))
    fwd3.append(int(pair[3]))

    # BuffPkt.
    buffPkt_start = line.find("BuffPkt")
    buffPkt_end = line.find("BuffData")
    buffPkt_str = line[buffPkt_start:buffPkt_end]
    pair = buffPkt_str.split(' ')

    buffPkt1.append(int(pair[1]))
    buffPkt2.append(int(pair[2]))
    buffPkt3.append(int(pair[3]))

    # BuffPkt.
    buffData_start = line.find("BuffData")
    buffData_str = line[buffData_start:]
    pair = buffData_str.split(' ')

    buffData1.append(int(pair[1]))
    buffData2.append(int(pair[2]))
    buffData3.append(int(pair[3]))

    #print (pair[1] + " " + pair[2] + " " + pair[3])
    dataPduLine = ''

    if (line_count_DataPdu % 4 == 0):
        timestamp = parseTimestamp(line)
        _dataPdu = "," + str(sum(dataPdu1)) + "," + str(sum(dataPdu2)) + "," + str(sum(dataPdu3))
        _sr = "," + str(sum(sr))
        _roHcf = "," + str(sum(roHcf))
        _toSgw = "," + str(sum(toSgw1)) + "," + str(sum(toSgw2)) + "," + str(sum(toSgw3))
        _buffPkt =  "," + str(sum(buffPkt1)) + "," + str(sum(buffPkt2)) + "," + str(sum(buffPkt3))
        _tofwd = "," + str(sum(fwd1)) + "," + str(sum(fwd2)) + "," + str(sum(fwd3))
        _buffData =  "," + str(sum(buffData1)) + "," + str(sum(buffData2)) + "," + str(sum(buffData3))

        dataPduLine = timestamp + _dataPdu + _sr + _roHcf + _toSgw + _tofwd + _buffPkt + _buffData + "\n"
        clearDataPdu()
    return dataPduLine


def compose_header():
    if keyword == "DataPDU":
        head_line = "timestamp,"+ "DataPDU1,"+ "DataPDU2,"+ "DataPDU3,"+ "SR," + "RoHCF," + "toSGW1," + "toSGW2," + "toSGW3," + "Fwd1," + "Fwd2," + "Fwd3," + "BuffPkt1," + "BuffPkt2," + "BuffPkt3," + "BuffData1," + "BuffData2," + "BuffData3\n"
    elif keyword == "DRB S1":
        head_line = "timestamp,"+ "DRB S1-1,"+ "DRB S1-2,"+ "DRB S1-3,"+ "X2-1," + "X2-2," + "X2-3," + "inBytes1,"  + "inBytes2,"  + "inBytes3," + "toRLC1,"  + "toRLC2,"  + "toRLC3," + "ACK1," + "ACK2," + "ACK3," + "NACK1," + "NACK2," + "NACK3\n"

    return head_line

def main():
    output_fp = open(output_filename, 'w')
    with open(input_filename) as input_content:
        head_line = compose_header()
        if (head_line != ''):
            output_fp.write(head_line)

        for line in input_content:
            if keyword in line:
                if keyword == "DataPDU":
                    output = doDataPduParse(line)
                elif keyword == "DRB S1":
                    output = doDrbS1Parse(line)

                #print (line)
                if (output != ''):
                    output_fp.write(output)

    output_fp.close()

main()
