![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > shell basics 

![rtfm](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg)

## Intro
In this session, we will introduce shell scripriting and have a look at the most basic scripting commands. Hang tight. 

## Resources
1. [What is the shell?](http://linuxcommand.org/lc3_lts0010.php)
2. [Navigation](http://linuxcommand.org/lc3_lts0020.php)
3. [Looking around](http://linuxcommand.org/lc3_lts0030.php)
4. [A guided tour](http://linuxcommand.org/lc3_lts0040.php)
5. [Manipulating files](http://linuxcommand.org/lc3_lts0050.php)
6. [Working with commands](http://linuxcommand.org/lc3_lts0060.php)
7. [Reading man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
8. [Keyboard shortcuts](https://www.howtogeek.com/181/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
9. [LTS](https://wiki.ubuntu.com/LTS)
10. [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)

## Man or help

* ```cd```
* ```ls```
* ```pwd```
* ```less```
* ```file```
* ```ln```
* ```cp```
* ```mv```
* ```rm```
* ```mkdir```
* ```type```
* ```which```
* ```help```
* ```man```


## Learning objectives
By the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/?fbclid=IwAR2K5_BGPVo0QjJXkOIIqNsqcXK4lTskPWJvA0asKQIGtCPWaQBdKmj1Ztg) __Without the help of google__ the following concepts

####  General Objectives
* [X] What does RTFM mean?
* [X] What is shebang?

#### What is the shell?

* [X] What is the shell
* [X] What is the difference between a terminal and a shell
* [X] What is the shell prompt
* [X] How to use the history (the basics)

#### Navigation

* [X] What do the commands or built-ins ```cd```, ```pwd```, ```ls``` do
* [X] How to navigate the filesystem
What are the ```.``` and ```..``` directories
* [X] What is the working directory, how to print it and how to change it
* [X] What is the root directory
* [X] What is the home directory, and how to go there
* [X] What is the difference between the root directory and the home directory of the user root
* [X] What are the characteristics of hidden files and how to list them
* [X] What does the command cd - do

#### Looking around

* [X] What do the commands ```ls```, ```less```, ```file``` do
* [X] How do you use options and arguments with commands
* [X] Understand the ```ls``` long format and how to display it
* [ ] [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
* [X] What does the ```ln``` command do
* [X] What do you find in the most common/important directories
* [X] What is a symbolic link
* [X] What is a hard link
* [X] What is the difference between a hard link and a symbolic link

#### Manipulating files

* [X] What do the commands ```cp```, ```mv```, ```rm```, ```mkdir``` do
* [X] What are wildcards and how do they work
* [X] How to use wildcards

#### Working with commands

* [X] What do ```type```, ```which```, ```help```, ```man``` commands do
* [X] What are the different kinds of commands
* [X] What is an alias
* [X] When do you use the command ```help``` instead of ```man```

#### Reading man pages

* [X] How to read a man page
* [X] What are man page sections
* [X] What are the section numbers for User commands, System calls and Library functions

#### Keboard shortcuts for bash
* [X] Common shortcuts for Bash

## Tasks

0. [Where am I?](./0-current_working_directory) : A script that prints the absolute path of the current working directory.
1. [What's in there?](./1-listit) : A script that displays the contents of your current directory.
2. [There is no place like home](./2-bring_me_home) : A script that changes the working directory to the user's home directory.
3. [The long format](./3-listfiles) : A script that displays the current directory contents in a long format.
4. [Hidden files](./4-listmorefiles) : A script that displays the current directory contents including hidden files.
5. [I loce numbers](./5-listfilesdigitonly) : A script that displays the current directory contents, using long format, while displaying group IDs in numeral and show hidden files.
6. [Welcome holberton](./6-firstdirectory) : A script that will create a directory named `holberton` in the `/tmp/` directory.
7. [Betty in Holberton](./7-movethatfile) : A scipt that will move a file called `betty` from home to the new directory created above.
8. [Bye bye Betty](./8-firstdelete) : A script that will delete file `betty` from the new location.
9. [Bye bye Holberton](./9-firstdirdeletion) : A script that will delete the directory `holberton` that is in the `/tmp/` directory path.
10. [Back to the future](./10-back) Change working directory to the previous one.
11. [Lists](./11-lists) List all files (*even ones with names beginning with a period character, which are normally hidden*) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
12. [File type](./12-file_type) A script that prints the type of the named file `iamafile`. The `iamafile` will be in the `/tmp/` directory when we will run your script.
13. [We are symbols, and inhabit symbols](./13-symbolic_link) Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.
14. [Copy HTML files](./14-copy_html) Create a script that copies all `html` files from the current working directory to the parent working directory while only copying files that did not exist.
15. [Let's move](./100-lets_move) A script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
16. [Clean Emacs](./101-clean_emacs) A script that deletes all files in the current directory that end with the character `~`.
17. [Tree](./102-tree) A script that creates the directory `welcome/`, `welcome/to/` and `welcome/to/holberton`.
18. [Life is a series of commas, not periods](./103-commas) A script that lists all the files and directories of the current directory separated by commas `,`.
19. [File type: Holberton](./holberton.mgc) Create a magic file `holberton.mgc` that can be used with the command `file` to detect `Holberton` data files always contain the string `HOLBERTON` at offset 0.
