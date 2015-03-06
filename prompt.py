from sys import argv


script, u_name = argv
print "Hi %s, this is %s script." %(u_name,script)

prompt = '>'
print "Hi %s do you like me" %(u_name)
likes = raw_input(prompt)

print likes + " I like you"
