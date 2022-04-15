from sys import argv

# Get argument from command line.
script, filename = argv

# Print the content from the file the user specified.
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

# Print the content from another file the user choosed.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
