from sys import argv

script_name, user_name = argv
prompt = '>>> '

print "Hi %s, I'm the %s script." % (user_name, script_name)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Alright, so you said %r about liking me." % likes
print "You live in %r. Not sure where that is." % lives
print "And you have a %r computer. Nice." % computer
