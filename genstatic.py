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
# create a file named index.html inside the directory that was passed as a command line argument
outfile = open(dir + "/index.html", "w")
#write a <html> tag to the file
outfile.write("<html>")
# insert links to every html file in the
# directory that was passed as a command line argument
# Files that start with "page" should be the first ones in the list

for file in sorted(os.listdir(dir)):
    if file.endswith(".html"):
        # skip index.html
        if file == "index.html":
            continue
        # write the link to the html file
        # extract the text inside the title tag in the html file as a string
        title = Path(dir + "/" + file).read_text().split("<title>")[1].split("</title>")[0]
        # write the link to the html file. The link text should be the text inside the title tag
        # and the link should be relative to the index.html file (same directory)
        outfile.write("<a href=\"" + file + "\">" + title + "</a><br>")

# close the file
#write a </html> tag to the file
outfile.write("</html>")
outfile.close
