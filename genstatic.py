# create a file named index.html
# and insert links to every html file in the
# directory that was passed as a command line argument
import sys
import os

from pathlib import Path

# check if the user supplied the correct number of command line arguments
arglen = len(sys.argv)
if arglen !=2 and arglen != 4:
    print("Usage: python index.py htmlfilesdirectory [--listen] [port]")
    sys.exit(1)

listen = False
port = "8000"
if arglen == 4:
    if sys.argv[2] == "--listen":
        listen = True
        port = sys.argv[3]
    else:
        print("Usage: python index.py htmlfilesdirectory [--listen] [port]")
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

# wait 1 second
import time
time.sleep(1)

fullpath = os.path.abspath(dir)
if listen:
    # run a simple python http server to serve the files using SimpleHTTPServer
    # the server will serve files from the directory that was passed as a command line argument
    # the server will run in the background
    import subprocess
    subprocess.Popen(["python3", "-m", "http.server", port, "--directory", fullpath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
