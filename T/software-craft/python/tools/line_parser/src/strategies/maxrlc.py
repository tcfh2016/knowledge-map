import src.strategies.strategy as strategy

'''
ASP-1831-Disp_3 <2021-07-27T08:22:56.794262Z> 14B-L2RlcDLQ INF/L2HiDu, g1r003u823Bucp1199t0010h04/RlcDlRbBase.cpp:120/Sending BearerErrorIndication due to MaxRlcRetransmission exceeded
'''
class MaxRlc(strategy.Strategy):
    def __init__(self):
        pass

    def construct_head_line(self):
        head_line = "TimeStamp," + "BearGroup," + "BearIndex," + "UeId," + "UeIdCu," + "LodataUeId," + "LogicalChannelId\n"
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

        BearGroup         = int(target[gStart+1:rStart], 16)
        BearIndex         = int(target[rStart+1:uStart], 16)
        UeId              = int(target[uStart+1:pStart], 16)
        UeIdCu            = int(target[pStart+3:tStart], 16)
        LodataUeId        = int(target[tStart+1:hStart], 16)
        LogicalChannelId  = int(target[hStart+1:], 16)

        output_line = ts + "," + str(BearGroup) + "," + str(BearIndex) + "," + str(UeId) + "," + str(UeIdCu) + "," + str(LodataUeId) + "," + str(LogicalChannelId) + "\n"
        print (output_line)
        return output_line
