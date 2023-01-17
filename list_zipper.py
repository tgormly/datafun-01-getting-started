"""
Illustrates the builtin zip() function.

Take two lists and zip them together into a list of tuples.

"""

xtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]
zvalues = [2, 2, 2, 4, 4, 4, 6, 6, 6, 8, 8, 8]

# zip the lists together
zipped = zip(xtimes, yvalues, zvalues)

# convert the zipped object to a list with builtin list() function
zipped_list = list(zipped)

# open a file for writing
# use the built-in open() function, and 'w' mode to allow writing
outfile = open("list_zipperout.csv", "w")

# for each row in our list
for row in zipped_list:

    # unpack the tuple e.g., (x,y) into variables named x and y
    x, y, z = row
    # create a string with the x and y values
    # end each line with a newline character \n
    outrow = str(x) + "," + str(y) + "," + str(z) + "\n"
    # write the string to the file
    outfile.write(outrow)

# close the file object when done
outfile.close()
