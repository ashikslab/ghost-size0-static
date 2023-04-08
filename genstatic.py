# create a file named index.html
# and insert links to every html file in the
# directory that was passed as a command line argument
import sys
import os
from pathlib import Path

# check if the user supplied the correct number of command line arguments
if len(sys.argv) != 2:
    print("Usage: python index.py htmlfilesdirectory")
    sys.exit(1)

# set the directory from the command line argument
dir = sys.argv[1]
# create a file named index.html
outfile = open("index.html", "w")
#write a <html> tag to the file
outfile.write("<html>")
# insert links to every html file in the
# directory that was passed as a command line argument
for file in os.listdir(dir):
    if file.endswith(".html"):
        # write the link to the html file
        outfile.write("<a href=" + file + ">" + file + "</a><br>")
# close the file
#write a </html> tag to the file
outfile.write("</html>")
outfile.close