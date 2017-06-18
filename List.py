stuff = {'name' : 'son', 'age' : 21, 'tall':172}

print stuff
print stuff['name']
print stuff['age']
print stuff['tall']

stuff['city'] = "Ho Chi Minh"

print stuff
print stuff['city']

# them vao vi tri 1,2

stuff[1] = "Wow"

stuff[2] = "neato"

print stuff[1]

print stuff[2]

print stuff

del stuff[1]
del stuff[2]
print stuff
