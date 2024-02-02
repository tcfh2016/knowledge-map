# -*- coding: utf-8 -*-

import argparse
import os

def parse_args():

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('directory',
                             help='specify the directory.')
    arg_parser.add_argument('-kw', '--keyword', required=True,
                             help='specify the keyword.')

    return arg_parser.parse_args()


'''
ASP-1732-Disp_1 <2023-03-07T16:52:59.024795Z> 520118-L2_LO_DL_RCV0 VIP/L2Lo, DlSlotSynchroCountersUpdate.hpp:82/ttisFromUpdate: 2047 numOfBearers 1500[iniTxPktsRcvd|reTxPktsRcvd: 6726064|6313558] [usedBuffers|overFlowNum|allocated|released: 5308|0|13044864|13039556][Rcvd|Sent|Buffered: 873853703|873853100|603] [EventPoolFreeCount: 35051]
'''
class Sent2Ps(object):
    def __init__(self):
        pass

    def write_header(self, outfile):
        header = 'TimeStamp,' + 'Rcvd,' + 'Sent,' + 'Buffered,' + 'EventPoolFreeCount\n'
        outfile.write(header)

    def doParse(self, line, out_file):
        t_begin = line.find('<');
        t_end = line.find('>');
        ts = line[t_begin + 1 : t_end - 4]

        # [Rcvd|Sent|Buffered: 873853703|873853100|603]
        rcvd_start = line.find('[Rcvd')
        rcvd_end = line.find(']', rcvd_start)        
        rcvd_str = line[rcvd_start : rcvd_end]
        #print(rcvd_str)
        segments = rcvd_str.split(' ')[1].split('|')

        rcvd = segments[0]
        sent = segments[1]
        buff = segments[2]

        # [EventPoolFreeCount: 35051]
        event_start = line.find('EventPoolFreeCount')
        event_end = line.find(']', event_start)
        event_str = line[event_start : event_end]
        #print(event_str)
        event = event_str.split(' ')[1]

        ret_str = ts + ',' + str(rcvd) + ',' + str(sent) + ',' + str(buff) + ',' + str(event) + '\n'
        #print (output_line)
        out_file.write(ret_str)        


'''
ASP-2730-Disp_1 <2024-01-26T08:36:25.329692Z> 1500146-L2_LO_DL_RCV0 INF/L2Lo, DlTracer.cpp:249/PCMD: stop timer for UE with crnti=16927, ueIdDu=75198, loDataUeId=76 timerWheelHandle=128 free_tw=4445
'''
class TimerWheel(object):
    def __init__(self):
        pass

    def write_header(self, outfile):
        header = 'SYSLOG,' + 'TimeStamp,' + 'ASP,' + 'EQ,' + 'crnti,' + 'timerWheelHandle,' + 'free_tw\n'
        outfile.write(header)

    def doParse(self, line, out_file, in_file=''):
        t_begin = line.find('<')
        t_end = line.find('>', t_begin)
        ts = line[t_begin + 1 : t_end - 4]
        
        asp_begin = line.find('ASP')
        asp_end = line.find('<', asp_begin)
        asp_str = line[asp_begin : asp_end - 1]

        eq_begin = line.find('L2_LO_', t_end)
        eq_end = line.find('INF/', eq_begin)
        eq_str = line[eq_begin : eq_end - 1]

        rnti_begin = line.find('crnti', eq_end)
        rnti_end = line.find(',', rnti_begin)
        rnti_str = line[rnti_begin : rnti_end - 1]

        twh_begin = line.find('timerWheelHandle', rnti_end)
        twh_end = line.find(' ', twh_begin)
        twh_str = line[twh_begin : twh_end - 1]

        ftw_start = line.find('free_tw', twh_end)
        ftw_str = line[ftw_start:].strip()


        ret_str = in_file + ',' + ts + ',' + asp_str + ',' + eq_str + ',' + rnti_str.split('=')[1] + ',' + twh_str.split('=')[1] + ',' + ftw_str.split('=')[1] + '\n'        
        out_file.write(ret_str)
        

'''
ASP-1731-Disp_2 <2024-01-29T08:25:51.320814Z> 500126-RlcDlDrbQ1 INF/g1r00Au0007ucp0002t0010h04/Ln:160/rdDebugDlRlcPduBurstsCounters handleBurstData: timeLastTbBuilt:Hfn:378, frame:771, slot:9, btu:760539, slotDurationUs:500, timeLastTbTransmitted:Hfn:378, frame:772, slot:2, btu:0, slotDurationUs:500, totalPduVol:130015B, lastTbVol:34704B
'''
class TotalPduVol(object):
    def __init__(self):
        pass

    def write_header(self, outfile):
        header = 'SYSLOG,' + 'TimeStamp,' + 'ASP,' + 'totalPduVol,' + 'lastTbVol\n'
        outfile.write(header)

    def doParse(self, line, out_file, in_file=''):
        t_begin = line.find('<')
        t_end = line.find('>', t_begin)
        ts = line[t_begin + 1 : t_end - 4]
        
        asp_begin = line.find('ASP')
        asp_end = line.find('<', asp_begin)
        asp_str = line[asp_begin : asp_end - 1]

        tv_begin = line.find('totalPduVol', asp_end)
        tv_end = line.find(',', tv_begin)
        tv_str = line[tv_begin : tv_end]

        lv_start = line.find('lastTbVol', tv_end)
        lv_str = line[lv_start:].strip()

        ret_str = in_file + ',' + ts + ',' + asp_str + ',' + str(int(tv_str.split(':')[1], 16)) + ',' + str(int(lv_str.split(':')[1], 16)) + '\n'
        out_file.write(ret_str)

def main():
    args = parse_args()    

    if args.keyword == 'DlSlotSynchroCountersUpdate.hpp':
        obj =  Sent2Ps()
    elif args.keyword == 'stop timer for UE':
        obj = TimerWheel()
    elif args.keyword == 'totalPduVol:':
        obj = TotalPduVol()

    out_name = args.directory.split('\\')[-1]
    with open(os.path.join(args.directory, out_name + '.csv'), 'w') as out_file:
        obj.write_header(out_file)
        
        files = [os.path.join(args.directory, f) for f in os.listdir(args.directory)]
        for f in sorted(files, key=os.path.getmtime):
            if f.find('.log') == -1:
                continue
            
            print('procss {}...'.format(f))
            for line in open(f):
                if line.find(args.keyword) != -1:
                    obj.doParse(line, out_file, f.split('\\')[-1])


if __name__ == '__main__':
    main()