NOTE:  THIS LAB IS NOT YET COMPLETE.   PLEASE COME BACK LATER...
================================================================




Goals
=====

Working with Files
------------------

In this lab, we'll start by learning how to create a simple HTML file by hand.

Then we'll learn about working with files.

By the time you have completed this lab, you should be able to understand the concepts of:

-   opening files
-   reading from files
-   closing files

In particular, you'll be able to:

-   read data from a file into a list of strings
-   get rid of extra new lines in that data (using the strip() method)
-   split that data (if separated by spaces, or commas) into separate fields, combine those into a namedtuple object, and add that object to a list of namedtuples
-   work with the resulting list of namedtuples
-   write to a file using Python code
-   read data from a file, convert it to HTML format, and write it to a file on the web

This will also provide additional practice with the concepts of "index" vs. "value" when dealing with lists. 

What you'll be doing
--------------------

Unlike the last several labs, there is no "starting point" file for this lab. You are going to write all of the code step-by-step, though there will be some places where I'll give you some code to copy and paste.

You'll need to come up with your own tests as well.

**For students in CCS CS 20**: You will do this lab on CSIL. Instructions for connecting to CSIL from your own machine can be found in Steps 0-2 of [lab02](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab02/blob/master/README.md).

Pair Programming is OPTIONAL for this lab.

Programming, Step-by-Step
=========================

Follow these steps to complete the assignment

Step 0: Preliminaries
---------------------

### Step 0a: Decide whether to work in pair, or alone, and if in pair, on initial driver/navigator


### Step 0b: Decide whether to work in pair, or alone, and if in pair, on initial driver/navigator

Create a github repo for this lab called CS20-S16-lab06.

* Make it a "private" repo--with the new github plans, you should have the ability to create unlimited private repos.
* Indicate that you want a README file to be created
* Make the .gitignore file be one for Python

### Step 0c: Add collaborators to your repo.


