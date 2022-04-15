from sys import argv
import os

print("Script Name        : ", argv[0])
print("File to be splitted: ", argv[1])

# Store all keywords.
keywords = ['@features', ]

for i in range(0, len(keywords)):
    print("keyword %s          :  %s" % (i+1, keywords[i]))

# Genarate output file name by 'input_filename' and 'keywords'.
input_filename = argv[1]
output_filename = ""
for i in range(0, len(keywords)):
    output_filename = output_filename + "-" + keywords[i].replace(':', '')
output_filename += '.info'

print("output filename %s" % output_filename)


def matchLine(line):
    for keyword in keywords:
        if keyword in line:
            return True
    return False


# Search file.
def searchFile(inputFile, outputFile):
    if os.path.isfile(inputFile):
        print("reading file: %s" % (inputFile))
        with open(inputFile, encoding="utf-8") as input_content:
            for line in input_content:
                if matchLine(line):
                    feature_string_start = line.find('5G')
                    feature_id = line[feature_string_start:]
                    print("%s -- %s" % (inputFile, feature_id))
                    outputFile.write(inputFile + ',' + feature_id)
    elif os.path.isdir(inputFile):
        for filename in os.listdir(inputFile):
            f = os.path.join(inputFile, filename)
            searchFile(f, outputFile)


def main():
    output_fp = open(output_filename, 'w')
    searchFile(input_filename, output_fp)
    output_fp.close()


main()
