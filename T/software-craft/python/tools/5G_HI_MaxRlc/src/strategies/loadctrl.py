import src.strategies.strategy as strategy

#DL LoadCtrl: cellId=81, psa=33916, ba=42869, cCha=6001, ta=5474, fa=77177, pa=8262, numUes=0, tdUes=50, fdEstAvg=12.89, fdSchedAvg=0.00, maxNumUeFdDl=14, isUnlicensedScell=0, maxNumUesUl=20, UesReqa=0.00, loadState=0(0), cpuLx100=1397, imOffset=0, ticksPresc=1, ThresUvpt1=2 cycleMargin=118913 ratioQ7=128 avgPrePost=
class LoadCtrl(strategy.Strategy):
    def __init__(self):
        self.columns = ["cellId", "fdEstAvg", "fdSchedAvg", "loadState"]
        #self.columns = ["cellId", "numFdUesAvg", "avgRequested", "loadState"]

    def construct_head_line(self):
        line = ""
        for elem in self.columns:
            line += (elem + ",")
        line += '\n'
        return line

    def doParse(self, line):
        target_start = line.find(self.columns[0])
        target = line[target_start:]
        print (target)

        output_line = ""
        for i in range(len(self.columns)):
            element_section_start = target.find(self.columns[i])

            data_start = target.find('=', element_section_start) + 1
            data_end = target.find(',', element_section_start)
            #data_start = target.find('=', element_section_start) + 1
            #data_end = target.find(' ', element_section_start)

            output_line += (str(target[data_start : data_end]) + ",")

        output_line += '\n'
        #print (output_line)
        return output_line
