from sys import argv

script, user_name = argv

prompt = '>'

print "hi %s, I'm the %s scipt." % (user_name, script)

print "I'd like to ask you a fer question."

likes = raw_input(prompt)

print likes
