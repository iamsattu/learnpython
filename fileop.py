from sys import argv

script, filename = argv
prompt = ">"

filename = raw_input(prompt)

text = open(filename)
print text.read()
