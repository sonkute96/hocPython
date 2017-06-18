ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that"

stuff = ten_things.split(' ') # gan stuff = ten_things nhung duoc format lai voi ''

print stuff
more_stuff = ["Day", "Night", "Song", "Corn"]

while len(stuff) != 10:

    next_one = more_stuff.pop() # pop() lay tu sau den dauTH
    print "Adding :", next_one
    stuff.append(next_one)

    print "there are %d items now." % len(stuff)

print "there we go:",stuff
print "*" *50

print stuff[1]
print stuff[-2]

print stuff.pop()

print ' '.join(stuff)

print '#'.join(stuff[3:5]) # in ra gia tri cua stuff[3]  & stuff[4]
