import src.strategies.strategy as strategy

class MaxRlc(strategy.Strategy):
    def __init__(self):
        pass

    def construct_head_line(self):
        head_line = "cellId," + "crnti," + "ueId," + "ueIndex," + "lcid\n"
        return head_line

    def doParse(self, line):
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
