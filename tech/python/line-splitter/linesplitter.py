from sys import argv

print ("Script Name        : ", argv[0])
print ("File to be splitted: ", argv[1])

# Store all keywords.
keywords = []
for i in range(2, len(argv)):
    keywords.append(argv[i])

for i in range(0, len(keywords)):
    print ("keyword %s          :  %s" %(i+1, keywords[i]))

# Genarate output file name by 'input_filename' and 'keywords'.
input_filename = argv[1]
output_filename = argv[1]
for i in range(0, len(keywords)):
    print ("keyword %s          :  %s" %(i+1, keywords[i]))
    output_filename = output_filename + keywords[i]

def main():
    output_fp = open(output_filename, 'w')

    with open(input_filename) as input_content:
        for line in input_content:
            for keyword in keywords:
                if keyword in line:
                    print (line)
                    output_fp.write(line)
                    break

    output_fp.close()

main()
