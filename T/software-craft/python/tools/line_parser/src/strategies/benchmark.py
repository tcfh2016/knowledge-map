import src.strategies.strategy as strategy

class Benchmark(strategy.Strategy):
    def __init__(self):
        self.columns = ["EMStart", "EMPreStart", "EMPreEnd", "EMSchStart", "EMSchEnd", "EMPostStart", "EMPostEnd"]

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

            data_start = target.find(' ', element_section_start)
            data_end = target.find(',', element_section_start)

            output_line += (str(target[data_start : data_end]) + ",")

        output_line += '\n'
        #print (output_line)
        return output_line
