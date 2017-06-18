from sys import argv
# sys la mot cai package.
script, nameFile = argv

txt = open(nameFile)

print "Content of File :"

#print txt.read()

print txt.read(10)
txt.close()
