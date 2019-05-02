import src.strategies.benchmark as benchmark
import src.strategies.maxrlc as maxrlc

class Parser(object):
    def __init__(self, opt):
        self.input_filename = opt.file
        self.output_filename = opt.file + ".csv"

        self.keyword = opt.keyword
        self.pattern = opt.pattern

    def get_parse_strategy(self):
        if self.pattern == "maxrlc":
            strategy = maxrlc.MaxRlc()
        elif self.pattern == "benchmark":
            strategy = benchmark.Benchmark()
        else:
            assert 0, "Not support"

        return strategy

    def parse(self):
        output_fp = open(self.output_filename, 'w')
        with open(self.input_filename) as input_content:
            strategy = self.get_parse_strategy()
            head_line = strategy.construct_head_line()
            output_fp.write(head_line)
            for line in input_content:
                if self.keyword in line:
                    #print (line)
                    output = strategy.doParse(line)
                    output_fp.write(output)

        output_fp.close()
