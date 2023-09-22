# -*- coding: utf-8 -*-

import argparse
import os

def parse_args():

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("directory",
                             help="specify the directory.")
    arg_parser.add_argument("-kw", "--keyword", required=True,
                             help="specify the keyword.")

    return arg_parser.parse_args()


'''
DL-PDCP numOfBearers:6, bearerGroup:0, inB:2686608, outB:2678832, disB:0, inP:1944, outP:1944, disP:0, disTmrB:0, disTmrP:0, disBcB:0, disBcP:0
'''
class Sent2Ps(object):
    def __init__(self):
        pass

    def write_header(self, outfile):
        header = "TimeStamp," + "numOfBearers," + "bearerGroup," + "inB," + "outB," + "disB," + "inP," + "outP," + "disP," + "disTmrB," + "disTmrP," + "disBcB," + "disBcP\n"
        outfile.write(header)

    def doParse(self, line, out_file):
        t_begin = line.find("<");
        t_end = line.find(">");
        ts = line[t_begin + 1 : t_end - 4]

        # numOfBearers:6,
        data = {}
        start = line.find("numOfBearers:")
        temp = line[start :]
        for pair in temp.split(','):
            ws = pair.strip().split(':')            
            data[ws[0]] = ws[1]

        ret_str = (ts + "," + 
                   str(data['numOfBearers']) + "," + 
                   str(data['bearerGroup']) + "," + 
                   str(data['inB']) + "," + 
                   str(data['outB']) + "," + 
                   str(data['disB']) + "," + 
                   str(data['inP']) + "," + 
                   str(data['outP']) + "," + 
                   str(data['disP']) + "," + 
                    str(data['disTmrB']) + "," + 
                   str(data['disTmrP']) + "," + 
                   str(data['disBcB']) + "," + 
                   str(data['disBcP']) + "\n")
        print (ret_str)
        out_file.write(ret_str)        
    

def main():
    args = parse_args()    

    if args.keyword == "DL-PDCP numOfBearers:":
        obj =  Sent2Ps()

    with open(os.path.join(args.directory, "out.csv"), "w") as out_file:
        obj.write_header(out_file)
        
        files = [os.path.join(args.directory, f) for f in os.listdir(args.directory)]
        for f in sorted(files): #, key=os.path.getmtime
            if f.find(".log") == -1:
                continue
            
            print("procss {}...".format(f))
            #source_file = os.path.join(args.directory, f)            
            for line in open(f):
                if line.find(args.keyword) != -1:# and line.find("ASP-1732") != -1:
                    obj.doParse(line, out_file)


if __name__ == "__main__":
    main()