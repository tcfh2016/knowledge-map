from sys import argv

print ("Script Name        : ", argv[0])
print ("File to be parsed  : ", argv[1])

def doParseJob(filename):
    if os.path.isdir(filename):
        print ("Start parse directory...")
    else
        print ("Start parse file: %s" %filename)

def main():
    if os.Path.exists(argv[1]):
        print ("")
        doParseJob(argv[1]);
    else:
        print ("File/Directory not exist!")
