# makeWebPageExample.py   From lab06 for CS20, Spring 2016, P. Conrad UCSB
# Practice with files---this makes a web page from
#   the  student.txt file we used in lab06, or any file in the same format

import os  # This allows access to operating system features

def webDirectory():
    """
    returns a string containing the folder associated with
    web directory http://www.cs.ucsb.edu/~yourusername/cs20/lab06
    """
    
    # Get the home directory

    myHome = os.getenv("HOME")
    if (type(myHome)!=str):
        
       # raise Exception is a way to force Python to vomit
       # if we've run into a situation we don't know how to handle
       raise Exception("Can't get home directory")

    return myHome + "/public_html/cs20/lab06"


def webAddress():
    """
    returns the URL (complete with the correct username) for
    http://www.cs.ucsb.edu/~yourusername/cs20/lab06
    """
    
    # Get the home directory

    myUsername = os.getenv("USER")
    if (type(myUsername)!=str):
        
       # raise Exception is a way to force Python to vomit
       # if we've run into a situation we don't know how to handle
       raise Exception("Can't get home directory")

    return "http://www.cs.ucsb.edu/~" + myUsername + "/cs20/lab06"


def makeWebDirectoryIfItDoesNotExistAlready():
    """
    Create the directory ~/public_html/cs20/lab06 unless it already
    exists.
    """
    # This code checks to see if the web directory
    # ~/public_html/cs20/lab06 already exists
    # If so,we just return---there is nothing to do!
    
    if (os.access(webDirectory(),os.F_OK)):
        return

    # If not, then create a web directory for this lab (cs20/lab06)
    # The 0o755 is the Python way or writing octal number 755 (rwxr-xr-x)

    else:
        os.makedirs(webDirectory(),0o755)

        
        
    # If you run this on CSIL, now you should be able to navigate to
    # http://www.cs.ucsb.edu/~yourusername/cs20/lab06 and see files




def webPageHeader(myTitle):
    """
    Returns a string with the head element for a web page
    with title myTitle.
    
    Example: webPageHeader("Temperatures") returns the
    header for a web page with temperatures on it, i.e.
    <head>
      <title>Temperatures</title>
    </head>
    """

    return ("<head>\n" +
      " <title>"+ myTitle + "</title>\n" + 
      "</head>\n")
    

def convertStudents2Table(inputFileName,outputFileName):
    """
    Takes the students.txt file we used in an earlier step of the lab
    and converts it into students.html that can be written to
    the web.
    """

    # Open the input file

    studentFile = open(inputFileName,"r")

    # Open the output file


    makeWebDirectoryIfItDoesNotExistAlready()

    htmlFileName = webDirectory() + "/" + outputFileName

    htmlFile = open(htmlFileName,"w")

    # Write the start of the HTML file
    
    htmlFile.write("<html>\n")
    htmlFile.write(webPageHeader("Table of Students"))
    htmlFile.write("<body>\n")
    htmlFile.write("<h1>Table of Students</h1>\n")
    htmlFile.write("<table border='1'>\n")

    # Write the table header

    htmlFile.write("<tr><th>First Name</th><th>Last Name</th><th>Major</th></tr>\n")
    
    # process every line in the file---and for each one
    # write a line to the html for the web page
    
    for line in studentFile:

        # Convert this line into a list
        lineAsAList = line.strip().split(",")

        # Pull out the first name, last name and major
        fname = lineAsAList[0].strip()
        lname = lineAsAList[1].strip()
        major = lineAsAList[2].strip()


        # Write one line to the table

        htmlFile.write("<tr>" +
                       "<td>" + fname + "</td>" +
                       "<td>" + lname + "</td>" +
                       "<td>" + major + "</td>" +
                       "</tr>")

    htmlFile.write("</table>\n")
    htmlFile.write("</body>\n")
    htmlFile.write("</html>\n")

    # close the intput file and the output file
    
    studentFile.close()
    htmlFile.close()

    # Tell the user where to find the page

    print("Look for the web page at this URL:\n")
    print(" " + webAddress() + "/" + outputFileName)

    print("Or if working on a PC or Mac, at this one:\n")
    print(" file://" + htmlFileName)

    
