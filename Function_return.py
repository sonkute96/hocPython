def secret_formula(started):
    jelly_beans = started * 500

    jars = jelly_beans / 1000

    crates = jars / 100

    # tra ve
    return jelly_beans, jars, crates
start_point = 10000

beans, jars, crates = secret_formula(start_point)

print "beans = %r , jars = %r , crates = %r " % (beans,jars,crates)
