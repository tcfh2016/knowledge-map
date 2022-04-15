print "How old are you",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight
)


# Change ' to " because ' exist in string.
print "%r %r" % ("But it didn't sing.",	"So I said goodnight.")

# Keep ' unchange because both ' and " exist in string.
print "%r %r" % ("But it didn't sing \"LOVE\".",	"So I said goodnight.")
