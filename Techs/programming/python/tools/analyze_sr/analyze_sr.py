# 分析sr设置与ue删除，统计某时刻各种offset对应的UE个数。
from sys import argv

print("Script Name        : ", argv[0])
print("File to be splitted: ", argv[1])
input_filename = argv[1]
output_filename = argv[1] + ".done"

records = []
info_structure = []

def parse_sr_configuration(line):
    timestamp_start_char = line.find('<')
    timestamp_stop_char = line.find('>')
    timestamp = line[timestamp_start_char + 1:timestamp_stop_char]

    ue_index_start_char = line.find('ueIndex')
    ue_index_end_char = line.find(',', ue_index_start_char)
    ue_index = line[ue_index_start_char:ue_index_end_char].split('=')[1]

    offset_start_char = line.find('offset')
    offset_end_char = line.find(',', offset_start_char)
    offset = line[offset_start_char:offset_end_char].split('=')[1]

    print("time=%s ueindex=%s offset=%s" % (timestamp, ue_index, offset))
    return [timestamp, ue_index, offset]

def parse_ue_info(line):
    timestamp_start_char = line.find('<')
    timestamp_stop_char = line.find('>')
    timestamp = line[timestamp_start_char + 1:timestamp_stop_char]

    ue_index_start_char = line.find('uePsIndex')
    ue_index = line[ue_index_start_char:].split('=')[1]

    print("uePsIndex=%s" % (ue_index))
    return [timestamp, ue_index]

def iterate_records_and_output_summary(ue_info, output_fp):
    counter = [0] * 81
    print("UE DELETE\n")
    print(ue_info)

    for item in records:
        counter[int(item[2])] += 1

        if item[1] == ue_info[1].rstrip():
            records.remove(item)
            print("UE DELETE: %s %s" % (item[1], ue_info[1]))

            print(ue_info)
            output_fp.write(str(ue_info))
            output_fp.write('ueDelete\n')
            print(counter)

    output_fp.write(str(counter))
    output_fp.write('summary\n')

def output_summary(output_fp, extr_info):
    counter = [0] * 81

    for item in records:
        counter[int(item[2])] += 1

    output_fp.write(str(extr_info))
    output_fp.write('srconfig\n')
    output_fp.write(str(counter))
    output_fp.write('\n')

def main():
    output_fp = open(output_filename, 'w')

    with open(input_filename) as input_content:
        for line in input_content:
            if "period=4" in line:
                sr_config = parse_sr_configuration(line)
                records.append(sr_config)
                output_summary(output_fp, sr_config)
            if "handlePsUeDeleteReq" in line:
                ue_info = parse_ue_info(line)
                iterate_records_and_output_summary(ue_info, output_fp)

    output_fp.close()

main()
