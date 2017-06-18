# muon su dung while
# accessing elements of lists

# ex35
def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input(" > ")

    if "0" in choice or "1" in choice:

        print " gia tri cua choice la ",choice 
    else:
        dead("Man, learn to type a number.")

def dead(why):
    print why, "Good job !"
gold_room()
