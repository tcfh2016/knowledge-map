import src.strategies.strategy as strategy

'''
L2HiDu, g0r186u0944ucp1A57t0097h04/RlcDlRbBase.hpp:296/T_PollTransmission expired, trigger reTx for last sent pdu, txNextAck=22284, txNext=22319, rbIndex=3047 fli=0
'''
class PollExpire(strategy.Strategy):
    def __init__(self):
        pass

    def construct_head_line(self):
        head_line = "TimeStamp," + "BearGroup," + "BearIndex," + "UeId," + "UeIdCu," + "LodataUeId," + "LogicalChannelId," +  "txNextAck," + "txNext," + "rbIndex\n"
        return head_line

    def doParse(self, line):
        timestamp_begin = line.find("<");
        timestamp_end = line.find(">");
        ts = line[timestamp_begin+1:timestamp_end]

        target_start = line.find("L2HiDu,") + len("L2HiDu,")
        target_end = line.find("/RlcDlRbBase")
        target = line[target_start:target_end]
        print (target)

        gStart = target.find('g')
        rStart = target.find('r')
        uStart = target.find('u')
        pStart = target.find('ucp')
        tStart = target.find('t')
        hStart = target.find('h')

        # , txNextAck=21497, txNext=21533, rbIndex=630 fli=0
        info = line[line.find("txNextAck=") : line.find("fli=")]
        txNextAck_begin = info.find('=')
        txNextAck_end = info.find(',')
        txNextAck = info[txNextAck_begin+1:txNextAck_end]

        info = info[info.find("txNext="):]
        txNext_begin = info.find('=')
        txNext_end = info.find(',')
        txNext = info[txNext_begin+1:txNext_end]

        info = info[info.find("rbIndex="):]
        rbIndex= info[info.find("=")+1:]

        BearGroup         = int(target[gStart+1:rStart], 16)
        BearIndex         = int(target[rStart+1:uStart], 16)
        UeId              = int(target[uStart+1:pStart], 16)
        UeIdCu            = int(target[pStart+3:tStart], 16)
        LodataUeId        = int(target[tStart+1:hStart], 16)
        LogicalChannelId  = int(target[hStart+1:], 16)

        output_line = ts + "," + str(BearGroup) + "," + str(BearIndex) + "," + str(UeId) + "," + str(UeIdCu) + "," + str(LodataUeId) + "," + str(LogicalChannelId) + "," + txNextAck + "," + txNext + "," + rbIndex + "\n"
        print (output_line)
        return output_line
