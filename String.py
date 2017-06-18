print "Mary had a little lamb"
print "Its fleece was white as %s ." %'snow'
print "And everywhere that Mary went."

print "." * 10 # what'd that dO?
 # in ra 10 dau cham lien nhau

end1 = "S"
end2 = "O"
end3 = "N"
print end1+end2+end3

print "*" * 50

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)

print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)

print "*" *50

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# cac truyen tham so : , <thamso>
# hoac la %s : % <thamso>
print "here are the days : %s " % days
print "here are the months : %s"% months
# print paragraph, we must use """
print """ There's something going on here.
With the three double- quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6. """
