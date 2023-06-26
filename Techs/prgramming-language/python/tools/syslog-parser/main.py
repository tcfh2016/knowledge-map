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
ASP-1732-Disp_1 <2023-03-07T16:52:59.024795Z> 520118-L2_LO_DL_RCV0 VIP/L2Lo, DlSlotSynchroCountersUpdate.hpp:82/ttisFromUpdate: 2047 numOfBearers 1500[iniTxPktsRcvd|reTxPktsRcvd: 6726064|6313558] [usedBuffers|overFlowNum|allocated|released: 5308|0|13044864|13039556][Rcvd|Sent|Buffered: 873853703|873853100|603] [EventPoolFreeCount: 35051]
'''
class Sent2Ps(object):
    def __init__(self):
        pass

    def write_header(self, outfile):
        header = "TimeStamp," + "Rcvd," + "Sent," + "Buffered," + "EventPoolFreeCount\n"
        outfile.write(header)

    def doParse(self, line, out_file):
        t_begin = line.find("<");
        t_end = line.find(">");
        ts = line[t_begin + 1 : t_end - 4]

        # [Rcvd|Sent|Buffered: 873853703|873853100|603]
        rcvd_start = line.find("[Rcvd")
        rcvd_end = line.find("]", rcvd_start)        
        rcvd_str = line[rcvd_start : rcvd_end]
        #print(rcvd_str)
        segments = rcvd_str.split(" ")[1].split("|")

        rcvd = segments[0]
        sent = segments[1]
        buff = segments[2]

        # [EventPoolFreeCount: 35051]
        event_start = line.find("EventPoolFreeCount")
        event_end = line.find("]", event_start)
        event_str = line[event_start : event_end]
        #print(event_str)
        event = event_str.split(" ")[1]

        ret_str = ts + "," + str(rcvd) + "," + str(sent) + "," + str(buff) + "," + str(event) + "\n"
        #print (output_line)
        out_file.write(ret_str)        
    

def main():
    args = parse_args()    

    if args.keyword == "DlSlotSynchroCountersUpdate.hpp":
        obj =  Sent2Ps()

    with open(os.path.join(args.directory, "out.csv"), "w") as out_file:
        obj.write_header(out_file)
        
        files = [os.path.join(args.directory, f) for f in os.listdir(args.directory)]
        for f in sorted(files, key=os.path.getmtime):
            if f.find(".LOG") == -1:
                continue
            
            print("procss {}...".format(f))
            source_file = os.path.join(args.directory, f)            
            for line in open(source_file):
                if line.find(args.keyword) != -1 and line.find("ASP-1732") != -1:
                    obj.doParse(line, out_file)


if __name__ == "__main__":
    main()