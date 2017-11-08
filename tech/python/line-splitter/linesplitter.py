from sys import argv

script_name, file_name, key_word1, key_word2 = argv

print ("Script Name:         %s" % script_name)
print ("File to be splitted: %s" % file_name)
print ("key_word1:            %s" % key_word1)
print ("key_word2:            %s" % key_word2)

def main():
    output_filename = file_name + "-" + key_word1 + "-" + key_word2
    output_fp = open(output_filename, 'w')

    with open(file_name) as input_content:
        for line in input_content:
            if key_word1 in line or key_word2 in line:
                print (line)
                output_fp.write(line)

    output_fp.close()

main()