Add the following users to your repo as collaborators (here are some [instructions for doing that](https://help.github.com/articles/adding-collaborators-to-a-personal-repository/))

* pconrad (your instructor)
* sarahmzhong (the undergrad mentor for this course)
* Your Pair Partner, if applicable


### Step 0d: Create a directory for lab06, 

cd into your ~/github directory then use "git clone" to clone your repo.  (If you've forgotten how, ask for help).

cd into your repository folder (i.e. ~/github/CS20-S16-lab06 )

Create a `~/github/CS20-S16-lab06` directory, and start a new file in it called `lab06Funcs.py`, using either emacs or idle as your editor.

NOTE WELL:

-   You may use emacs no matter how you connect.
-   If you want to use IDLE, then you either need
    -   On Windows: MobaXTerm, or PuTTY + XMing
    -   On Mac: ssh -X + XQuartz
    -   On Linux: you are probably good to go with just ssh -X

Once you've opened that file, add a comment to the top of your file like this one (substituting your own name and the current date in the proper spot):

    # lab06Funcs.py  by Agnes Nitt and Jason Ogg for CS20 lab06,  11/13/2013
    # Writing to files in Python

Then, save it under the name `lab06Funcs.py`

Also create a separate file called `lab06Tests.py`

    # lab06Tests.py  by Agnes Nitt and Jason Ogg for CS20 lab06,  11/13/2013
    # Tests for lab06Funcs.py 

and save it under the name `lab06Tests.py`

### Step 0c: Copying some files into your lab06 directory

We're going to create three new files and copy/paste the code and data from the links below. Same steps as the last lab: File => New Window, copy/paste, Save As.

- [makeWebPageExample.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab06/master/makeWebPageExample.py)
- [sb2009weather.csv](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab06/master/sb2009weather.csv)
- [students.txt](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab06/master/students.txt)

You can use IDLE as your editor. Be sure to save the names of the files exactly as shown above, with the correct extensions (`.py`, `.csv`, `.txt`). You'll learn what csv means in a minute if you don't know already, but just follow the instructions for now.


Step 1: Learning how to make simple web pages by hand
-----------------------------------------------------

In this step, we'll learn how to make a simple web page.

(You'll eventually need to repeat step 1 for both pair partners so that each of you has a web page.)

The first web page we will create will be at the following URL (except it will have your username in place of the words "yourusername".)

So the first thing we need to do is create the folder that corresponds to this URL.

<http://www.cs.ucsb.edu/~yourusername/cs20/lab06/sample.html>

### Step 1a: Making the directory for the web page

Bring up a terminal, and use these two commands:

    -bash-4.1$ mkdir -p ~/public_html/cs20/lab06
    -bash-4.1$ cd ~/public_html/cs20/lab06

The first command is the familiar mkdir command—but with an extra option. The -p option stands for path and indicates that the command should create the entire path—that is, with one command, we'll create:

    ~/public_html
    ~/public_html/cs20
    ~/public_html/cs20/lab06

The second command (`cd ~/public_html/cs20/lab06`) puts us all the way down there—three directories down—with just one command. This would be the equivalent of doing all of the following commands—but we did it with just two commands!

    -bash-4.1$ cd
    -bash-4.1$ mkdir public_html
    -bash-4.1$ cd public_html
    -bash-4.1$ mkdir cs20
    -bash-4.1$ cd cs20
    -bash-4.1$ mkdir lab06
    -bash-4.1$ cd lab06

Note also, how many mouse clicks it would take to do all of that with clicking in windows—this is a case where the command line definitely saves us effort and time!

### Step 1b: Making the HTML code for the web page

To create the HTML code, we need to use some kind of program that allows us to create and edit files.

If you don't already know one of the Unix-based text editors (emacs, vi, or vim—or if you MUST, nano), the easiest things to do is just use the editor that is already built into IDLE. That is, we'll just "pretend" we are making a new Python file, but in the end, we'll save it as an HTML file.

This causes a bit of a quirk, as we'll see—since IDLE at first thinks we are writing Python code, it will try to use colors that are appropriate to Python code. Once we save the file with a name that ends in .html, this quirk will go away.

If you already know another Unix text editor—emacs, vi, or vim—you can use one of those. If you are interested in learning one of those, your instructor can point you to resources for learning those—if you are going on to CS16, you'll need to learn that skill eventually anyway.

Open up IDLE (the command, as you may know by now, is idle), and go to "New" to create a new window—the kind of window that you would normally use for Python function definitions.

But instead of typing in Python code, type in the following—this is HTML code, the language used for making web pages. Use your name instead of "Jennifer" and alter gender pronouns as desired.

Note that I made this an image—that means you have to type it, you can't just copy and paste.

Typing it will help you to learn the HTML code—as you type, you'll be learning the syntax (i.e. the rules of HTML coding.)

![F13_Labs_lab06_SimpleWebPage.png](/images/F13_Labs_lab06_SimpleWebPage.png)

Notice that the words is and for come up in orange, and everything after the ' mark comes up in green—until the end of the line. Can you figure out why? (Hint: it has to do with that fact that IDLE thinks you are trying to write Python code)

The next step is to save this as an HTML file. You'll use the normal way of saving, but there is a small change that is crucial to getting your page to save correctly—so follow along with the diagrams below.

First, use the "Save As" option from the File menu:

![F13_Labs_lab06_SaveAsOption.png](/images/F13_Labs_lab06_SaveAsOption.png)

Then, in the box that comes up, navigate to the *public\_html/cs20/lab06 directory*.

Depending on what directory you were in when you typed the idle command, you might already be there.

![F13_Labs_lab06_NavigatingTo_public_html.png](/images/F13_Labs_lab06_NavigatingTo_public_html.png)

Once you are in the *public\_html/cs20/lab06* directory—pull down the drop box at the bottom where you can select All files (\*) instead of Python and text files (\*.py,\*.pyw,\*.txt) as shown above. This is important, because you want to save your file as a .html file instead of as a Python file.

(**NOTE: The image below shows lab04 instead of lab06. This isn't a typo, so don't bother reporting it**--I'm reusing this image from a previous quarter when this was lab04. I just didn't think it was worth the time to redo the image just to change the lab nunber.)

![F13_Labs_lab06_NavigatingTo_cs8_lab06_andSelectingAllFiles.png](/images/F13_Labs_lab06_NavigatingTo_cs8_lab06_andSelectingAllFiles.png)

Then, type in the name sample.html as the filename, as shown below. (Again, it says lab04, when it should say lab06, but you're young---you'll adjust.)

![F13_Labs_lab06_puttingIn_sample.html_asName.png](/images/F13_Labs_lab06_puttingIn_sample.html_asName.png)

Once you've saved the file with a name ending in .html, you should see that the special coloring that was intended for Python all goes away as shown below:

![F13_Labs_lab06_puttingIn_sample.html_withoutColors.png](/images/F13_Labs_lab06_puttingIn_sample.html_withoutColors.png)

Your file should now be on the web! You can look at the URL shown below to verify this (again, replacing "~yourusername" with your username):

<http://www.cs.ucsb.edu/~yourusername/cs20/lab06/sample.html>

It should look something like this:

![F13_Labs_lab06_whatWebPageShouldLookLike.png](/images/F13_Labs_lab06_whatWebPageShouldLookLike.png)

### Step 1c: Troubleshooting your HTML (if things don't look right)

If you find that the web page doesn't look right, check your HTML code for any mistakes. Here's a quick guide to how HTML code works.

In general, HTML consists of pairs of open tags and close tags, that must match. For example:

-   `<h1>` matches with `</h1>`, and signifies the beginning and end of a heading
-   `<p>` matches with `</p>` and signifies the beginning and end of a paragraph
-   `<body>` matches with `</body>` and says everything between is the body of the webpage.
-   `<title>` matches with `</title>` and says everything in between is the title of your page—the part that appears in the title bar at the top of the window.

<!-- -->

-   Some common mistakes:
    -   Be sure that you didn't use a backslash (\\) instead of a forward slash (/)
    -   Be sure that you didn't use two open tags (`<h1>Jennifer's test web page<h1>`) instead of an open and a close tag.

Your pair partner may be able to help you spot any differences between the sample code given, and the code you need to type.

### What if I get "Forbidden"?

If you get a message "Forbidden" when trying to access the page (rather than page not found) it may have to do with file permissions. To fix the problem, you'll need to type these Unix commands:

    -bash-4.1$ chmod 711 ~
    -bash-4.1$ chmod -R 755 ~/public_html

These chmod commands use octal numbers to change the permission modes of files and directories

-   Hence "chmod" for change mode
-   By permissions, we mean "who is allowed to see the files".

The details of how file permissions work—and how those connect to octal numbers—are explained on the following web page which you may like to explore another time.

<http://www.cs.ucsb.edu/~pconrad/cs8/topics/chmodQuiz1/>

For now, we need to move on though, because there's lots more to do on today's lab!

### IMPORTANT NOTE IF WORKING IN A PAIR

If you are working a pair, at some point before this lab is due, you must repeat Step 1 for the other pair partner in your group—you'll both be responsible (if registered as a pair) that each of you has the simple web page shown above.

But for now, I suggest you keep going with step 2, and come back and do that later.

Step 2: Preparations
--------------------

### Step 2a: Understanding the role of data files

In working with Python so far, we have mostly been working with either one of a few situations:

-   We've used Turtle graphics to draw interesting and fun shapes.
-   We've developed Python functions that can take some parameters, do a computation, and return a result.
-   We've then used Python's testing framework (unittest) to test whether those functions return the expected results.

However, in many real world applications, what we ultimately want to do is examine some data, and answer some questions about the data. Here are some examples:

#### Example 1: A data file with students and majors

Here is a data file listing some students names, and their majors.

    SHARON, ROBINSON, PHYSICS 
    BRIAN, CLARK, MUSIC
    MICHELLE, RODRIGUEZ, UNDEC
    RONALD, LEWIS, MATH
    LAURA, LEE, ENGLISH
    ANTHONY, WALKER, UNDEC
    SARAH, HALL, CS
    KEVIN, ALLEN, CHEM
    KIMBERLY, YOUNG, UNDEC
    JACOB, HERNANDEZ, STATS

Note: these are fictional students

-   I took the first and last names from the name distribution data of the [1990 Census](Data:_1990_Census_Name_Distribution "wikilink")
-   I picked some majors arbitrarily from this [list of undergraduate degree programs at UCSB](http://my.sa.ucsb.edu/catalog/current/UndergraduateEducation/UndergraduateDegreeList.aspx)

Suppose we want to know:

-   How many students have "undeclared" as their major?
-   Which students are these "undeclared" students?

Each line in this file is the following format:

FIRSTNAME, LASTNAME, MAJOR

As we will see, we can use various Python functions and methods to turn this into a list of Student [namedtuples](https://foo.cs.ucsb.edu/8wiki/index.php/Python:_Named_Tuples) and then write functions that work on a list of Students to answer various questions.

#### Example 2: Earthquake Data

Here is some data on earthquakes that occurred during a three hour period on Monday, September 7, 2010.

    Src,Eqid,Version,Datetime,Lat,Lon,Magnitude,Depth,NST,Region
    nc,71272610,0,"Monday, September  7, 2010 16:49:28 UTC",38.8148,-122.8097,1.0,2.00,12,"Northern California"
    nn,00291988,1,"Monday, September  7, 2010 16:48:29 UTC",37.1950,-114.9640,1.6,0.00,24,"Nevada"
    nn,00291985,1,"Monday, September  7, 2010 16:37:29 UTC",39.3630,-118.1420,1.9,2.00,17,"Nevada"
    ak,10008422,1,"Monday, September  7, 2010 16:25:46 UTC",62.5900,-148.8269,2.0,5.50,07,"Central Alaska"
    us,2010lgbc,6,"Monday, September  7, 2010 16:24:27 UTC",42.1945,142.7938,5.0,62.10,34,"Hokkaido, Japan region"
    pr,p0925006,1,"Monday, September  7, 2010 16:23:45 UTC",19.5597,-68.9285,3.7,68.00,27,"Dominican Republic region"
    us,2010lgba,6,"Monday, September  7, 2010 16:12:21 UTC",-10.2017,110.6088,6.1,15.90,61,"south of Java, Indonesia"
    ci,14507596,1,"Monday, September  7, 2010 15:24:51 UTC",33.9095,-118.3215,1.7,12.40,30,"Greater Los Angeles area, California"
    ak,10008412,1,"Monday, September  7, 2010 14:57:39 UTC",61.1263,-151.9616,1.8,100.00,14,"Southern Alaska"
    us,2010lga8,Q,"Monday, September  7, 2010 14:42:22 UTC",23.6065,126.3178,4.8,10.00,33,"southeast of the Ryukyu Islands, Japan"
    ci,14507588,1,"Monday, September  7, 2010 14:13:01 UTC",33.9783,-116.8166,1.5,12.10,24,"Southern California"

Similar data can be found at the link below for earthquakes from the past hour, day, or week.

<http://earthquake.usgs.gov/earthquakes/map/> 
(There is a download link on the left, and an archive accessible through Options, if you're interested.)

This data is a bit more complex—it is in a format called "CSV", or "comma-separated values".

-   Notice that there is a header line that has the names of the fields (e.g Src, Eqid, etc.)
-   There are also "" quotation marks around some fields, such as the "Datetime", and "Region"—this is because there may be commas inside these fields that should not be treated as field separators.
-   Processing this data could be a bit more complex because of these embedded commas, but there are Python functions that can help us do it easily.

With this data we may want to ask questions such as:

-   How many earthquakes have magnitude 3.0 or larger?
-   Which earthquake had the largest magnitude?
-   Which earthquake was closest to UCSB (with latitude and longitude 34.41254, -119.84813)?

### Why learning about data files is important

In the real world, this data often comes from a file on a hard drive. So learning to read data from a file into a program is a very important concept, and a very practical and useful tool.

The simplest kind of file is a basic "text file"—the kind of file you can edit in one of several ways:

-   With the IDLE editor on any machine that runs IDLE
    -   We edit the files the same way we edit Python files, but we save them with the .txt extension
-   On Windows with programs such as "Notepad"
-   On Mac with programs such as "TextEdit"
-   On Unix systems with editors such as "vi", "vim", or "emacs".

There are other real world data sources—such as web sites, databases, and spreadsheets, just to name a few. In practice, working with each of these data sources involves variations on basic techniques that we can first learn by working with plain text files. So, that is a great place to start.

Of course, there are many programs that you can use to work with data files—spreadsheet programs are the most common. Most of the questions we'll be exploring in this lab are questions you could answer with a simple spreadsheet like Excel. However, there are three things to keep in mind:

-   Since this is an intro class, we have to start with simple questions to begin to build our skills.
-   Once you develop your skills with using Python to manipulate data files, you may find some types of questions are easier to answer with a custom Python program than with a spreadsheet.
-   Excel itself is only a computer program—someone had to write it.
-   We are starting with the basic techniques that would lead you—with further study of programming and computer science—to understand how to write your own spreadsheet tool.

### Read more about working with data files (and review strings and lists) in your textbook

Your textbook briefly discusses working with data files in Chapter 4, section 4.6.

You may also find it helpful to look at these sections about strings and lists:

-   Techniques for working with strings from Sections 2.3 and 5.4
-   Techniques for working with lists from Section 5.2

or review the notes from this lecture regarding lists. [S16:Lectures:04.07](https://foo.cs.ucsb.edu/8wiki/index.php/S16:Lectures:04.07)

### Step 2b: Learning about Named Tuples

You'll next need to read about named tuples.  Conrad will go over these in lecture on Thu 05/19, but you are encouraged to read about them and explore them here:

-   This [tutorial on Named Tuples](https://foo.cs.ucsb.edu/8wiki/index.php/Python:_Named_Tuples) linked earlier in the lab as well
-   The sample code from these two CS8 Lectures shows some additional examples: [F13:Lectures:11.05](https://foo.cs.ucsb.edu/8wiki/index.php/F13:Lectures:11.05), [S14:Lectures:05.07](https://foo.cs.ucsb.edu/8wiki/index.php/S14:Lectures:05.07)

Step 3: Creating data files
---------------------------

Open up IDLE

Use this sequence of commands so that your current default directory is ~/github/CS20-S16-lab06, and you have idle open in that directory:

    cd ~/github/CS20-S16-lab06
    idle

Then open up a window where you can create a new file. This time, however, we are not going to create a Python program (at least not at first.) We are going to create a data file.

In the new window, type in the following (or copy and paste it from this page into the window.)

    SHARON, ROBINSON, PHYSICS 
    BRIAN, CLARK, MUSIC
    MICHELLE, RODRIGUEZ, UNDEC
    RONALD, LEWIS, MATH
    LAURA, LEE, ENGLISH
    ANTHONY, WALKER, UNDEC
    SARAH, HALL, CS
    KEVIN, ALLEN, CHEM
    KIMBERLY, YOUNG, UNDEC
    JACOB, HERNANDEZ, STATS

Then, save the file with the name `students.txt`

-   NOTE: Do NOT put a .py on the end. If the program tries to put a .py on the end, delete it. We want `students.txt`, not `students.txt.py` or `students.py`.

If you started in the ~/github/CS20-S16-lab06 directory before starting IDLE, when you go to save the file, it should automatically try to save the file in your ~/github/CS20-S16-lab06 directory.

Now that you've saved this file, it should be possible to open this file at the Python prompt. Try typing this at the Python prompt (note that you don't type the &gt;&gt;&gt;—that's the prompt!)

    >>> infile = open('students.txt','r')
    >>>

If you get back another `>>>` prompt as shown above, you are in good shape. If so, congratulations—move on to Step 3.

If not, see the "What if it doesn't work" section below.

### What if it doesn't work?

If, instead, you something like the following, then something is wrong:

    >>> infile = open('students.txt','r')
    Traceback (most recent call last):
    File "<pyshell#1>", line 1, in <module>
        infile = open('students.txt','r')
    File "/Library/Frameworks/Python.framework/Versions/3.0/lib/python3.0/io.py", line 278, in __new
        return open(*args, **kwargs)
    File "/Library/Frameworks/Python.framework/Versions/3.0/lib/python3.0/io.py", line 222, in open
        closefd)
    File "/Library/Frameworks/Python.framework/Versions/3.0/lib/python3.0/io.py", line 619, in __init__
        _fileio._FileIO.__init__(self, name, mode, closefd)
    IOError: [Errno 2] No such file or directory: 'students.txt'
    >>>

The most important part of this is the last line: "No such file or directory: 'students.txt'"

What Python is telling us is that it can't find this file. This may be because you didn't name it properly, or it may be because Python is not looking in the right place for it.

You are encouraged to do this lab by ssh'ing in to CSIL--but if, instead, you are working directly on your own machine that runs Mac or Windows, you may need to concatenate a directory with your filename, like this, on Mac:

    >>> where = '/Users/Bob/cs20/lab06/'
    >>> infile = open(where + 'students.txt', 'r')

or like this on Windows:

    >>> where = 'c:/cs20/lab06/'
    >>> infile = open(where + 'students.txt', 'r')

There is nothing special about the variable name `where`—you could call it `myDir` or whatever name you like. We are just defining a string variable that we are adding in front of the filename to tell Python where to find it.

What you put after `where =` will depend on where you created your lab06 directory, and will depend on whether you are on working on Windows XP, Windows Vista, Mac, or Linux.

The same trick might be needed on CSIL if you didn't cd into the `~/github/CS20-S16-lab06` directory before typing `idle`—in this case, use `where='/path/to/your/home/directory/cs20/lab06'`

### A note about the home directory symbol `~`

As you may know `~` is a symbol for your home directory that you can use when you type commands in at the `-bash-4.1$` prompt (i.e. the *shell*.)

However, you usually *can't* use `~` as an abbreviation for your home directory when accessing a file inside a program (whether that program is in Python, or C, or Java, or whatever).

That's because `~` is a symbol for home directory only in the *shell*, e.g. at the `-bash-4.1$` prompt

Instead, determine what the full path to your home directory is by opening a new terminal window, doing a `cd` to return to your home directory, and then typing `pwd`. What comes up is the full path to your home directory, e.g. `/fs/home1/student/j/jsmith` or `/cs/student/jsmith`

So, that's what you need to use in your `where` variable:

-   Incorrect: `where="~/cs8/lab06/"`
-   Correct: `where="/cs/student/jsmith/cs8/lab06/"`
-   Correct: `where="/fs/home1/student/j/jsmith/cs8/lab06/"`

Talk it over with your pair partner to make sure you both understand—and if it still isn't clear, ask your TA or instructor for help.


Step 4: Opening an input file, reading some data, closing the file
------------------------------------------------------------------

If you have reached this point, you've already created a file named 'students.txt' with lines such as

    SHARON, ROBINSON, PHYSICS
    BRIAN, CLARK, MUSIC
    etc...

and you've opened it with a line like this (possibly with an extra where variable if needed to specify the location of the file)

    >>> infile = open('students.txt','r')
    >>>

Now, the question is, what can we do with an open file?

Since we opened this file with the 'r' flag, this is a file we have opened for reading. That means we can read data from this file into Python variables, as shown below. Try this at the IDLE prompt:

    >>> for line in infile:
          print(line)

You should get output like this. Notice the extra newline in between each name.

There are two newlines because one comes from the print function in Python, and the other was in the original data file. We'll show how to get rid of these extra newlines in a later step.

    >>> for line in infile:
          print(line)
     

    SHARON, ROBINSON, PHYSICS

    BRIAN, CLARK, MUSIC

    MICHELLE, RODRIGUEZ, UNDEC

    RONALD, LEWIS, MATH

    LAURA, LEE, ENGLISH

    ANTHONY, WALKER, UNDEC

    SARAH, HALL, CS

    KEVIN, ALLEN, CHEM

    KIMBERLY, YOUNG, UNDEC

    JACOB, HERNANDEZ, STATS

    >>>

We see that we can read data from the file into a variable and use a for loop to print each line. But what would be more useful would be to store the data in a list of Students (where Student is a Named Tuple with the fields firstName, lastName and major)—that gives us more options as we work with the data. We'll do that in next step.

First, though we need to close the file. This frees up resources on the computer, and allows us to reopen the file and start reading it from the beginning. So, type this next:

    >>> infile.close()
    >>>

### Something to notice...

Notice the difference between the syntax of:

-   opening a file, e.g. `infile = open("students.txt","r")`
-   and closing a file, e.g. `infile.close()`

In the first case, we are using the open function, and writing an assignment statement that creates a new variable called infile. We can choose any name we want for this variable (e.g. studentFile, theFile, etc.) It is not required that this variable end with "file"—for example, we could call it "inputData", or even "fred" if we want. But it is good practice to name it something that reminds us it is a variable that stands for an open file.

In the second case, we are using a method of the file variable—that is why we write the variable name (infile) first, and then write a dot (.), and finally the name of the function (close).

This is similar to how we wrote `t.forward(100)` or `t.right(90)` when the variable `t` referred to a turtle—`forward()` and `right()` are methods of any variable that refers to a Turtle, just like `close()` is a method of any variable that refers to a file object.

-   In this class we only use methods—we don't write any ourselves.
-   However, if you take future CS courses, you may see the idea of methods come up again, and you'll learn how to write your own methods:
    -   You'll see methods again in CS24 in C++, and in CS56 in Java

### To review...

In this step, we did three things:

1. Opened a file with `infile = open('students.txt','r')`
2. Read data from the file with a loop:

    ```
    for item in infile:
        print(item)
    ```

3. Closed the file using `infile.close()`

We'll do these three things again in the next step of this lab, but instead of just printing out the data, we'll read it into a list so we can work with it further, even after the file is closed.

Step 5: Reading data into a list
--------------------------------

In this step, we'll read the data into a list of strings.

### Step 5a: Learning about opening files

Type the following in at the Python prompt:

    >>> infile = open('students.txt','r')
    >>> inputList=[]
    >>> for item in infile:
             inputList = inputList + [item]

          
    >>> infile.close()
    >>> 

Once you've typed in those four lines, you can type the name of the variable inputList at the Python prompt to see what inputList contains. You should see something like this:

    >>> inputList
    ['SHARON, ROBINSON, PHYSICS \n', 'BRIAN, CLARK, MUSIC\n', 'MICHELLE, RODRIGUEZ, UNDEC\n',
    'RONALD, LEWIS, MATH\n', 'LAURA, LEE, ENGLISH\n', 'ANTHONY, WALKER, UNDEC\n', 
    'SARAH, HALL, CS\n', 'KEVIN, ALLEN, CHEM\n', 'KIMBERLY, YOUNG, UNDEC\n', 
    'JACOB, HERNANDEZ, STATS\n']
    >>>

It should be clear from the \[ \] characters and the commas, but in case it isn't, what we have is a list of strings:

    >>> type(inputList)
    <class 'list'>
    >>> for item in inputList:
          print(type(item))

    <class 'str'>
    <class 'str'>
    <class 'str'>
    <class 'str'>
    <class 'str'>
    <class 'str'>
    <class 'str'>
    <class 'str'>
    <class 'str'>
    <class 'str'>
    >>>

So, what can we do with this list?

First we'll write a function that takes a string such as:

    'SHARON, ROBINSON, PHYSICS \n'

and returns a named tuple such as:

    Student(fname='SHARON', lname='ROBINSON', major='PHYSICS')

We'll call this function `makeStudentFromDataFileLine`. It will take one parameter, `dataFileLine`.

With that function, we can go through the list of strings and turn it into a list of `Student` named tuples.

The next step explains how to do that.

### Step 5b: Adding code to `lab06Funcs.py` to read the file into a list of Students

Here's how we define a named tuple. Put this in your `lab06Funcs.py` file, just after the opening comment.

    from collections import namedtuple
    Student = namedtuple("Student","fName lName major")

Then, add this bit of code just afterwards to read the data file into a list of strings:

    def lineToStudent(inputLine):
       """
       creates a Student (named tuple) from an inputLine (string)
       >>> lineToStudent('SHARON, ROBINSON, PHYSICS')
       Student(fName='SHARON', lName='ROBINSON', major='PHYSICS')
       >>> 
       """

       itemStripped = inputLine.strip()  # remove the newlines
       itemSplit = itemStripped.split(',')  # split into a list at the comma

       # now, itemSplit[0] is the first name,
       #      itemSplit[1] is the last name
       #      itemSplit[2] is the major
       # but each might still have spaces
      
       return Student(itemSplit[0].strip(), itemSplit[1].strip(), itemSplit[2].strip())

Then after that function definition, add this code:


    def Main():
        infile = open('students.txt', 'r')
        inputList = [] # empty list of all lines in file

        # read all lines from file into inputList

        for line in infile:
            inputList = inputList + [line]

        # Now inputList is a list of strings. 

        # make variable students "global" so it is 
        # available at Python prompt, and 
        # initialize to empty list

        global students 
        students = [] 

        # make a list of students from the inputList

        for item in inputList:
            thisStudent =  lineToStudent(item)
            students = students + [thisStudent]

        # end of Main()

    if __name__ == "__main__":
        Main()

Put this code in your file, and use the Run/Run Module\[F5\] command to compile the code. Assuming you have no errors, you should now be able to type `students` at the Python prompt and see the list of students, like this:

    >>> ================================ RESTART ================================
    >>>  
    >>> students
    [Student(fName='SHARON', lName='ROBINSON', major='PHYSICS'), Student(fName='BRIAN', lName='CLARK', major='MUSIC'), 
    Student(fName='MICHELLE', lName='RODRIGUEZ', major='UNDEC'), Student(fName='RONALD', lName='LEWIS', major='MATH'), 
    Student(fName='LAURA', lName='LEE', major='ENGLISH'), Student(fName='ANTHONY', lName='WALKER', major='UNDEC'), 
    Student(fName='SARAH', lName='HALL', major='CS'), Student(fName='KEVIN', lName='ALLEN', major='CHEM'), 
    Student(fName='KIMBERLY', lName='YOUNG', major='UNDEC'), Student(fName='JACOB', lName='HERNANDEZ', major='STATS')]
    >>>

### Step 5c: A note about the `strip()` and `split()` methods

Before we continue to work with the list of students, a short digression.

Look back at the lineToStudent function. Find where it uses the `strip()` function and the `split()` function. These functions are both string *methods*—that is, they are applied to a string variable using the dot operator, e.g. `item.strip()` or `itemStripped.split(',')`

As a reminder, we said "methods" before when we used the Turtle functions back in lab03—the turtle had "methods"—functions we applied using the "dot" operator.

-   The `split()` method is used to split a string into a list of strings. The argument is a string that is used as the character that separates the items (in this case, a comma.)
-   The `strip()` method simply takes a string and returns a new string that is the same as the old string, except that any spaces, tabs or newline characters ('whitespace') at the beginning and the end has been 'stripped off'.

### Step 5d: An Example Computation on this Data: the whatMajor function

Now that we have this data, we can do lots of different kinds of computations on this data.

For example, here is a function that, given the first name of a student, returns us a string indicating their major. (Note that if more than one student matches, we'll only return the first match. For any given function call, you can only return once!)

Add this function definition into your file, right after the definition of lineToStudent, and then compile again:

    def whatMajor(fName, listOfStudents):
        """
        return the major of first student in listOfStudents with first name fName, False if none found

        >>> whatMajor("FRED",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
        'HISTORY'
        >>> 
        """

        for i in range(len(listOfStudents)):

           # step through every item in listOfStudents
           # when you find a match, return that students's major

           if listOfStudents[i].fName == fName:
              return listOfStudents[i].major

        # if you got all the way through the loop and didn't find
        #  the name, return False

        return False

Then, set up the `lab06Tests.py` file to test this function. Into the file, paste this "boilerplate code" for testing:

    import unittest            
    from lab06Funcs import *   

    class TestLab06Functions(unittest.TestCase): 

        # tests for someFunction 

        #def test_someFunction(self):
        #    self.assertEqual(  functionCallHere(param1, param2),   expectedResultGoesHere )

        # End of tests for lab06

    def runTestsWithPrefix(testFile,prefix):
        """
        run only tests from testFile with a certain prefix
        Example: runTestsWithPrefix("lab03Tests.py","test_isPrimaryColor")
        """
        loader = unittest.TestLoader()
        loader.testMethodPrefix = prefix
        suite = loader.discover('.', pattern = testFile) 
        unittest.TextTestRunner(verbosity=2).run(suite)


    # When you run this file, it runs either ALL the tests, or
    # just some tests.  It depends on which line you comment out (or not)

    if __name__ == '__main__':

        # To run ALL tests, uncomment the "unittest.main(exit=False)" line
        
        # unittest.main(exit=False)  

        # Uncomment "runTestsWithPrefix" line to run just SOME tests
        #    First parameter is name of file with tests
        #    Second parameter is prefix starting with test_ 
        #      such as test_FtoC  or test_isString

        runTestsWithPrefix("lab06Tests.py","test_whatMajor") 

Then, write some tests for your whatMajor function. Replace the comment that says:

        # tests for someFunction 

with:

        # tests for whatMajor 

and then, replace the comment:

        #def test_someFunction(self):
        #    self.assertEqual(  functionCallHere(param1, param2),   expectedResultGoesHere )

with a test for whatMajor like this one.

-   This test case sets up the variable students as a list of students.
-   Then it calls whatMajor with:
    -   "FRED" as the first parameter
    -   students as the second parameter
-   It asserts that the result should be "HISTORY"

<!-- -->

        def test_whatMajor_1(self):
            students = [Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")]
            self.assertEqual(  whatMajor("FRED",students),  "HISTORY" )

Now, set up some tests cases with your own name and major, and that of a few other people, real or made up.

Try testing the function, both at the Python prompt, as well as by running the `lab06Tests.py` file to see that your tests pass.

Now it is your turn to do some coding!

Step 6: Writing five functions that work with a list of Students
----------------------------------------------------------------

Now you need to write five functions on your own.

In each case, be sure to include a "docstring comment" (similar to the one in the `whatMajor()` function above) that

-   starts with a one line description of the function,
-   then has an example of how the function works.

Then, add tests cases to the `lab06Tests.py` file. In each case, modify the line

        runTestsWithPrefix("lab06Tests.py","test_whatMajor") 

changing `whatMajor` to whatever function you are testing.

### Step 6a: `whatLName()`

Using the function `whatMajor()` as a model, write a function that will return the last name of a student, given the student's first name. For now, ignore the possibility that there might be more than one student with a given first name—just return the first match you find. If no students are found with that first name, return False.

The parameters to your function should be the first name to search for and the list of students.

### Step 6b: `countUndec()`

Now write a function that counts the number of students in the list that have "UNDEC" as their major. You'll need to pass in only the list of students, and return the answer as an int.

Use the accumulator pattern on a variable "count". Initialize it to zero, and add one to it each time you find a match. Return the value of count when you are finished.

### Step 6c: `lNamesOfUndec()`

Now write a function that returns the last names of all the students that have "UNDEC" as their major. You'll pass in only the list of students as a parameter. You'll return the answer as a list of strings. If no students were found that have UNDEC as their major, return an empty list.

Use the accumulator pattern on a variable "answerList". Initialize it to an empty list. Go through the list of students. Each time you find a student that has undecided as his/her major, add that students last name to the list.

Return the list you constructed.

### Step 6d: `majorToLNames()`

Now generalize the `lNamesOfUndec()` function—write a function that works exactly the same way, except that it takes two parameters, first a parameter thisMajor, and then the list of students as the second parameter. Instead of looking for "UNDEC", look for thisMajor. Return a list of strings containing all the last names of the students with the major specified by thisMajor. Return an empty list if there are no such students.

### Step 6e: `allStudentsMajoringIn()`

Now generalize further. This function will be the same as `lNamesOfUndec()`, except instead of appending just the last name of each student to the result list, append the entire Student object (i.e. the entire namedtuple). You'll end up with a list of Students, but a list that ONLY contains the students that are majoring in whatever major you passed into the function.

For example, instead of the result of the function being something like this, which is a list of strings representing last names:

    ["CHANG","SMITH","LOPEZ"]

it will be a list of Students, like this:

    [Student(fName='JOAN', lName='CHANG', major='CMPSC'), 
     Student(fName='FRED', lName='SMITH', major='CMPSC'), 
     Student(fName='SHIELA', lName='LOPEZ', major='CMPSC')]

### What to do when done with all of these functions

When you are finished with all of these functions, you are ready for the final challenge in this lab: making a web page from a data file.

But first, change the code at the bottom of `lab06Tests.py` so that it tests all of your functions. That is, comment out:

        # runTestsWithPrefix("lab06Tests.py","test_whatMajor") 

and un-comment the line:

        unittest.main(exit=False)  

That should make `lab06Tests.py` run ALL of your tests, which should now all pass.

Step 7: Making a web page from a data file
------------------------------------------

Now we are going to take `students.txt`, the same data file we've been working with, and turn it into a web page.

As you can see, each line in the input file has the following format:

    FIRSTNAME, LASTNAME, MAJOR

On a web page, we want this data to be in a table like this one:

![F13_Labs_lab06_ExampleTable.png](/images/F13_Labs_lab06_ExampleTable.png)

We will use Python's ability to write to files to accomplish this.

Step 8: Run the code from `makeWebPageExample.py`
-------------------------------------------------

Back at Step 1, you were supposed to copy some files into your lab06 directory.

One of those files was called `makeWebPageExample.py`.

Now, run that file--that is, open it in idle, and select Run (or press F5.)

NOTE: You MUST put yourself into your own `~/github/CS20-S16-lab06` directory with the cd command BEFORE you type `idle`, otherwise, the program won't be able to find the `students.txt` file.

Then at the Python prompt, type this:

    convertStudents2Table("students.txt","table.html")

It should look something like this when you do it—except that instead of pconrad, you'll see your own username:

    >>> convertStudents2Table("students.txt","table.html")
     
     Look for the web page at this URL:
     http://www.cs.ucsb.edu/~pconrad/cs20/lab06/table.html
     Or if working on a PC or Mac, at this one:

     file:///cs/faculty/pconrad/public_html/cs20/lab06/table.html
    >>>

If you read the output carefully, you'll see that what happens next depends on whether you are on CSIL, or on your own PC/Mac—but either way, it involves copying a web address into a browser. When you open up that web address, you should see a table like the one shown above, but with your own data.

Note: if you completed the lab on your own PC or Mac, the web page may be at the "file" URL instead of the http URL.

(Or maybe not. The code definitely works on CSIL and on Macs. I wrote the code so that it will probably work on Windows and Linux too—but since there are so many different possibilities, it is impossible for me to test them all. If you have trouble, just do the lab on CSIL. If it doesn't work, make sure you have a `students.txt` file in the directory where you are running IDLE. You may need to do the same troubleshooting steps listed under "what if it doesn't work" in Step 3. In addition, you may need to revisit the "What if I get 'Forbidden'" section from Step 1.)

Assuming it does work, though, go on to the next step.

Step 9: Making another data file and another web page
-----------------------------------------------------

Create a another file similar to `students.txt`—in the same format, with first name, last name, and major separated by commas—but with different names and majors. Save it with another name, say `friends.txt`.

Run the convertStudents2Table function again—this time, putting in the name of your data file, e.g. "friends.txt" as the first parameter, and "friends.html" as the second parameter.

You should see another web page—this time with the new data you put in your `friends.txt` file formatted as an HTML page.

Step 10: Understanding the example code
---------------------------------------

Now, you need to look through the code in `makeWebPageExample.py` and try to understand how it works.

Note that you do NOT need to spend much time on the following functions—these are supplied for you to make your lives a little easier, but are not that important for you to focus on at this time:

-   `webDirectory()`
-   `webAddress()`
-   `makeWebDirectoryIfItDoesNotExistAlready()`
-   `webPageHeader()`

We'll briefly introduce each of those a little later in the lab—but for the most part, you won't need to touch those.

Instead, skip on down to the definition of the function that we DO want to focus on—the one for which you typed in a function call at the Python prompt—the definition that starts like this:

    def convertStudents2Table(inputFileName,outputFileName):
    ...

This function takes two strings as parameters (e.g. "students.txt" and "table.html").

The first is used as the filename in a call to open that opens an input file:

    studentFile = open(inputFileName,"r")

The second is used as the last part of a filename in a call to open that opens an output file.

The first two lines below create a directory for web pages under your home directory and build up a file name (using string concatenation) that starts with ~/public\_html/cs20/lab06 and ends with the value of outputFileName.

They do so using some functions I'm supplying for you that take care of the complicated stuff (looking up your home directory and your username). (You don't need to worry about the internal details of those functions.)

    makeWebDirectoryIfItDoesNotExistAlready()

    htmlFileName = webDirectory() + "/" + outputFileName


    htmlFile = open(htmlFileName,"w")

Now, we have both an input file and an output file to work with.

The first thing we do is write the "header" to the HTML output file.

Review what we did in step 1 with creating web pages to remind yourself about the structure of an HTML file (
`<html>`, `<head>`,`<body>`, etc.)

This is done via these lines:

    htmlFile.write("<html>\n")
    htmlFile.write(webPageHeader("Table of Students"))

We then have code which writes out the body of the page which contains an H1 heading, and table.

To make sense of the code, you'll need a bit of an overview of how HTML tables work:

### How HTML Tables work

-   In HTML, the code for a table starts with `<table>` and ends with `</table>`.
-   In between, there are table rows that start with `<tr>` and end with `</tr>`
-   Each table row is either a sequence of `<th>...</th>` elements (table headers) or
    `<td>...</td>` elements (table data).
-   Each of the <th></th> elements contains the header for one column,
    -   e.g. the first row: `<tr><th>First` `Name</th><th>Last` `Name</th><th>Major</th></tr>`
-   Each of the <td></td> elements contains the data for one entry in the table,
    -   e.g. the second row `<tr><td>SHARON</td><td>ROBINSON</td><td>PHYSICS</td></tr>`

For more information on HTML Tables, see: <http://www.w3schools.com/html/html_tables.asp>

In general, w3schools.com is a helpful resource for learning about HTML and other web markup, design and programming topics.

### The code that writes an HTML Table

So, we see in the code, some lines that write the first part of the body to the output file:

    htmlFile.write("<html>\n")
    htmlFile.write(webPageHeader("Table of Students"))
    htmlFile.write("<body>\n")
    htmlFile.write("<h1>Table of Students</h1>\n")
    htmlFile.write("<table border='1'>\n")
    # Write the table header
    htmlFile.write("<tr><th>First Name</th><th>Last Name</th><th>Major</th></tr>\n")

Then, there is a loop that reads every line from the file:

    # process every line in the file---and for each one
    # write a line to the html for the web page



    for line in studentFile:

    ...

What do we do for each line? We split it into a list of items, and then print those items, formatted as a row in an HTML table, like this:

       # Convert this line into a list
       lineAsAList = line.strip().split(",")

       # Pull out the first name, last name and major
       fname = lineAsAList[0].strip()
       lname = lineAsAList[1].strip()
       major = lineAsAList[2].strip()


       # Write one line to the table

       htmlFile.write("" +
                      "" + fname + "" +
                      "" + lname + "" +
                      "" + major + "" +
                      "")
            

Only after the entire loop is finished, we write the end of the table, the end of the HTML file, and then close up the files:

    htmlFile.write("</table>\n")
    htmlFile.write("</body>\n")
    htmlFile.write("</html>\n")

    # close the intput file and the output file
        
    studentFile.close()
    htmlFile.close()

There is then a little more code that prints out some messages for the user, telling them where to look for the web page. The output is something the user can copy/paste into the web address bar of their browser to find the file on the web.

Once you think you understand what is going on, you are ready for the challenge of this week's lab.

Step 11: Write a program that formats weather data into a web page
------------------------------------------------------------------

The file `sb2009weather.csv` is a file that contains actual weather data for Santa Barbara for every day during 2009. You copied it into your lab06 directory in a previous step, but here is the link again to it if you cannot find it:

<http://www.cs.ucsb.edu/~pconrad/cs8/14S/labs/lab06/code/sb2009weather.csv>

This data is downloaded from a website at UC Davis: <http://www.ipm.ucdavis.edu/WEATHER/wxretrieve.html>

I removed a few columns to make the data a bit easier to work with

Like most "real-world" data, it contains "imperfections". There are a few missing values, for example, for relative humidity for a few days—those values are just blank.

The file extension .csv stands for "comma separated values". This is a standard way of representing data that can be imported into various programs (e.g. spreadsheets and databases) Look over this file. Here are the first few lines:

    20090101,0.01,61,35,N,2,95.5,61.7 
    20090102,0,57,39,NE,2,93.5,74.5 
    20090103,0,59,42,NE,2,94.6,61.3 
    20090104,0,57,39,NE,3,77.8,38.1 
    20090105,0,60,37,NE,3,82.5,42.2 
    20090106,0,62,41,N,2,87.9,58.4 
    20090107,0,65,41,N,2,88.4,51.1

Each line contains these values, separated by commas:

-   Date in the format YYYYMMDD
    -   You can use string slicing to pull out year, month, day—e.g. what does year\[4:6\] pull out?
-   Precipitation in inches
-   High temperature (°F)
-   Low temperature (°F)
-   Average wind direction
-   Average wind speed (mph)
-   Relative humidity % (max for the day)
-   Relative humidity % (min for the day)

Your job: write a program that reads all the data from this file, and formats it as a web page, so that it looks like this:

![F13_Labs_lab06_sbweather_as_a_table.png](/images/F13_Labs_lab06_sbweather_as_a_table.png)

You can use the `makeWebPageExample.py` as a starting point—but be sure to make appropriate changes:

-   The file you submit should be called `lab06WebWriter.py`
-   The comment at the top should be YOUR comment, not the one I had in `webPageExample.py`
-   More significantly: the main function shouldn't be called `convertStudent2Table`
    -   instead, call it **makeWeatherWebPage**
-   Any variables that refer to student should be changed to something more appropriate.
-   Your code should work by providing a function that you can call like this:

<!-- -->

    makeWeatherWebPage("sb2009weather.csv","sb2009weather.html")

You may want to save a small version of your file—say just the first few lines—to a file called "test.csv" and use that when testing.

When your function can turn any weather file into one like the one shown above, then you are almost done with lab06!

Step 12: Copy the files for your lab to your pair partner's account and run them there also
-------------------------------------------------------------------------------------------

To get full credit on this lab, both partners (or all three partners) need to be showing the web page under their account.

So, before submitting via "turnin", make sure that for both (or all three partners), you can see the web page at:

<http://www.cs.ucsb.edu/~usernamegoeshere/cs20/lab06/sb2009weather.html>

To do that, you need to:

-   copy the lab into each person's account (instructions below)
-   run the function makeWeatherWebPage in each person's account.
-   check that the link above works with each person's username substituted

Note: if you completed the lab on your own PC or Mac, it is important to run the files on CSIL at least once before doing the turnin step, so that the web pages are in place on CSIL.

### Sharing code with your pair partner

The easiest way to share coe with your pair partner is to:

* make sure they are a collaborator on your github repo
* make sure you have done the `git add ...`, `git commit -m 'message'`, `git push origin master` steps.   
* let your pair partner clone the repo, or do a `git pull origin master` if they already cloned it.


Step 13: Final Submission
-------------------------

Before submitting, do your final inspection—look over the rubric, make sure everything looks ok.

We are NOT using submit.cs in this case to test our code or submit. 

The only thing you need to do to submit is to go on Gauchospace, and put in the name of the repo where we can find your code and your web page.


Go to the forum on Gauchospace marked "lab06 submission".

Make a forum post, and in the post, put links to:

* (1) Your github repo for lab06 
* (2) The web pages you made, i.e. https://www.cs.ucsb.edu/~yourusername/cs20

Once you've done that, that's a sign that you are ready for your lab06 to be
"graded", so to speak.


Evaluation and Grading Rubric
=============================

### Professional software documentation practices

### Writing functions that work with a list of Students

Each function should have a docstring, internal comments, and variable names should be chosen appropriately.

-   (15 pts) whatLName() written with good style and works correctly
    -   (10 pts) and has tests cases in lab06Tests.py
-   (15 pts) countUndec() written with good style and works correctly
    -   (10 pts) and has tests cases in lab06Tests.py
-   (15 pts) lNamesOfUndec() written with good style and works correctly
    -   (10 pts) and has tests cases in lab06Tests.py
-   (15 pts) majorToLNames() written with good style and works correctly
    -   (10 pts) and has tests cases in lab06Tests.py
-   (15 pts) allStudentsMajoringIn() written with good style and works correctly
    -   (10 pts) and has tests cases in lab06Tests.py

Making a web page
=================

These steps have to do with the web pages you make at www.cs.ucsb.edu/~youruseridhere/cs8/lab06

-   (40 pts) Both partners (if applicable) or the one solo programmer has a visible web page (this is the one created by hand during the early step of the lab) at www.cs.ucsb.edu/~youruseridhere/cs20/lab06 per instructions above.
    -   Half the points apply to each lab partner's individual web page, but the grade APPLIES TO BOTH PARTNERS.
    -   So if you choose to work together, please be sure you take responsibility for make sure your partner completes this too!
-   (40 pts) Completing a working version of the makeWeatherWebPage function. This will appears in your lab06WebWriter.py file.
    -   The points for this step apply to making sure that the code is written well, and functions correctly. The focus is on the Python code itself.
-   (35 pts) The weather web page is formatted correctly (no visible "glitches")
    -   These points refer to the web page created automatically by the makeWeatherWebPage() function that should appear in the lab06WebWriter.py file.
    -   Columns headers should be appropriate (indicating names of weather items)
    -   HTML page title and H1 header should be aappropriate ("SB Weather", not "Students")
    -   For folks working in pairs, if no weather web page appears on EITHER account, you lose all 35 of these points. You also lose all thirty-five of these points if the weather web page that appears was NOT created by your Python code (you get no points for creating one of these by hand.)
-   (30 pts) For PAIRS: Each pair partner has a copy of the formatted weather webpage on his/her account
    -   for SOLO programmers, these points get added into the previous item, i.e. the previous item is worth sixty-five points instead of thirty-five.)


Professional software documentation practices
---------------------------------------------

In general, you get (30 pts) for following these practices, or lose those points not following them.

However, additional points from other items on rubric may be "at risk" if the practices below are not followed---deductions are at the discretion of the grader.

-   Naming your files lab06Funcs.py, lab06Tests.py, lab06WebWriter.py
-   Putting a comment on the first two lines of each file according to the instructions given (with both pair partners names, if applicable.)
-   All variable name shoud be appropriate (e.g. "students" vs. "weather" in your lab06WebWriter.py file.)
-   Submitting on time

